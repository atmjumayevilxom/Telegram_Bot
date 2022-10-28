
import pyttsx3
engine = pyttsx3.init()
text=input("Text andoz = ")
engine.say("{}".format(text))
engine.runAndWait()