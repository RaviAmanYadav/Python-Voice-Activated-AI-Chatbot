from core.speak_engine import speak

def writeNote():
    speak("What should I write, Aman?")
    note = input("Type or speak your note: ")
    with open("data/notes.txt", "a") as f:
        f.write(f"{note}\n")
    speak("Your note has been saved.")

def showNotes():
    speak("Here are your notes:")
    with open("data/notes.txt", "r") as f:
        print(f.read())
