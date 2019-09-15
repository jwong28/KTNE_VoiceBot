import pyttsx3
import speech_recognition as sr

##File import
from speechToText import speechToText
import helper

engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

colorInput = []
results = []

def simonSays():
    strikes = checkStrikes()
    phase = 1
    while(True):
        engine.say("Color "+ str(phase))
        engine.runAndWait()
        res = speechToText(recognizer, microphone)
        print(res["text"])
        if(helper.checkResponse(res)):
            try:
                ans = res["text"].strip().lower().split()
                done = getColors(strikes, ans)
                if(done == "done"):
                    return
                elif(done == "next"):
                    phase = phase + 1
            except ValueError:
                print("Simon says error")
    return
    
def checkStrikes():
    while(True):
        engine.say("Any strikes?")
        engine.runAndWait()
        strikes = speechToText(recognizer, microphone)
        print(strikes["text"])
        ans = strikes["text"].strip().lower().split()
        for word in ans:
            print(word)
            if(word in helper.denyMessage or word == 0):
                return 0
            else:
                numWord = helper.getNumber(word)
                if(numWord == 1):
                    return 1
                elif(numWord == 2):
                    return 2

#Using the table, and what use says, return
def getColors(strikes, ans):
    inColor = ""
    outColor = ""
    for word in ans:
        #Check if done has been called, if so return
        if(word in helper.done):
            return "done"
        # If vowel exists
        if(helper.vowel):
            if(word == "red"):
                inColor = "red"
                if(strikes == 0):
                    outColor = "blue"
                elif(strikes == 1):
                    outColor = "yellow"
                elif(strikes == 2):
                    outColor = "green"
            elif(word == "blue"):
                inColor = "blue"
                if(strikes == 0):
                    outColor = "red"
                elif(strikes == 1):
                    outColor = "green"
                elif(strikes == 2):
                    outColor = "red"
            elif(word == "green"):
                inColor = "green"
                if(strikes == 0):
                    outColor = "yellow"
                elif(strikes == 1):
                    outColor = "blue"
                elif(strikes == 2):
                    outColor = "yellow"  
            elif(word == "yellow"):
                inColor = "yellow"
                if(strikes == 0):
                    outColor = "green"
                elif(strikes == 1):
                    outColor = "red"
                elif(strikes == 2):
                    outColor = "blue" 
        # If vowel DNE
        else:
            if(word == "red"):
                inColor = "red"
                if(strikes == 0):
                    outColor = "blue"
                elif(strikes == 1):
                    outColor = "red"
                elif(strikes == 2):
                    outColor = "yellow"
            elif(word == "blue"):
                inColor = "blue"
                if(strikes == 0):
                    outColor = "yellow"
                elif(strikes == 1):
                    outColor = "blue"
                elif(strikes == 2):
                    outColor = "green"
            elif(word == "green"):
                inColor = "green"
                if(strikes == 0):
                    outColor = "green"
                elif(strikes == 1):
                    outColor = "yellow"
                elif(strikes == 2):
                    outColor = "blue"  
            elif(word == "yellow"):
                inColor = "yellow"
                if(strikes == 0):
                    outColor = "red"
                elif(strikes == 1):
                    outColor = "green"
                elif(strikes == 2):
                    outColor = "red"
        # If there was a color detected 
        if(not inColor == ""):
            colorInput.append(inColor)
            results.append(outColor)
            engine.say(colorInput)
            engine.say("Press")
            engine.say(results)
            engine.runAndWait()
            return "next"
    return ""

                