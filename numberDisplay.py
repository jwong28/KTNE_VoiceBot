import pyttsx3
import speech_recognition as sr

##File import
from speechToText import speechToText
import helper

engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def numberDisplay():
    phase = 1
    results = []
    while(True):
        engine.say("Phase "+ str(phase) + "What are the numbers")
        engine.runAndWait()
        res = speechToText(recognizer, microphone)
        print(res["text"])
        if(helper.checkResponse(res)):
            try:
                ans = res["text"].strip().lower().split()
                nums = getNumbers(ans)
                if(len(nums) == 5):
                    # engine.say(nums)
                    # engine.runAndWait()
                    results = calculateAnswer(phase, nums, results)
                    phase = phase + 1
                    if(phase == 6):
                        return
            except ValueError:
                print("Number display error")
    return

def calculateAnswer(phase, nums, results):
    #Nums[0] is input
    num = nums[0]
    print("Phase "+ str(phase) + "    : " + str(nums))
    # Put an uncalled value in num[0]
    nums[0] = 9
    #Results is based on phase, [position, label]
    # First phase
    if(phase == 1):
        if(num == 1):
            engine.say("Position two")
            results.append([2,nums[2]])
        elif(num == 2):
            engine.say("Position two")
            results.append([2,nums[2]])
        elif(num == 3):
            engine.say("Position three")
            results.append([3,nums[3]])
        else:
            engine.say("Position four")
            results.append([4,nums[4]])
    # Second phase  
    elif(phase == 2):
        #Label 4
        if(num == 1):
            engine.say("Position "+ str(nums.index(4)))
            results.append([nums.index(4),4])
        # Position as phase 1
        elif(num == 2):
            engine.say("Position "+ str(results[0][0]))
            results.append([results[0][0],nums[results[0][0]]])
        elif(num == 3):
            engine.say("Position 1")
            results.append([1,nums[1]])
        #Position as phase 1
        else:
            engine.say("Position "+ str(results[0][0]))
            results.append([results[0][0],nums[results[0][0]]])
    # Phase 3
    elif(phase == 3):
        # Label as phase 2
        if(num == 1):
            engine.say("Position "+ str(nums.index(results[1][1])))
            results.append([nums.index(results[1][1]),results[1][1]])
        # Label as phase 1
        elif(num == 2):
            engine.say("Position "+ str(nums.index(results[0][1])))
            results.append([nums.index(results[0][1]),results[0][1]])
        elif(num == 3):
            engine.say("Position 3")
            results.append([3,nums[3]])
        #Label 4
        else:
            engine.say("Position "+ str(nums.index(4)))
            results.append([nums.index(4),4])
    # Phase 4
    elif(phase == 4):
        # Position as phase 1
        if(num == 1):
            engine.say("Position "+ str(results[0][0]))
            results.append([results[0][0],nums[results[0][0]]])
        elif(num == 2):
            engine.say("Position 1")
            results.append([1,nums[1]])
        # Position as phase 2
        elif(num == 3):
            engine.say("Position "+ str(results[1][0]))
            results.append([results[1][0],nums[results[1][0]]])
        # Position as phase 2
        else:
            engine.say("Position "+ str(results[1][0]))
            results.append([results[1][0],nums[results[1][0]]])
    # Phase 5
    else:
        # Label as phase 1
        if(num == 1):
            engine.say("Position "+ str(nums.index(results[0][1])))
        # Label as phase 2
        elif(num == 2):
            engine.say("Position "+ str(nums.index(results[1][1])))
        # # Label as phase 4
        elif(num == 3):
            engine.say("Position "+ str(nums.index(results[3][1])))
        # # Label as phase 3
        else:
           engine.say("Position "+ str(nums.index(results[2][1])))
    engine.runAndWait()
    return results

def getNumbers(arr):
    ans = []
    for word in arr:
        num = helper.getNumber(word)
        if(num > 0 and num < 5):
            ans.append(num)
        # If interpreted as a 2 or more digit word
        elif(num > 10):
           for i in str(num):
               ans.append(int(i)) 
    return ans