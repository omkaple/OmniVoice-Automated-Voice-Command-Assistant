import speech_recognition as sr
import pyttsx3
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys


recognizer = sr.Recognizer()

def speaktheword(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processCommand(c):
    speaktheword("You said " + c)
    if c.lower()=="open google":
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open  you tube" in c.lower():
        webbrowser.open("https://www.youtube.com/")

def processCommand2(c):
      if "stop" in c.lower():
        speaktheword("Going to rest mode")
        return False

      elif "play " in c.lower():
        song = c.lower().replace("play", "").strip()

        if song == "":
            speaktheword("Tell me the song name")
            return True

        speaktheword("Playing " + song)

        driver = webdriver.Chrome()   # make sure chromedriver is installed
        driver.get("https://www.youtube.com")

        time.sleep(2)

        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys(song)
        search_box.send_keys(Keys.RETURN)

        time.sleep(3)

        # Click first video
        video = driver.find_element(By.ID, "video-title")
        video.click()

        return True
      

      else:
        speaktheword("You said " + c)
        return True

if __name__ == "__main__":
    speaktheword("Your personal assistance is ready gave me a command")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio)
            print("You said:", command)

            if command.lower() == "open browser":
                speaktheword("ready to open")

                while True:
                  try:
                  

                      with sr.Microphone() as source:
                        print("Speak your command...")
                        audio = recognizer.listen(source)

                      command = recognizer.recognize_google(audio)
                      processCommand(command)

                      if command.lower() == "exit the browser":
                        print("Exitfrom the browser ")
                        speaktheword("exit")
                        break
                      
                      elif command.lower()=="stop":
                         print("Stopping completely")
                         speaktheword("your assitance is going to rest mode")
                         sys.exit()



                  except Exception:
                      continue
            elif command.lower()=="play something":
                speaktheword("open the you tube , told me the song i will play for you")
                while True:
                  try:
                  

                      with sr.Microphone() as source:
                        print("Speak your command...")
                        audio = recognizer.listen(source)

                      command = recognizer.recognize_google(audio)
                      processCommand2(command)

                      if command.lower() == "exit":
                        print("exit from the play ")
                        speaktheword("stop playing song")
                        break
                      
                      elif command.lower()=="stop":
                         print("Stopping completely")
                         speaktheword("your assistance is going to rest mode ")
                         sys.exit()



                  except Exception:
                      continue
            elif command.lower()=="stop":
                    print("Stopping completely")
                    speaktheword("your assistance is going to rest mode ")
                    sys.exit() 

        except Exception as e:
            print("Error:", e)
