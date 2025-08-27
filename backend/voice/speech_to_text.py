import speech_recognition as sr

def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        try:
            audio = recognizer.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("⚠️ Listening timed out. No speech detected.")
            return ""

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"❌ Speech Recognition error: {e}")
        return ""