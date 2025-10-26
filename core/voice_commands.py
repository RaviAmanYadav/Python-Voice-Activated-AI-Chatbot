import speech_recognition as sr

def takeCommand():
    """Capture voice input and return as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("🧠 Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"🗣️ You said: {query}\n")
    except sr.UnknownValueError:
        print("❌ Couldn't understand, please say that again.")
        return "None"
    except sr.RequestError:
        print("⚠️ Internet error. Check your connection.")
        return "None"

    return query.lower()
