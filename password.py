import pyttsx3
import speech_recognition as sr

##File import
from speechToText import speechToText
import helper

engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

passwords = ["about", "after", "again", "below", "could",
"every", "first", "found", "great", "house",
"large", "learn", "never", "other", "place",
"plant", "point", "right", "small", "sound",
"spell", "still", "study", "their", "there",
"these", "thing", "think", "three", "water",
"where", "which", "world", "would", "write"]

columns = []

def password():
    while(True):
        getColumn(len(columns)+1)
        word = findWord()
        if(word == ""):
            engine.say("Needs more information")
            # print("More info")
            # print("Start while")
        elif not(word == ""):
            engine.say(word)
            engine.runAndWait()
            print(word)
            return

    


def getColumn(num):
    ans = []
    # if(num == 1):
    #     ans = ["x","z","a","i","j","r"]
    # if(num == 2):
    #     ans = ["b","f","r","g","c","j"]
    # if(num == 3):
    #     ans = ["o","t","a","g","c","j"]
    # if(num == 4):
    #     ans = ["b","f","r","u","c","j"]
    while(True):
        engine.say("Letters for column " + str(num))
        engine.runAndWait()
        res = speechToText(recognizer, microphone)
        print(res["text"])
        if(helper.checkResponse(res)):
        # if(1==1):
            try:
                col = []
                ans = res["text"].strip().lower().split()
                if(len(ans) == 6):
                    for word in ans:
                        char = word[0]
                        col.append(char)
                    engine.say(col)
                    engine.say("confirm")
                    engine.runAndWait()
                    confirm = helper.checkConfirm()
                    if(confirm):
                        columns.append(col)
                        return
                    # columns.append(col)
                    # return
            except ValueError:
                print("Password error")

def findWord():
    results = []
    print("In find word")
    print(columns)
    # Fix this its not taking the first one of each row
    # for x in range(len(columns)):
    # for x in range(len(columns)):
    #     word = ""
    #     print(str(x) + "is in column")
    #     # for y in range(len(columns[x])):
    #     for y in range(6):
    #         word = word + columns[x][y]
    #         print("the word is " + word)
    #     for w in passwords:
    #         if(word in w):
    #             print(word)
    #             results.append(word)
    #             if(len(results) > 1 or len(results) == 0):
    #                 return ""
    # return results[0]
    length = len(columns)
    letters = []
    print("The length of columsn " + str(length))
    x = 0
    print("Initial results")
    print(results)
    while (x < len(columns[0])):
        print("x inc")
        print(x)
        print(columns[0])
        letters.append(columns[0][x])
        word = letters[0]
        print(word)
        if(length == 1):
            used = False
            for w in passwords:
                if(word == w[0]):
                    results.append(w)
                    print(results)
                    used = True
                    if(len(results) > 1):
                        print("Found too many")
                        print(results)
                        return ""
            if(used == False):
                columns[0].remove(columns[0][x])
            else:
                x += 1
        elif(length > 1):
            y = 0
            while (y < len(columns[1])):
                print("y inc")
                print(columns[1])
                word = letters[0] + columns[1][y]
                letters.append(word)
                print(word)
                if(length == 2):
                    used = False
                    for w in passwords:
                        # print("The word is " + w)
                        if(word == w[:2]):
                            results.append(w)
                            print("Found " + word + " in " + w)
                            used = True
                            print(results)
                            if(len(results) > 1):
                                print("Found too many")
                                print(results)
                                return ""
                        if(word[1] == w[1]):
                            used = True
                    if(used == False):
                        columns[1].remove(columns[1][y])
                    else:
                        y += 1
                elif(length > 2):
                    z = 0
                    while (z < len(columns[2])):
                    # for z in range(6):
                        word = letters[1] + columns[1][z]
                        letters.append(word)
                        if(length == 3):
                            used = False
                            for w in passwords:
                                if(word == w[:3]):
                                    results.append(w)
                                    used = True
                                    if(len(results) > 1):
                                        return ""
                                if(word[2] == w[2]):
                                    used = True
                            if(used == False):
                                columns[2].remove(columns[1][z])
                            else:
                                z += 1
                        elif(length > 3):
                            a = 0
                            while (a < len(columns[3])):
                                word = letters[2] + columns[1][a]
                                letters.append(word)
                                if(length == 4):
                                    used = False
                                    for w in passwords:
                                        if(word == w[:4]):
                                            results.append(w)
                                            used = True
                                            if(len(results) > 1):
                                                return ""
                                        if(word[3] == w[3]):
                                            used = True
                                    if(used == False):
                                        columns[3].remove(columns[1][a])
                                    else:
                                        a += 1
                                letters.pop()
                                print("after pop 4")
                                print(letters)
                        # if(usedz):
                        z += 1
                        letters.pop()
                        print("after pop 3")
                        print(letters)
                # if(usedy):
                y += 1
                letters.pop()
                print("after pop 2")
                print(letters)
        # if(usedx):
        x += 1
        letters.pop()
        print("after pop 1")
        print(letters)
    print("Got the word")
    print(results)
    # print(results[0])
    return results[0]

if __name__ == "__main__":
    password()