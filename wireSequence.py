import pyttsx3
import speech_recognition as sr

##File import
from speechToText import speechToText
import helper

engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Need to fix the detected words. If in cWord, look for a c
# If read, look for red

red = ["c", "b", "a", "a c", "b", "a c", "a b c", "a b", "b"]
blue = ["b", "a c", "b", "a", "b", "b c", "c", "a c", "a"]
black = ["a b c", "a c", "b", "a c", "b", "b c", "a b", "c", "c"]
aWord = ["a", "ey", "eggs"]
bWord = ["b", "be", "bee", "bean"]
cWord = ["see", "sea", "c"]
redIndex = 0
blueIndex = 0
blackIndex = 0
wireInput = []
wireOutput = []
index = 0

def wireSequence():
    engine.say("Say done when module is finished")
    while(True):
        engine.say("Name wires")
        engine.runAndWait()
        res = speechToText(recognizer, microphone)
        print(res["text"])
        if(helper.checkResponse(res)):
            try:
                ans = res["text"].strip().lower().split()
                print("x is now ")
                print(ans)
                wire = ""
                for word in ans:
                    if(word == "done"):
                        getOutput(wire)
                        if(ran):
                            sayOutput()
                        return
                    if(word in aWord):
                        wire += " a" 
                        print("The word is "+wire)
                        ran = getOutput(wire)
                        wire = ""
                    elif(word in bWord):
                        wire += " b" 
                        print("The word is "+wire)
                        ran = getOutput(wire)
                        wire = ""
                    elif(word in cWord):
                        wire += " c" 
                        print("The word is "+wire)
                        ran = getOutput(wire)
                        wire = ""
                    elif(word == "red" or word == "blue" or word == "black"):
                        wire += word + " "
                if(ran):
                    sayOutput()
            except ValueError:
                print("Wire sequence error")
                continue

def getOutput(word):
    global red, blue, black, redIndex, blueIndex, blackIndex, wireInput, wireOutput
    wireIn = ""
    wireOut = ""
    if("red" in word or "read" in word):
        wireIn = "red "
        word = word.replace("a" , "")
        print("indexing")
        print(red[redIndex])
        for letter in red[redIndex]:
            if(letter in word and not(letter == " ")):
                wireOut = "cut"
        if(wireOut == ""):
            wireOut = "don't cut"
        redIndex += 1
        print("red num is now " + str(redIndex+1))
    elif("blue" in word):
        wireIn = "blue "
        word = word.replace("blue" , "")
        print("indexing")
        print(blue[blueIndex])
        for letter in blue[blueIndex]:
            if(letter in word and not(letter == " ")):
                wireOut = "cut"
                print(word + " " + letter + " letter")
        if(wireOut == ""):
            wireOut = "don't cut"
        blueIndex += 1
        print("blue num is now " + str(blueIndex+1))
    elif("black" in word):
        wireIn = "black "
        word = word.replace("black" , "")
        print("indexing")
        print(black[blackIndex])
        for letter in blue[blueIndex]:
            if(letter in word and not(letter == " ")):
                wireOut = "cut"
        if(wireOut == ""):
            wireOut = "don't cut"
        blackIndex += 1
        print("black num is now " + str(blackIndex+1))
    else:
        return False
    if(word in aWord):
        wireIn = wireIn + "to a"
    elif(word in bWord):
        wireIn = wireIn + "to b"
    elif(word in cWord):
        wireIn = wireIn + "to c"
    wireInput.append(wireIn)
    wireOutput.append(wireOut)
    print(wireInput)
    print(wireOutput)
    return True
     
def sayOutput():
    result = ""
    global index, wireOutput, wireInput
    for x in range(len(wireInput)):
        result = result + wireInput[x] + " " + wireOutput[x] + " "
    wireInput.clear()
    wireOutput.clear()
    engine.setProperty('rate', 150)
    engine.say(result)
    engine.runAndWait()

if __name__ == "__main__":
    wireSequence()