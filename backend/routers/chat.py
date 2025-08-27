from fastapi import APIRouter
from backend.model.ChatRequest import ChatRequest
from backend.chatbot.censored_lang_filter import is_inappropiate
from backend.chatbot.text_generator import generate_response
from backend.retriever.search import get_summary_by_title_from_db, search_books_by_theme_db

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
	user_message = request.message.strip()

	# 1. Comandă de ieșire (opțional)
	if user_message.lower() in {"exit", "quit"}:
		return {"response": "👋 Goodbye!"}

	# 2. Filtru de limbaj neadecvat
	if is_inappropiate(user_message):
		return { "response": "🚫 Please use appropriate language. I'm here to help you with book recommendations." }

	# 3. Comandă explicită pentru rezumat
	if user_message.lower().startswith("show me the summary for"):
		title = user_message[len("show me the summary for"):].strip()
		summary = get_summary_by_title_from_db(title)
		return {"response": summary}

	# 4. Chat semantic + GPT (RAG)
	results = search_books_by_theme_db(user_message)
	if not results["documents"][0]:
		print("⚠️ Nothing found in ChromaDB. Trying SQL fallback...")
		results = search_books_by_theme_db(user_message)  # acum returnează același format
		if not results["documents"][0]:
			return {"response": "❌ No books found in ChromaDB or SQL database."}

	gpt_reply = generate_response(user_message, results)

	# 5. Fallback dacă GPT nu a generat nimic
	if not gpt_reply:
		return {"response": "❌ I couldn't generate a response. Please try again."}

	return {"response": gpt_reply}