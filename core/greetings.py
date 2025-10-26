import datetime
from core.speak_engine import speak

def wishMe():
    """Greet user based on time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Aman!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Aman!")
    else:
        speak("Good Evening Aman!")
    speak("I am your Voice Assistant. How can I help you today?")
