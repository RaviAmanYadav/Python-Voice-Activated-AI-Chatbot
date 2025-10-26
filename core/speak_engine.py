import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0=Male, 1=Female
engine.setProperty('rate', 170)

def speak(audio):
    """Convert text to speech."""
    print(f"🤖 Bot: {audio}")
    engine.say(audio)
    engine.runAndWait()
