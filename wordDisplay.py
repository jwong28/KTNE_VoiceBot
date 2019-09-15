import pyttsx3
import speech_recognition as sr

##File import
from speechToText import speechToText
import helper

engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

#Array of the words
ready = ["yes", "okay", "what", "middle", "left", "press", "right", "blank", "ready", "no", "first", "uhhh", "nothing", "wait"]
first = ["left", "okay", "yes", "middle", "no", "right", "nothing", "uhhh", "wait", "ready", "blank", "what", "press", "first" ]
no = ["blank", "uhhh", "wait", "first", "what", "ready", "right", "yes", "nothing", "left", "press", "okay", "no", "middle"]
blank = ["wait", "right", "okay", "middle", "blank", "press", "ready", "nothing", "no", "what", "left", "uhhh", "yes", "first"]
nothing = ["uhhh", "right", "okay", "middle", "yes", "blank", "no", "press", "left", "what", "wait", "first", "nothing", "ready"]
yes = ["okay", "right", "uhhh", "middle", "first", "what", "press", "ready", "nothing", "yes", "left", "blank", "no", "wait"]
what = ["uhhh", "what", "left", "nothing", "ready", "blank", "middle", "no", "okay", "first", "wait", "yes", "press", "right"]
uhhh = ["ready", "nothing", "left", "what", "okay", "yes", "right", "no", "press", "blank", "uhhh", "middle", "wait", "first"]
left = ["right", "left", "first", "no", "middle", "yes", "blank", "what", "uhhh", "wait", "press", "ready", "okay", "nothing"]
right = ["yes", "nothing", "ready", "press", "no", "wait", "what", "right", "middle", "left", "uhhh", "blank", "okay", "first"]
middle = ["blank", "ready", "okay", "what", "nothing", "press", "no", "wait", "left", "middle", "right", "first", "uhhh", "yes"]
okay = ["middle", "no", "first", "yes", "uhhh", "nothing", "wait", "okay", "left", "ready", "blank", "press", "what", "right"]
wait = ["uhhh", "no", "blank", "okay", "yes", "left", "first", "press", "what", "wait", "nothing", "ready", "right", "middle"]
press = ["right", "middle", "yes", "ready", "press", "okay", "nothing", "uhhh", "blank", "left", "first", "what", "no", "wait"]
you = ["sure", "you are", "your", "you're", "next", "uh huh", "ur", "hold", "what?", "you", "uh uh", "like", "done", "u"]
youAre = ["your", "next", "like", "uh huh", "what?", "done", "uh uh", "hold", "you", "u", "you're", "sure", "ur", "you are"]
your = ["uh uh", "you are", "uh huh", "your", "next", "ur", "sure", "u", "you're", "you", "what?", "hold", "like", "done"]
youre = ["you", "you're", "ur", "next", "uh uh", "you are", "u", "your", "what?", "uh huh", "sure", "done", "like", "hold"]
ur = ["done", "u", "ur", "uh huh", "what?", "sure", "your", "hold", "you're", "like", "next", "uh uh", "you are", "you"]
u = ["uh huh", "sure", "next", "what?", "you're", "ur", "uh uh", "done", "u", "you", "like", "hold", "you are", "your"]
uhHuh = ["uh huh", "your", "you are", "you", "done", "hold", "uh uh", "next", "sure", "like", "you're", "ur", "u", "what?"]
uhUh = ["ur", "u", "you are", "you're", "next", "uh uh", "done", "you", "uh huh", "like", "your", "sure", "hold", "what?"]
      # "what?" == whatt
whatt = ["you", "hold", "you're", "your", "u", "done", "uh uh", "like", "you are", "uh huh", "ur", "next", "what?", "sure"]
done = ["sure", "uh huh", "next", "what?", "your", "ur", "you're", "hold", "like", "you", "u", "you are", "uh uh", "done"]
wordNext = ["what?", "uh huh", "uh uh", "your", "hold", "sure", "next", "like", "done", "you are", "ur", "you're", "u", "you"]
hold = ["you are", "u", "done", "uh uh", "you", "ur", "sure", "what?", "you're", "next", "hold", "uh huh", "your", "like"]
sure = ["you are", "done", "like", "you're", "you", "hold", "uh huh", "ur", "sure", "u", "what?", "next", "your", "uh uh"]
like = ["you're", "next", "u", "ur", "hold", "done", "uh uh", "what?", "uh huh", "you", "like", "sure", "you are", "your"]

def wordDisplay():
      # getSecondPart("ready")
      engine.say("Say done when module is finished")
      while(True):
            engine.say("What is the display word")
            engine.runAndWait()
            res = speechToText(recognizer, microphone)
            print(res["text"])
            if(helper.checkResponse(res)):
                  if("done" in res["text"]):
                        engine.say("Ok, done")
                        return
                  questionTwo = "What is the word in the"
                  # questionTwo += checkWord(res["text"].lower())
                  position = checkWord(res["text"].lower())
                  if not(position == ""):
                        questionTwo += position
                        getSecondPart(questionTwo)
                  

def checkWord(phrase):
      if("yes" in phrase):
            return "middle left"
      elif("first" in phrase):
            return "top right"
      elif("display" in phrase):
            return "bottom right"
      elif("okay" in phrase or "ok" in phrase):
            return "top right"
      elif("says" in phrase):
            return "bottom right"
      elif("no" in phrase):
            return "bottom right"
      # elif("reed" in phrase):
      #       return "bottom left"
      elif("hold on" in phrase):
            return "bottom right"
      elif("letter" in phrase):
            if("c" in phrase or "see" in phrase or "sea" in phrase):
                  return "top right"
      # Ambiguity words
      elif("nothing" in phrase or "blank" in phrase or "empty" in phrase):
            return ambiguity("blank", 1)
      elif("led" in phrase or "lead" in phrase or "leed" in phrase):
            return ambiguity("lead", 1)
      elif("read" in phrase or "red" in phrase or "reed" in phrase):
            return ambiguity("read", 1)
      elif("you" in phrase or "you are" in phrase or 
      "your" in phrase or "you're" in phrase or
      "ur" in phrase):
            return ambiguity("you", 1)
      elif("there" in phrase or "they're" in phrase or
      "they are" in phrase or "their" in phrase):
            return ambiguity("they", 1)
      elif("see" in phrase or "c" in phrase or
      "cee" in phrase or "sea" in phrase):
            return ambiguity("c", 1)
      else:
            return ""


def ambiguity(word, phase):
      choices = []
      if(phase == 1):
            if(word == "blank"):
                  question = "Say 1 if it is empty, 2 if word is nothing, 3 if word is blank"
                  choices = ["empty", "nothing", "blank"]
            elif(word == "lead"):
                  question = "Say 1 if word is l e d, 2 if l e a d, 3 if l e e d"
                  choices = ["led","lead", "leed"]
            elif(word == "read"):
                  question = "Say 1 if word is r e a d, 2 if r e d, 3 if r e e d"
                  choices = ["read", "red", "reed"]
            elif(word == "you"):
                  question = "Say 1 if word is y o u, 2 if y o u space a r e, 3 if y o u r "
                  question += "4 if y o u apostrophe r e, 5 if letters u r"
                  choices = ["you", "you are", "your", "youre", "ur"]
            elif(word == "they"):
                  question = "Say 1 if word is t h e r e, 2 if t h e i r, 3 if t h e y space a r e "
                  question += "4 if t h e y apostrophe r e"
                  choices = ["there", "their", "they are", "theyre"]
            elif(word == "c"):
                  question = "Say 1 if word is s e e, 2 if c e e, 3 if letter c"
                  choices = ["see", "c", "cee"]
            else:
                  return ""
      else:
            if(word == "what"):
                  question = "Say 1 if there is a question mark, two for just what"
                  choices = ["whatt", "what"]
            elif(word == "uh"):
                  question = "Say 1 if word is u h h h, 2 if u h h u h, 3 if u h u h"
                  choices = ["uhhh", "uhhuh", "uhuh"]
            elif(word == "you"):
                  question = "Say 1 if word is y o u, 2 if y o u r, 3 if y o u  space a r e, "
                  question += "4 if y o u apostrophe r e, 5 if u r, 6 if letter u"
                  choices = ["you", "your", "you are", "you're", "ur", "u"]
      while(True):
            engine.say(question)
            engine.runAndWait()
            res = speechToText(recognizer, microphone)
            print(res["text"])
            if(helper.checkResponse(res)):
                  #Split text by space and get the number
                  arr = res["text"].strip().lower().split()
                  for a in arr:
                        num = helper.getNumber(a.strip())
                        if(num > len(choices)):
                              word = choices[num - 1]
                              if(phase == 1):
                                    if(word == "empty"):
                                          return "bottom left"
                                    elif(word == "nothing"):
                                          return "middle left"
                                    elif(word == "blank"):
                                          return "middle right"
                                    elif(word == "led"):
                                          return "middle left"
                                    elif(word == "lead"):
                                          return "bottom right"
                                    elif(word == "leed"):
                                          return "bottom left"
                                    elif(word == "red"):
                                          return "middle right"
                                    elif(word == "read"):
                                          return "middle right"
                                    elif(word == "reed"):
                                          return "bottom left"
                                    elif(word == "you"):
                                          return "middle right"
                                    elif(word == "you are"):
                                          return "bottom right"
                                    elif(word == "your"):
                                          return "middle right"
                                    elif(word == "youre"):
                                          return "middle right"
                                    elif(word == "ur"):
                                          return "top left"
                                    elif(word == "there"):
                                          return "bottom right"
                                    elif(word == "their"):
                                          return "middle right"
                                    elif(word == "they are"):
                                          return "middle left"
                                    elif(word == "theyre"):
                                          return "bottom left"
                                    elif(word == "see"):
                                          return "bottom right"
                                    elif(word == "c"):
                                          return "top right"
                                    elif(word == "cee"):
                                          return "bottom right"
                              else:
                                    if(word == "whatt"):
                                          read(whatt)
                                    elif(word == "what"):
                                          read(what)
                                    elif(word == "uhhh"):
                                          read(uhhh)
                                    elif(word == "uhhuh"):
                                          read(uhHuh)
                                    elif(word == "uhuh"):
                                          read(uhUh)
                                    elif(word == "you"):
                                          read(you)
                                    elif(word == "your"):
                                          read(your)
                                    elif(word == "you are"):
                                          read(youAre)
                                    elif(word == "you're"):
                                          read(youre)
                                    elif(word == "ur"):
                                          read(ur)
                                    elif(word == "u"):
                                          read(u)
                                    return ""

def getSecondPart(question):
      while(True):
            engine.say(question)
            engine.runAndWait()
            res = speechToText(recognizer, microphone)
            print(res["text"])
            phrase = ""
            if(helper.checkResponse(res)):
                  phrase = res["text"]
            # if(1 == 1):
                  phrase = "ready set go"
                  if("ready" in phrase):
                        read(ready)
                  elif("first" in phrase):
                        read(first)
                  elif("no" in phrase):
                        read(no)
                  elif("yes" in phrase):
                        read(yes)
                  elif("left" in phrase):
                        read(left)
                  elif("right" in phrase):
                        read(right)
                  elif("middle" in phrase):
                        read(middle)
                  elif("okay" in phrase):
                        read(okay)
                  elif("wait" in phrase):
                        read(wait)
                  elif("press" in phrase):
                        read(press)
                  elif("done" in phrase):
                        read(done)
                  elif("next" in phrase):
                        read(wordNext)
                  elif("hold" in phrase):
                        read(hold)
                  elif("sure" in phrase):
                        read(sure)
                  elif("like" in phrase):
                        read(like)
                  elif("blank" in phrase):
                        read(blank)
                  elif("nothing" in phrase):
                        read(nothing)
                  elif("letter" in phrase):
                        if("you" in phrase or "u" in phrase):
                              read(u)
                  elif("triple" in phrase or "three" in phrase):
                        read(uhhh)
                  elif("what" in phrase):
                        checkWord("what")
                  elif("uh" in phrase):
                        checkWord("uh")
                  elif("you" in phrase):
                        checkWord("you")
                  


def read(arr):
      count = 0
      output = ""
      # engine.say(arr)
      # engine.runAndWait()
      for word in arr:
            count += 1
            if(word == "uhhh"):
                  output += "uhhh "
            elif(word == "what"):
                  output += "what no question "
            elif(word == "what?"):
                  output += "what question mark "
            elif(word == "u"):
                  output += "letter u "
            elif(word == "u"):
                  output += "letters u and r "
            elif(word == "you"):
                  output += "word you "
            elif(word == "your"):
                  output += "y o u r "
            elif(word == "you're"):
                  output += "y o u apostrophe r e "
            elif(word == "you are"):
                  output += "you space are "
            elif(word == "uh huh"):
                  output += "u h space h u h "
            elif(word == "uh uh"):
                  output += "u h space u h "
            else:
                  output += word + " "
            # Say 5 words at a time
            if(count == 5):
                  engine.setProperty('rate', 150)
                  engine.say(output)
                  engine.runAndWait()
                  count = 0
                  engine.say("Need more words?")
                  confirm = helper.checkConfirm()
                  if(not confirm):
                        return
                  


# if __name__ == "__main__":
#       wordDisplay()