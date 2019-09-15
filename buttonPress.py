import pyttsx3
import speech_recognition as sr

##File import
from speechToText import speechToText
import helper

engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def buttonPress():
    while(True):
        engine.say("Button color and text")
        engine.runAndWait()
        color = ""
        text = ""
        res = speechToText(recognizer, microphone)
        print(res["text"])
        if(helper.checkResponse(res)):
            try:
                ans = res["text"].strip().lower().split()
                # Get color
                if("blue" in ans):
                    color = "blue"
                    engine.say("blue")
                elif("red" in ans):
                    color = "red"
                    engine.say("red")
                elif("white" in ans):
                    color = "white"
                    engine.say("white")
                elif("yellow" in ans):
                    color = "yellow"
                    engine.say("yellow")
                # Get text
                if("hold" in ans):
                    text = "hold"
                    engine.say("hold")
                elif("detonate" in ans):
                    text = "detonate"
                    engine.say("detonate")
                elif("abort" in ans):
                    text = "abort"
                    engine.say("abort")
                elif("press" in ans):
                    text = "press"
                    engine.say("press")
                getResult(color, text)
                if(not ans == ""):
                    return
            except ValueError:
                print("Button press error")
                continue

def getResult(color, text):
    if(color == "blue" and text == "abort"):
        holdButton()
    elif(helper.batteries > 1 and text == "detonate"):
        release()
    elif(color == "white" and helper.car):
        holdButton()
    elif(helper.batteries > 2 and helper.frk):
        release()
    elif(color == "yellow"):
        holdButton()
    elif(color == "red" and text == "hold"):
        release()
    else:
        holdButton()

def holdButton():
    engine.say("Hold the button, what's the color strip")
    engine.runAndWait()
    while(True):
        res = speechToText(recognizer, microphone)
        print(res["text"])
        if(helper.checkResponse(res)):
            try:
                ans = res["text"].strip().lower().split()
                if("blue" in ans):
                    engine.say("Release when 4 in any position")
                    engine.runAndWait()
                    return
                elif("white" in ans):
                    engine.say("Release when 1 in any position")
                    engine.runAndWait()
                    return
                elif("yellow" in ans):
                    engine.say("Release when 5 in any position")
                    engine.runAndWait()
                    return
                elif("red" in ans or "orange" in ans or "black" in ans):
                    engine.say("Release when 1 in any position")
                    engine.runAndWait()
                    return
                else:
                    engine.say("Whats the color?")
                    engine.runAndWait()
            except:
                continue

def release():
    engine.say("Press and immediately release")
    engine.runAndWait()
    return