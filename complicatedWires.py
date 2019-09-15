import pyttsx3
import speech_recognition as sr

##File import
from speechToText import speechToText
import helper

engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# 1 = c, 2 = d, 3 = s, 4 = p, 5 = b
# c = cut, d = don't cut, s = cut if digit is even, p = cut if parallel, b = cut if > 2 batteries
# w = white, r = red, b = blue, s = star, l = led
# white = [wr, wb, ws, wl, wsl, wrs, wrl, wbs, wbl ]
# red = [r, rb, rs, rl, rsl, rbs, rbl, rbsl]
# blue = [b, bs, bl, bsl]

arrInput = []
output = []

def complicatedWires():
    while(True):
        engine.say("Name wires")
        engine.runAndWait()
        res = speechToText(recognizer, microphone)
        print(res["text"])
        if(helper.checkResponse(res)):
            try:
                ans = res["text"].strip().lower().split()
                wire = ""
                for word in ans:
                    if(word in helper.done):
                        appendWire(wire)
                        wire = ""
                    elif(ans.index(word) == len(ans)-1):
                        wire = wire + word + " "
                        appendWire(wire)
                        wire = ""
                    else:
                        wire = wire + word + " "
                sayOutput()
                return
            except ValueError:
                print("Complicated wires error")
                continue

def appendWire(wire):
    print(wire)
    wireInput = ""
    wireOutput = ""
    if("red" in wire):
        wireInput = "red "
        if("blue" in wire):
            wireInput = wireInput + " blue"
            if("led" in wire or "light" in wire):
                wireInput = wireInput + " light"
                if("star" in wire):
                    # rbls
                    wireInput = wireInput + " star"
                    wireOutput = 2
                else:
                    # rbl
                    wireOutput = 3
            elif("star" in wire):
                # rbs
                wireInput = wireInput + "star"
                wireOutput = 4 
            else:
                # rb
                wireOutput = 3
        elif("led" in wire or "light" in wire):
            wireInput = wireInput + " light"
            if("star" in wire):
                # rls
                wireInput = wireInput + " star"
                wireOutput = 5
            else:
                # rl
                wireOutput = 5
        elif("star" in wire):
            # rs
            wireInput = wireInput + "star"
            wireOutput = 1
        else:
            # r
            wireOutput = 3
    elif("blue" in wire):
        wireInput = "blue"
        if("led" in wire or "light" in wire):
                wireInput = wireInput + " light"
                if("star" in wire):
                    # bls
                    wireInput = wireInput + " star"
                    wireOutput = 4
                else:
                    # bl
                    wireOutput = 4
        elif("star" in wire):
            #bs
            wireInput = wireInput + " star"
            wireOutput = 2
    elif("white" in wire):
        wireInput = "white"
        if("led" in wire or "light" in wire):
            wireInput = wireInput + " light"
            if("star" in wire):
                # wls
                wireInput = wireInput + " star"
                wireOutput = 5
            else:
                # wl
                wireOutput = 2
        elif("star" in wire):
            # ws
            wireInput = wireInput + " star"
            wireOutput = 1
        else:
            # w
            wireOutput = 1
    if("white" in wire and not "white" in wireInput):
        wireInput = wireInput + " white"
    arrInput.append(wireInput)
    output.append(wireOutput)

def sayOutput():
    result = ""
    for i in range(len(arrInput)):
        cut = output[i]
        if(cut == 1):
            cut = True
        elif(cut == 2):
            cut = False
        elif(cut == 3):
            if(helper.digit % 2 == 0):
                cut = True
            else:
                cut = False
        elif(cut == 4):
            if(helper.parallel):
                cut = True
            else:
                cut = False
        else:
            if(helper.batteries > 2):
                cut = True
            else:
                cut = False
        result = result + arrInput[i] + cutText(cut)
    print(result)
    engine.setProperty('rate', 100)
    engine.say(result)
    engine.runAndWait()
    engine.setProperty('rate', 200)

def cutText(cut):
    if(cut):
        return " cut "
    else:
        return " don't cut "
        
