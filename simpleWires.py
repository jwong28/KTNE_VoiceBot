import pyttsx3
import speech_recognition as sr

##File import
from speechToText import speechToText
import helper

engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def simpleWires():
    while(True):
        engine.say("What are the colors")
        engine.runAndWait()
        res = speechToText(recognizer, microphone)
        print(res["text"])
        if(helper.checkResponse(res)):
            try:
                ans = res["text"].strip().lower().split()
                ans = getWire(ans)
                if(not len(ans) == 0):
                    print(ans)
                    engine.say(ans)
                    engine.runAndWait()
                    return
            except ValueError:
                print("Simple wires error")
                continue

###Module simple wires###
def getWire(wires):
    answer = ""
    num = len(wires)
    odd = (helper.digit%2 == 1)
    engine.say(wires)
    engine.runAndWait()

    #Colors are black 0, blue 1, red 2, white 3, yellow 4
    count = [0,0,0,0,0]
    for wire in wires:
        # print(wire)
        if(wire == "black"):
            count[0] = count[0] + 1 
        elif(wire == "blue"):
            count[1] = count[1] + 1
        elif(wire == "red"):
            count[2] = count[2] + 1
        elif(wire == "white"):
            count[3] = count[3] + 1
        elif(wire == "yellow"):
            count[4] = count[4] + 1
    # Solve wires
    if(num == 3):
        if("red" in wires):
            answer = "Second wire"
        elif(wires[2] == "white"):
            answer = "Last wire"
        elif(count[1] > 1):
             answer = "Last blue wire"
        else:
            answer = "Last wire"
    elif(num == 4):
        if(count[2] > 1 and odd):
            answer = "Last red wire"
        elif(wires[3] == "yellow" and count[2] == 0):
            answer = "First wire"
        elif(count[1] == 1):
            answer = "First wire"
        elif(count[4] > 1):
            answer = "Last wire"
        else:
            answer = "Second wire"
    elif(num == 5):
        if(wires[4] == "black" and odd):
            answer = "Fourth wire"
        elif(count[2] == 1 and count[4] > 1):
            answer = "First wire"
        elif(count[0] == 0):
            answer = "Second wire"
        else:
            answer = "First wire"
    elif(num == 6):
        if(count[4] == 0 and odd):
            answer = "Third wire"
        elif(count[4] == 1 and count[3] > 1):
            answer = "Fourth wire"
        elif(count[2] == 0):
            answer = "Last wire"
        else:
            answer = "Fourth wire"
    return answer