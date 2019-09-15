import pyttsx3
import speech_recognition as sr

##File import
from speechToText import speechToText
import helper

engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Array of the greek letters
balloon = ["balloon", "circle", "line", "racket"]                           #1 a
at = ["a", "t", "arrowhead", "upside", "v", "pyramid"]                      #2 b
llamda = ["lambda", "llamda", "slide",  "x", "upside", "y"]                           #3 c
n = ["lighting","thunder", "n", "weird", "squiggly"]                        #4 d
hym = ["h", "y", "m", "alien", "spaceship", "triangle", "e", "line"]        #5 e
h = ["h", "cursive", "hook"]                                                #6 f
cBackwards = ["backwards", "c", "dot", "middle"]                            #7 g
e = ["backwards", "e", "dots", "two", "top"]                                #8 h
q = ["q", "o", "curve", "loop", "curly"]                                                     #9 i
star = ["white","star"]                                                             #10 j
question = ["question", "upside"]                                           #11 k
copy = ["copyright", "symbol", "circle", "c"]                               #12 l
nose = ["nose", "w", "apostrophe" ]                                         #13 m 
k = ["k", "backwards", "butterfly", "i"]                                    #14 n
wand = ["wand", "hook", "broken", "three"]                                  #15 o
six = ["flat", "six", "6"]                                                       #16 p
p = ["p", "paragraph", "symbol"]                                            #17 q
tb = ["t", "b", "backwards", "d"]                                           #18 r 
smile = ["smile", "smiley", "tonue", ":-)"]                                        #19 s
trident = ["trident", "fork", "spear"]                                      #20 t
c = ["c", "dot", "middle", "see", "sea"]                                                  #21 u
three = ["three", "squiggly", "antennae", "caterpillar", "3"]                    #22 v
blackstar = ["star", "black"]                                               #23 w
nEqual = ["equal", "not", "diagonal", "line"]                               #24 x
ae = ["a", "e"]                                                             #25 y
nu = ["n", "u"]                                                             #26 z 
omega = ["omega", "squid", "upside", "horshoe", "octopus", "ohms", "god"]          #27 aa

# The columns
col1 = [1, 2, 3, 4, 5, 6, 7]
col2 = [8, 1, 7, 9, 10, 6, 11]
col3 = [12, 13, 9, 14, 15, 3, 10]
col4 = [16, 17, 18, 5, 14, 11, 19]
col5 = [20, 19, 18, 21, 17, 22, 23]
col6 = [16, 8, 24, 25, 20, 26, 27]

# Symbols
symbol1 = 0
symbol2 = 0
symbol3 = 0
symbol4 = 0

def greekLetters():
    getSymbols()
    getAnswer()
    

def getSymbols():
    global symbol1, symbol2, symbol3, symbol4
    num = 1
    # x = "llamda"
    while(True):
        engine.say("Symbol "+ str(num))
        engine.runAndWait()
        res = speechToText(recognizer, microphone)
        print(res["text"])
        if(helper.checkResponse(res)):
        # if(1 == 1):
            try:
                # ans = x.strip().lower().split()
                ans = res["text"].strip().lower().split()
                case = findSymbolNum(ans)
                if not(case == 0):
                    if(symbol1 == 0):
                        symbol1 = case
                        num = num + 1
                        # x = "circle with line on the bottom"
                    elif(symbol2 == 0):
                        symbol2 = case
                        num = num + 1
                        # x = "backwards c with a dot"
                    elif(symbol3 == 0):
                        symbol3 = case
                        num = num + 1
                        # x = "a cursive h"
                    elif(symbol4 == 0):
                        symbol4 = case
                        num = num + 1
                        return
            except ValueError:
                print("Greek letter error")

def findSymbolNum(words):
    results = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for word in words:
        if(word in balloon):
            results[0] += 1
        if(word in at):
            results[1] += 1
        if(word in llamda):
            results[2] += 1
        if(word in n):
            results[3] += 1
        if(word in hym):
            results[4] += 1
        if(word in h):
            results[5] += 1
        if(word in cBackwards):
            results[6] += 1
        if(word in e):
            results[7] += 1
        if(word in q):
            results[8] += 1
        if(word in star):
            results[9] += 1
        if(word in question):
            results[10] += 1
        if(word in copy):
            results[11] += 1
        if(word in nose):
            results[12] += 1
        if(word in k):
            results[13] += 1
        if(word in wand):
            results[14] += 1
        if(word in six):
            results[15] += 1
        if(word in p):
            results[16] += 1
        if(word in tb):
            results[17] += 1
        if(word in smile):
            results[18] += 1
        if(word in trident):
            results[19] += 1
        if(word in c):
            results[20] += 1
        if(word in three):
            results[21] += 1
        if(word in blackstar):
            results[22] += 1
        if(word in nEqual):
            results[23] += 1
        if(word in ae):
            results[24] += 1
        if(word in nu):
            results[25] += 1
        if(word in omega):
            results[26] += 1
    print(results)
    # Check if results have the same num
    if(max(results)== 0):
        return 0
    symbols = [i for i,d in enumerate(results) if d == max(results)]
    if(len(symbols) == 1):
        return symbols[0] + 1
    else:
        return checkResults(symbols)

def checkResults(arr):
    engine.say("Found multiple choices")
    for num in arr:
        question = "Does the symbol look like a" + getPhrase(num)
        engine.say(question)
        engine.runAndWait()
        confirm = helper.checkConfirm()
        if(confirm):
            return num + 1
    return 0

def getPhrase(arg):
    switcher = {
        0: "circle and a vertical line directly under it",
        1: "small t in a tent",
        2: "high heel with a dash at the top",
        3: "tilted n with 2 small curves at the end",
        4: "have a triangle and sideways e with 2 lines on the left",
        5: "cursive h with a hook on the bottom right",
        6: "backwards c with a dot in the middle",
        7: "backwards e with two dots on top",
        8: "roller coaster loop",
        9: "white star",
        10: "upside down question mark",
        11: "copyright symbol",
        12: "nose with a curve and apostrophe on top",
        13: "letter I with a k popping out on both sides",
        14: "three quarter circle connected to a squiggly line on the bottom",
        15: "six with a flat top",
        16: "paragraph symbol",
        17: "letter t crossed with a letter b",
        18: "smiley face with a tongue",
        19: "trident",
        20: "c with a dot in the middle",
        21: "number 3 with antennas and a curve at the bottom",
        22: "black star",
        23: "not equal sign",
        24: "letter a and e combined",
        25: "capital n with the letter u on top",
        26: "omega sign or upside down horshoe",
    }
    return switcher.get(arg)

def getAnswer():
    if(symbol1 in col1 and symbol2 in col1 and symbol3 in col1 and symbol4 in col1):
        sortIn(col1)
    elif(symbol1 in  col2 and symbol2 in  col2 and symbol3 in  col2 and symbol4 in  col2):
        sortIn(col2)
    elif(symbol1 in col3 and symbol2 in col3 and symbol3 in col3 and symbol4 in col3):
        sortIn(col3)
    elif(symbol1 in  col4 and symbol2 in col4 and symbol3 in col4 and symbol4 in col4):
        sortIn(col4)
    elif(symbol1 in col5 and symbol2 in col5 and symbol3 in col5 and symbol4 in col5):
        sortIn(col5)
    elif(symbol1 in col6 and symbol2 in col6 and symbol3 in col6 and symbol4 in col6):
        sortIn(col6)

def sortIn(col):
    i1 = col.index(symbol1)
    i2 = col.index(symbol2)
    i3 = col.index(symbol3)
    i4 = col.index(symbol4)
    index = [i1, i2, i3, i4]
    index.sort()
    result = "click "
    for i in index:
        if(i == i1):
            result += getPhrase(symbol1 - 1)
        elif(i == i2):
            result += getPhrase(symbol2 - 1)
        elif(i == i3):
            result += getPhrase(symbol3 - 1)
        elif(i == i4):
            result += getPhrase(symbol4 - 1)
        if not(i == i4):
            result += " click "
    print(result)
    engine.setProperty('rate', 150)
    engine.say(result)
    engine.runAndWait()