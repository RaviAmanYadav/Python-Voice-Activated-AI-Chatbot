import webbrowser
import datetime
import wikipedia
import os
from core.speak_engine import speak

def handleCommand(query):
    """Perform action based on user's voice command."""
    
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)

    elif 'open google' in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

    elif 'shutdown' in query:
        speak("Shutting down the system. Bye!")
        os.system("shutdown /s /t 5")

    elif 'restart' in query:
        speak("Restarting the system.")
        os.system("shutdown /r /t 5")

    else:
        speak("Sorry, I didn't understand that.")
