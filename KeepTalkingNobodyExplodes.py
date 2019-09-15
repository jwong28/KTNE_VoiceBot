import speech_recognition as sr
import pyttsx3
from gtts import gTTS 
import os
from datetime import datetime


##File import
from speechToText import speechToText
import helper
import initial

##Modules
from buttonPress import buttonPress
from complicatedWires import complicatedWires
from greekLetters import greekLetters
from mazes import mazes
from morseCode import morseCode
from numberDisplay import numberDisplay
from password import password
from simonSays import simonSays
from simpleWires import simpleWires
from wireSequence import wireSequence
from wordDisplay import wordDisplay

# Array of module descriptions

bPress = ["button", "press", "big"]
cWires = ["complicated", "wires", "wire", "vertical"]
gLetters = ["greek", "symbols", "keypad", "symbol", "letters"]
maze = ["maze", "grid", "triangle", "mazes"]
mCode = ["morse", "code", "flashing"]
nDisplay = ["display", "number"]
pword = ["pass", "password","anagram", "letters", "letter","arrow"]
sSays = ["simon", "says", "flashing", "color"]
sWires = ["simple", "wires", "wire", "horizontal"]
wSequence = ["wires", "wire", "sequence", "abc", "123","horizontal"]
wDisplay = ["display", "word", "words"]

global ans

#Check what user says and sends it to responding function
def checkModule(phrase):
    print("In check module" + phrase)
    text = phrase.strip().lower().split()
    print(text)
    results = [0,0,0,0,0,0,0,0,0,0,0]
    for word in text:
        print(word)
        if (word in bPress):
            results[0] += 1
        if(word in cWires):
            results[1] += 1
        if(word in gLetters):
            results[2] += 1
        if(word in maze):
            results[3] += 1
        if(word in mCode):
            results[4] += 1
        if(word in nDisplay):
            results[5] += 1
        if(word in pword):
            results[6] += 1
        if(word in sSays):
            results[7] += 1
        if(word in sWires):
            results[8] += 1
        if(word in wSequence):
            results[9] += 1
        if(word in wDisplay):
            results[10] += 1
    # Check if results have the same num
    if(max(results)== 0):
        return 0
    maxNum = [i for i,d in enumerate(results) if d == max(results)]
    print(results)
    if(len(maxNum) == 1):
        runModule(maxNum[0] + 1)
    else:
        for i in maxNum:
            if(i == 0):
                engine.say("Does it look like a big colored button with a word")
            elif(i == 1):
                engine.say("Do you see vertical wires")
            elif(i == 2):
                engine.say("Do you see 4 weird symbols")
            elif(i == 3):
                engine.say("Do you see a six by six grid with 2 circles")
            elif(i == 4):
                engine.say("Do you see an orange flashing light with a button that say tx")
            elif(i == 5):
                engine.say("Do you see a number in a display with 4 buttons under it")
            elif(i == 6):
                engine.say("Do you see 6 letters with arrows on the top and bottom")
            elif(i == 7):
                engine.say("Do you see a red blue green and yellow button")
            elif(i == 8):
                engine.say("Do you see 3 to 6 horizontal wires")
            elif(i == 9):
                engine.say("Do you see horizontal wires and a b c 1 2 3")
            elif(i == 10):
                engine.say("Do you see a word in display with six buttons under")
            engine.runAndWait()
            confirm = helper.checkConfirm()
            if(confirm):
                runModule(i + 1)
                return
    # if("button press" in text):
    #     buttonPress()
    # elif("complicated " in text):
    #     complicatedWires()
    # elif("greek" in text):
    #     greekLetters()
    # elif("maze" in text):
    #     mazes()
    # elif("morse" in text):
    #     morseCode()
    # elif("number" in text):
    #     numberDisplay
    # elif("password" in text):
    #     password()
    # elif("simon" in text):
    #     simonSays()
    # elif("simple" in text):
    #     simpleWires()
    # elif("sequence" in text):
    #     wireSequence()
    # elif("word" in text):
    #     wordDisplay()

def runModule(i):
    if(i == 1):
        print("To button press")
        buttonPress()
    elif(i == 2):
        print("To complicated wires")
        complicatedWires()
    elif(i == 3):
        print("To greek letters")
        greekLetters()
    elif(i == 4):
        print("To mazes")
        mazes()
    elif(i == 5):
        morseCode()
        print("To morse code")
    elif(i == 6):
        print("To number display")
        numberDisplay()
    elif(i == 7):
        password()
        print("To password")
    elif(i == 8):
        simonSays()
        print("To simon says")
    elif(i == 9):
        simpleWires()
        print("To simple wires")
    elif(i == 10):
        wireSequence()
        print("To wire sequcne")
    elif(i == 11):
        wordDisplay()
        print("To word display")



if __name__ == "__main__":
    start = datetime.now()
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    engine = pyttsx3.init()
    
    engine.say("Please wait 1 to 2 seconds after I talk to adjust for noise")
    initial.getInitial()
    engine.say("Initialized")
    engine.runAndWait()
    
    while(True):
        engine.say("Module name")
        engine.runAndWait()
        res = speechToText(recognizer, microphone)
        if (helper.checkResponse(res)):
            print("Module " + res["text"])
            checkModule(res["text"])

    #For mic testing
    # while True:
    #     res = speechToText(recognizer, microphone)
    #     if(helper.checkResponse(res)):
    #         print(res["text"])

        
  

