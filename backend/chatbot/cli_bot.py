from ..retriever.search import search_books_by_theme, get_summary_by_title
from ..chatbot.censored_lang_filter import is_inappropiate
from  ..chatbot.text_generator import generate_response
from  ..voice.speech_to_text import listen_to_user
from  ..voice.text_to_speech import speak_text
from ..embedding.load_db_to_chroma import collection

# Choose a communication option with Chatbot
def show_menu():
    print("\n=== Smart Librarian Menu ===")
    print("1. Text → Text")
    print("2. Text → Audio")
    print("3. Voice → Text")
    print("0. Exit")

# The CLI modes to communicate with Chatbot while is running
def run_chatbot_cli_modes():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("👋 Goodbye!")
            break

        elif choice == "1":
            user_input = input("💬 You: ")
            print(collection.count())
            if is_inappropiate(user_input):
                print("Assistant: Please use an adequate language. I'm here to help you with book recommendations.")
                continue

            if user_input.lower().startswith("show me the summary for"):
                title = user_input[len("show me the summary for"):].strip()
                reply = get_summary_by_title(title)
            else:
                results = search_books_by_theme(user_input)
                reply = generate_response(user_input, results)
            print(f"🤖 Assistant: {reply}")

        elif choice == "2":
            user_input = input("💬 You: ")
            if not user_input.strip():
                print("⚠️ No valid input provided.")
                continue
            results = search_books_by_theme(user_input)
            reply = generate_response(user_input, results)
            print(f"🔊 Assistant: {reply}")
            speak_text(reply)

        elif choice == "3":
            user_input = listen_to_user()
            if not user_input.strip():
                print("⚠️ No speech detected. Try again.")
                continue
            print(f"📝 Transcribed: {user_input}")
            results = search_books_by_theme(user_input)
            reply = generate_response(user_input, results)
            print(f"🤖 Assistant: {reply}")

        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    run_chatbot_cli_modes()