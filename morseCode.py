import pyttsx3
import speech_recognition as sr

##File import
from speechToText import speechToText
import helper

engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Morse
translate = ["a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n", "o", 
    "p", "q", "r", "s", "t", "u", "v", "w",
    "x", "y", "z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Letters
letters = ["dot dash", "dash dot dot dot", "dash dot dash dot", "dash dot dot", "dot",
    "dot dot dash dot", "dash dash dot", "dot dot dot dot",
    "dot dot", "dot dash dash dash", "dash dot dash", "dot dash dot dot",
    "dash dash", "dash dot", "dash dash dash", "dot dash dash dot",
    "dash dash dot dash", "dot dash dot", "dot dot dot", "dash", "dot dot dash",
    "dot dot dot dash", "dot dash dash", "dash dot dot dash", "dash dot dash dash", "dash dash dot dot",
    "dash dash dash dash dash", "dot dash dash dash dash", "dot dot dash dash dash",
    "dot dot dot dash dash", "dot dot dot dot dash", "dot dot dot dot dot", "dash dot dot dot dot",
    "dash dash dot dot dot", "dash dash dash dot dot", "dash dash dash dash dot"]

words = [["shell", "3 point 5 0 5"], ["halls","3 point 5 1 5"], ["slick","3 point 5 2 2"],
    ["trick","3 point 5 2 2"], ["boxes","3 point 5 3 5"], ["leaks","3 point 5 5 2"],
    ["strobe","3 point 5 4 5"], ["bistro","3 point 5 5 2"], ["flick","3 point 5 5 5"],
    ["bombs","3 point 5 6 5"], ["break","3 point 5 7 2"], ["brick","3 point 5 7 5"],
    ["steak","3 point 5 8 2"], ["sting","3 point 5 9 2"], ["vector","3 point 5 9 5"],
    ["beats","3 point 6 0 0"]]


def morseCode():
    engine.say("Say and in betweeen dash and dot")
    while(True):
        print("Start while")
        codeWord = ""
        engine.say("Ready for code")
        engine.runAndWait()
        res = speechToText(recognizer, microphone)
        print(res["text"])
        if(helper.checkResponse(res)):
        # if(1 == 1):
            try:
                # ans = x.strip().lower().split()
                ans = res["text"].strip().lower().split()
                letter = ""
                for word in ans:           
                    if("dot" in word):
                        letter += "dot "
                    elif("dash" in word):
                        letter += "dash "
                    if("." in word):
                        letter += "dot "
                    elif("-" in word):
                        letter += "dash "
                    if("space" in word):
                        exist = findLetter(letter.strip())
                        letter = ""
                        if not(exist == ""):
                            codeWord += exist
                        #    engine.say(exist) 
                        #    return
                exist = findLetter(letter.strip())
                if not(exist == ""):
                    codeWord += exist
                code = findWord(codeWord)
                if not(code == ""):
                    engine.say(code)
                    engine.runAndWait()
                    return code
                engine.say("No word found, try again")
            except:
                continue
                        
def findLetter(letter):
    print("letter morse code is " + letter)
    print(len(letters))
    # count = 0
    # result = []
    for code in letters:
        # print(letter + " : " +code)
        if(letter == code):
            index = letters.index(code)
            print(letter + " becomes " + str(translate[index]))
            return translate[index]

def findWord(codeword):
    print("looking for " + codeword)
    result = []
    count = 0
    for word in words:
        print(codeword + " : " + word[0])
        if(codeword == word[0][:len(codeword)]):
            print("found " + word[0] + " code "+ word[1])
            count += 1
            result.append(word[1])
            if(len(result) > 1):
                return ""
    return result[0]