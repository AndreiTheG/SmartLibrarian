from fastapi import APIRouter
from backend.model.ChatRequest import ChatRequest
from backend.chatbot.censored_lang_filter import is_inappropiate
from backend.chatbot.text_generator import generate_response, generate_response_from_db
from backend.retriever.search import get_summary_by_title_from_db, search_books_by_theme, search_books_by_theme_db

router = APIRouter()

conversation_history = []

@router.post("/chat")
def chat(request: ChatRequest):
	user_message = request.message.strip()

	# 1. Exit command (opțional)
	if user_message.lower() in {"exit", "quit"}:
		return {"response": "👋 Goodbye!"}

	# 2. Inadequate language filter
	if is_inappropiate(user_message):
		return { "response": "🚫 Please use appropriate language. I'm here to help you with book recommendations." }

	# 3. Explicit command for the summary
	if user_message.lower().startswith("show me the summary for"):
		title = user_message[len("show me the summary for"):].strip()
		summary = get_summary_by_title_from_db(title)
		return {"response": summary}

	# 4. Chat semantic + GPT (RAG)
	results = search_books_by_theme(user_message)
	if not results["documents"][0]:
		print("⚠️ Nothing found in ChromaDB. Trying SQL fallback...")
		results = search_books_by_theme_db(user_message)
		if not results["documents"][0]:
			return {"response": "❌ No books found in ChromaDB or SQL database."}

	# Verify the source: Chroma or fallback SQL
	if "documents" in results and results["documents"][0]:
		gpt_reply = generate_response(user_message, results, conversation_history[-10:])
	else:
		gpt_reply = generate_response_from_db(user_message, results, conversation_history[-10:])

	# 5. Fallback if GPT didn't generate anything
	if not gpt_reply:
		return {"response": "❌ I couldn't generate a response. Please try again."}

	conversation_history.append({"role": "user", "content": user_message})
	conversation_history.append({"role": "assistant", "content": gpt_reply})

	return {"response": gpt_reply}