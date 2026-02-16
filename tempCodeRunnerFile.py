import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

def speaktheword(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processCommand(c):
    if "stop" in c.lower():
        speaktheword("Going to rest mode")
        return False   # signal to stop loop
    else:
        speaktheword("You said " + c)
        return True

if __name__ == "__main__":
    
    speaktheword("Ram Ram Om")

    running = True

    while running:
        try:
            with sr.Microphone() as source:
                print("Listening .....")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)

            print("Recognizing.....")
            command = recognizer.recognize_google(audio)
            print("You said:", command)

            if command.lower() == "jarvis":
                speaktheword("Activated")

                with sr.Microphone() as source:
                    print("Speak your command...")
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print("Command:", command)

                running = processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Error ; {0}".format(e))
