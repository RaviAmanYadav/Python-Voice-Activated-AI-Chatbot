from core.voice_commands import takeCommand
from core.speak_engine import speak
from core.greetings import wishMe
from core.command_handler import handleCommand

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if query == "none":
            continue
        elif "exit" in query or "quit" in query:
            speak("Goodbye Aman! Have a great day!")
            break
        else:
            handleCommand(query)
