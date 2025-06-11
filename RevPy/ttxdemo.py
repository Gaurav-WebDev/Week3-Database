import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def speak(msg):
    engine.say(msg)
    engine.runAndWait()


while True:
    userText = input("Enter your message ( type 'exit' for stop):")
    if 'exit' in userText :
        speak("Ok Bye")
        break
    else :
        speak(userText)