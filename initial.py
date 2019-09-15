import pyttsx3
import speech_recognition as sr

##File import
from speechToText import speechToText
import helper

engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def getDigit():
    res = speechToText(recognizer, microphone)
    if(helper.checkResponse(res)):
        #Split text by space and take letters
        print(res["text"])
        arr = res["text"].strip().lower().split()
        for word in arr:
            num = helper.getNumber(word.strip())
            if(isinstance(num, int)):
                # engine.say(num)
                # engine.runAndWait()
                return num
            
    return ""
  
def getBatteries():
    res = speechToText(recognizer, microphone)
    if(helper.checkResponse(res)):
        #Split text by space and get the number
        arr = res["text"].strip().lower().split()
        for word in arr:
            num = helper.getNumber(word.strip())
            print(word, "  ", num)
            print(isinstance(num, int))
            if(isinstance(num, int)):
                # engine.say("Got " + str(num))
                return num
    return 100    

def getTruthValue():
    confirm = helper.checkConfirm()
    if(confirm):
        return True
    elif(not confirm):
        return False
    return ""   

#Get the items that are wrong
def getWrongItems():
    items = []
    res = speechToText(recognizer, microphone)
    if(helper.checkResponse(res)):
        #Split text by space and take letters
        print("Wrong items " + res["text"])
        arr = res["text"].strip().lower().split()
        for word in arr:
            if(word == "digit"):
                items.append("digit")
            elif(word == "vowel" or word == "vowels"):
                items.append("vowel")
            elif(word == "battery" or word == "batteries"):
                items.append("batteries")
            elif(word == "frk"):
                items.append("FRK")
            elif(word == "car"):
                items.append("CAR")
            elif(word == "indicator" or word == "indicators"):
                items.append("indicators")
            elif(word == "port" or word == "parallel"):
                items.append("port")
    return items

def getInitial():
    engine = pyttsx3.init()
    complete = False
    batteries = 100
    FRK = ""
    CAR = ""
    parallelPort = ""
    serialDigit = "" 
    serialVowel = ""
    while(not complete):
        if(serialDigit == ""):
            engine.say("Serial last digit")
            engine.runAndWait()
            serialDigit = getDigit()
        # elif(serialVowel == ""):
        #     engine.say("Serial vowel, yes or no")
        #     engine.runAndWait()
        #     serialVowel = getTruthValue()
        elif(batteries == 100):
            engine.say("How many batteries?")
            engine.runAndWait()
            batteries = getBatteries()
        # elif(FRK == ""):
        #     engine.say("Is F R K lit?") 
        #     engine.runAndWait()
        #     FRK = getTruthValue()
        # elif(CAR == ""):
        #     engine.say("Is C A R lit") 
        #     engine.runAndWait()
        #     CAR = getTruthValue()
        # elif(parallelPort == ""):
        #     engine.say("Is there a parallel port?")
        #     engine.runAndWait()
        #     parallelPort = getTruthValue()
        elif(serialVowel == "" or FRK == "" or CAR == "" or parallelPort == ""):
            question = "Answer the following with a series of yes or no. Does the bomb serial have a vowel, is there a lit FRK "
            question += "Is there a lit C A R and is there a parallel port"
            engine.setProperty("rate", 150)
            engine.say(question)
            engine.runAndWait()
            engine.setProperty("rate", 200)
            restart = True
            while(restart):
                engine.runAndWait()
                res = speechToText(recognizer, microphone)
                print(res["text"])
                if(helper.checkResponse(res)):
                    try:
                        ans = res["text"].strip().lower().split()
                        for word in ans:
                            value = ""
                            if(word in helper.confirmMessage):
                                value = True
                            elif(word in helper.denyMessage):
                                value = False
                            if(value == True or value == False):
                                if(serialVowel == ""):
                                    serialVowel = value
                                elif(FRK == ""):
                                    FRK = value
                                elif(CAR == ""):
                                    CAR = value
                                elif(parallelPort == ""):
                                    parallelPort = value
                        if not(serialVowel == "" or FRK == "" or CAR == "" or parallelPort == ""):
                            restart = False
                        else:
                            engine.say("Not all questions were answered")
                    except:
                        continue
        else:
            #Get confirmation
            msg = "Last digit " + str(serialDigit)
            msg = " Vowel " + str(serialVowel)
            msg = str(batteries) + " battery"
            msg = " FRK " + str(FRK)
            msg = " C A R" + str(CAR)
            msg = " Parallel port " + str(parallelPort)
            msg = " Is everything correct?"
            engine.say(msg)
            engine.runAndWait()
            correct = getTruthValue()
            if(correct):
                #Save variables
                helper.saveInitial(serialDigit, serialVowel, batteries, FRK, CAR, parallelPort)
                return
            else:
                engine.say("What is wrong?")
                engine.runAndWait()
                wrong = getWrongItems()
                if(len(wrong) == 0):
                    engine.say("You didn't say any of the items")
                elif("digit" in wrong):
                    serialDigit = ""
                elif("vowel" in wrong):
                    serialVowel = ""
                elif("batteries" in wrong):
                    batteries = 100
                elif("FRK" in wrong):
                    FRK = ""
                elif("CAR" in wrong):
                    CAR = ""
                elif("indicators" in wrong):
                    FRK = ""
                    CAR = ""
                elif("port" in wrong):
                    parallelPort = ""

