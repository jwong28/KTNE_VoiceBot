import pyttsx3
import speech_recognition as sr

from speechToText import speechToText

recognizer = sr.Recognizer()
microphone = sr.Microphone()
engine = pyttsx3.init()

numWord = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
confirmMessage = ["yes", "yea", "yeah", "yep", "ok", "okay", "confirm", "check"]
denyMessage = ["no", "nope", "nothing"]
done = ["finished", "finish", "complete", "next", "done", "ok", "okay", "alright", "confirm", "then", "than"]

#gloabl variables
digit = ""
vowel = ""
frk = ""
car = ""
batteries = 10
parallel = ""

def checkConfirm():
    global confirmMessage, denyMessage
    complete = False
    while(not complete):
        try:
            confirm = speechToText(recognizer, microphone)
            print("Confirm msg: "+ confirm["text"])
            arr = confirm["text"].strip().lower().split()
            for word in arr:
                if(word in confirmMessage):
                    return True
                elif(word in denyMessage):
                    return False
        except:
            engine.say("Please repeat")
            engine.runAndWait()

def checkDone(res):
    if(res["text"].strip().lower() == "done"):
        return True

def checkResponse(res):
    global engine
    if (not(res["success"]) or res["error"] or res["text"] is None):
        print("Error is : "+ res["error"])
        engine.say("Error, please repeat")
        engine.runAndWait()
        return False
    else:
        return True

def getNumber(word):
    global numWord
    if(word == "to" or word == "too"):
        return 2
    elif(word == "for" or word == "fore"):
        return 4
    elif(isinstance(word, int)):
        return word
    elif(word.isnumeric()):
        print(int(word))
        return int(word)
    elif(word in numWord):
        return numWord.index(word)
    return ""

def saveInitial(serialDigit, serialVowel, battery, indicatorOne, indicatorTwo, parallelPort):
    global digit, vowel, batteries, frk, car, parallel
    digit = serialDigit
    vowel = serialVowel
    batteries = int(battery)
    frk = indicatorOne
    car = indicatorTwo
    parallel = parallelPort
