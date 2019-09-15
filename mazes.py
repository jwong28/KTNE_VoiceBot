import pyttsx3
import speech_recognition as sr
import math

##File import
from speechToText import speechToText
import helper

engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

nthNum = ["first", "second", "third", "fourth", "fifth", "sixth"]
#First get all possible movements for a specific cell
# Top left is (0,0), bottom right is (5,5)
# u = up, d = down, l = left, r = right
# Column then row coordinates for cirlce
# Maze 1: (1,2), (6,3)
maze1 = [["d r","l r","l d","r d","l r","l"],
          ["u d","r d","u l","u r","l r","l d"],
          ["u d","u r","l d","d r","l r","l u d"],
          ["u d","r","l r u","l u","r","l u d"],
          ["u d r","r l","d l","r d","l","u d"],
          ["u r","l","u r","u l","r","u l"]]
# Maze 2: (2,4), (5,2)
maze2 = [["r","l r d","l","d r","l r d","l"],
        ["d r","l u","r d","l u","u r","l d"],
        ["u d","d r","l u","d r","l r","u d l"],
        ["u d r","l u","d r","l u","d","u d"],
        ["u d","d","u d","d r","u l","u d"],
        ["u","u r","l u","u r","l r","l u"]]
# Maze 3: (4,4), (6,4)
maze3 = [["d r","l r","l d","d","d r","l d"],
        ["u","d","u d","u r","u l","u d"],
        ["d r","u d l","u d","d r","d l","u d"],
        ["u d","u d","u d","u d","u d","u d"],
        ["u d","u r","u l","u d","u d","u d"],
        ["u r","l r","l r","u l","u r","u l"]]
# Maze 4: (1,1), (1,4)
maze4 = [["d r ","d l","l r","l r","l r","d l"],
        ["u d","u d","d r","l r","l r","u d l"],
        ["u d","u r","u l","d r","l","u d"],
        ["u d","r","l r","u l r","l r","u d l"],
        ["u d r","l r","l r","l r","d u","u d"],
        ["u r","l r","l","r","l u","u"]]
# Maze 5: (4,6), (5,3)
maze5 = [["r","r l","r l","r l","d r l","l d"],
        ["d r","l r","l r","d l r","l u","u"],
        ["u d r","d l","r","l u","d r","l d"],
        ["u d","u r","l r","l d","u","u d"],
        ["u d","d r","l r","u l r","l","u d"],
        ["u","u r","l r","l r","l r","u l"]]
# Maze 6: (5,1), (3,5)
maze6 = [["d","d r","d l","r","d r l","d l"],
        ["u d","u d","u d","d r","u l","u d"],
        ["u d r","l u","u","u d","d r","u l"],
        ["u r","d l","d r","u d l","u d","d"],
        ["d r","u l","u","u d","u r","u d l"],
        ["u r","l r","l r","l u","r","l u"]]
# Maze 7: (2,1), (2,6)
maze7 = [["d r","l r","l r","d l","d r","l d"],
        ["u d","d r","l","u r","u l","u d"],
        ["u r","u l","d r","l","d r","u l"],
        ["d r","d l","u d r","l r","u l","d"],
        ["u d","u","u r","l r","d l","u d"],
        ["u r","l r","l r","l r","u l r","u l"]]
# Maze 8: (4,1), (3,4)
maze8 = [["d","d r","l r","l d","d r","l d"],
        ["u d r","u l r","l","u r","u l","u d"],
        ["u d","d r","l r","l r","d l","u d"],
        ["u d","u r","d l","r","u l r","u l"],
        ["u d","d","u r","l r","l r","l"],
        ["u r","u l r","l r","l r","l r","l"]]
# Maze 9: (1,5), (3,2)
maze9 = [["d","d r","l r","l r","d l r","d l"],
        ["u d","u d","d r","l","u d","u d"],
        ["u d r","u l r","u l","d r","u l","u d"],
        ["u d","d","d r","u l","r","u d l"],
        ["u d","u d","u d","d r","l d","u"],
        ["u r","u l","u r","u l","u r","l"]]
# circles = [[2,1],[]]
circles = [[1,2],[6,3],[2,4],[5,2],[6,4],[4,4],[1,4],[1,1],
    [4,6],[5,3],[5,1],[3,5],[2,1],[2,6],[4,1],[3,4],[1,5],[3,6]]
circle = ["",""]
numWord = ["first", "second", "third", "fourth", "fifth", "sixth"]
end = ["", ""]

# Branch coor
branches = ()
# Number of branches 
branchNums = ()
# Branch directions
options = ()
# The actual path
path = ()
# The index of the branches on the path
pathIndex = ()

def mazes():
    global mazeNum
    global end
    global circle
    getMazeNum()
    # mazeNum = 7
    # num = 1
    # start = [3,4]
    # end = [2,1]
    # getMazeNum()
    start = getStartEnd()
    initial = "Start is " +  str(start[0]+1) + " " + str(start[1]+1) + " end is " + str(end[0]+1) + " " + str(end[1]+1) 
    engine.setProperty('rate', 150)
    engine.say(initial)
    print(initial)
    engine.runAndWait()
    # Rotate and switch coordinates. May switch in the function itself
    print("New start and end")
    print(start)
    print(end)
    # path = findPath(start,"", "")
    engine.setProperty('rate', 75)
    # engine.say(maze2)
    # engine.runAndWait()
    
    cur = findPath(start,"","")
    # print("returned to main")
    sayMoves()
    engine.setProperty('rate',200)
    # print(cur)
    print(path)

def getMazeNum():
    global mazeNum
    while(True):
        engine.say("Where are the circles in column then row order")
        engine.runAndWait()
        res = speechToText(recognizer, microphone)
        print(res["text"])
        if(helper.checkResponse(res)):
        # if(1 == 1):
            try:
                # ans = res["text"].strip().lower().split()
                # ans = "1 2"
                c = determinePos(res["text"])
                # return when both circle positions are obtained and in the map
                if not(c[0] == 100 and c[1] == 100):
                    if(c in circles):
                        mazeNum = math.ceil((circles.index(c)+1)/2)
                        print("solution")
                        print(mazeNum)
                        return
                # return                        
            except ValueError:
                print("Maze circles error")
                continue

# Get the starting and ending positions
def getStartEnd():
    global end
    start = [100, 100]
    end = [100, 100]
    while(start[0] == 100 or start[1] == 100 or end[0] == 100 or end[1] == 100):
        if(start[0] == 100 and start[1] == 100):
            engine.say("Start position")
        elif(end[0] == 100 and end[1] == 100):
            engine.say("End position")
        engine.runAndWait()
        res = speechToText(recognizer, microphone)
        print(res["text"])
        if(helper.checkResponse(res)):
            try:
                # ans = res["text"].strip().lower().split()
                if(start[0] == 100 and start[1] == 100):
                    # engine.say("Start position")
                    s = determinePos(res["text"])
                    start = [s[1] - 1, s[0] - 1]
                    print("New start")
                    print(start)
                elif(end[0] == 100 and end[1] == 100):
                    e = determinePos(res["text"])
                    end = [s[1] - 1, e[0] - 1]
                    print("end")
                    print(end)
            except ValueError:
                print("Start end error")
                continue
        if(end[0] == 100 and end[1] == 100):
            print("Not completed yet")
        if(not(start[0] == 100 or start[1] == 100 or end[0] == 100 or end[1] == 100)):
            print("Both is all full")
            print(start)
            print(end)
            return start

def determinePos(phrase):
    r = 99
    c = 99
    pos = [100,100]
    print(phrase)
    words = phrase.strip().lower().split()
    print("The phrase is ")
    print(words)
    if("row" in words):
        r = words.index("row")
        print("Found row in index: " + str(r))
    if("col" in words):
        c = words.index("col")
        print("Found col in index: " + str(c))
    elif("column" in words):
        c = words.index("column")
        print("Found column in index: " + str(c))
    for x in range(len(words)):
        print("For the step: " + str(x))
        word = words[x]
        n = helper.getNumber(word)
        print("The word: " + word + " converted to number is "+ str(n))
        # Get the index of rows and columns word if exist
        if(r < c):
            print("Awaiting input in row")
            if(word in numWord):  
                if(pos[1] == 100):
                    pos[1] = numWord.index(word) + 1
                    r = 99
            elif(word in helper.numWord):  
                if(pos[1] == 100):
                    pos[1] = helper.numWord.index(word)
                    r = 99
            elif(isinstance(n, int)):
                if(pos[1] == 100):
                    pos[1] = n
                    print(pos)
                    r = 99
        elif(c < r):
            print("Awaiting input in col")
            if(word in numWord):  
                if(pos[0] == 100):
                    pos[0] = numWord.index(word) + 1
                    c = 99
            elif(word in helper.numWord):  
                if(pos[0] == 100):
                    pos[0] = helper.numWord.index(word)
                    c = 99
            elif(isinstance(n, int)):
                if(pos[0] == 100):
                    pos[0] = n
                    print(pos)
                    c = 99
        elif(word in numWord):  
            if(pos[0] == 100):
                pos[0] = numWord.index(word) + 1
            elif(pos[1] == 100):
                pos[1] = numWord.index(word) + 1
        elif(word in helper.numWord):  
            if(pos[0] == 100):
                pos[0] = helper.numWord.index(word)
            elif(pos[1] == 100):
                pos[1] = helper.numWord.index(word)
        elif(isinstance(n, int)):
            if(pos[0] == 100):
                pos[0] = n
            elif(pos[1] == 100):
                pos[1] = n
        # return
    print("pos: ")
    print(pos)
    return pos

# Find the path with the coordinates
def findPath(start, move, nextM):
    global branches
    global options
    global branchNums
    global path
    global pathIndex
    global mazeNum
    global end
    print("The next move is "+ nextM)
    # At the beginning, check both branches aka. If next move is ""
    #   then we can check both l , r. So deal with branches in the beginning.
    #  will follow the path later
    # Maze[row] [col]
    cur = start
    # maze = maze2
    if(mazeNum == 1):
        maze = maze1
    elif(mazeNum == 2):
        maze = maze2
    elif(mazeNum == 3):
        maze = maze3
    elif(mazeNum == 4):
        maze = maze4
    elif(mazeNum == 5):
        maze = maze5
    elif(mazeNum == 6):
        maze = maze6
    elif(mazeNum == 7):
        maze = maze7
    elif(mazeNum == 8):
        maze = maze8
    elif(mazeNum == 9):
        maze = maze9
    # path = []
    # If finished
    if(cur == end):
        return cur
    # If next move exists, move to it
    print("WHAT IS NEXT MMMMMM: " + nextM)
    nextMove = nextM
    if(nextMove == "u"):
        print("Last move u")
        cur[0] = cur[0] - 1
        lastMove = "u"
    elif(nextMove == "d"):
        print("Last move d")
        cur[0] = cur[0] + 1
        lastMove = "d"
    elif(nextMove == "r"):
        print("Last move r")
        cur[1] = cur[1] + 1
        lastMove = "r"
    elif(nextMove == "l"):
        print("Last move l")
        cur[1] = cur[1] - 1
        lastMove = "l"
    else:
        lastMove = ""
    if(nextMove == ""):
        print("Next move is empty")
    else:
        print("From next, appending: "+ lastMove)
        pathList = list(path)
        pathList.append(lastMove)
        path = tuple(pathList)
        # path.append(lastMove)
        
    while(not cur == end):
        print("CALLING IN WHILE LOOP")
        print(cur)
        # Follow given path until branch is possible 
        # If options has 2 characters, then theres a branch
        optionsList = maze[cur[0]][cur[1]].split()
        # Remove possible backtrack move
        print("last move is "+ lastMove)
        move = ""
        if(lastMove == "u"):
            move = "d"
        elif(lastMove == "d"):
            move = "u"
        elif(lastMove == "r"):
            move = "l"
        elif(lastMove == "l"):
            move = "r"
        if(move in optionsList):
            optionsList.remove(move)
        print("After move if possible is ")
        print(optionsList)
        branchLength = 1
        if(len(optionsList) > 1):
            # save the current position
            branchList = list(branches)
            r = cur[0]
            c = cur[1]
            branchList.append(r)
            branchList.append(c)
            branches = tuple(branchList)
            # Can only be two or three branches
            numList = list(branchNums)
            print("The amount of branches available are ")
            print(optionsList)
            optionsBranch = list(options)
            if(len(optionsList)== 2):
                # optionsBranch.append([optionsList[0],optionsList[1]])
                optionsBranch.append(optionsList[0]) 
                optionsBranch.append(optionsList[1])
                numList.append(2)
            if(len(optionsList)== 3):
                optionsBranch.append(optionsList[0])
                optionsBranch.append(optionsList[1])
                optionsBranch.append(optionsList[2])
                numList.append(3)
            # for word in optionsList:
            # optionsBranch.append(len(optionsList))
            options = tuple(optionsBranch)  
            print("The options for branches are")
            print(options)   
            branchNums = tuple(numList)
            print("The amount of branches for each branch are")
            print(branchNums)
            # branchLength = len(optionsList)
            branchLength = branchNums[len(branchNums)-1]
        # print("GEtting branches: ")
        # print(options)
        # print("done options")
        # Is this needed, no popping above
        if(len(optionsList) == 0):
            return cur
        # Deal with branches
        if(branchLength > 1):
        # Else if can move and wasn't last move
            # for word in options[len(options)-1]:
            branchPath = ""
            # Put the index of the starting point of the new branch
            indexList = list(pathIndex)
            indexList.append(len(path))
            pathIndex = tuple(indexList)
            print("The index lists of all the branches")
            print(pathIndex)
            # for x in range(branchLength):
            while(not branchNums[0] == 0):
                # print("The starting x values are")
                # print(x)
                # Get the branch coordinates. Since getting 1 branch, -1 from that branchNum
                print("Indexes of the branches are")
                print(pathIndex)
                print("Get the coordinates of the branch")
                print(branches)
                branchList = list(branches)
                c = branchList[len(branchList)-1]
                r = branchList[len(branchList)-2]
                # print("After popping the branch")
                # branches = tuple(branchList)
                startCoor = [r,c]
                print(branches)
                optionsBranch = list(options)
                word = optionsBranch.pop()
                print("Item has been popped " + word)
                print("popped during ")
                print(start)
                options = tuple(optionsBranch)
                print("Position for start is ")
                # if(startCoor == end):
                #     return
                print(startCoor)
                print("ending ")
                print(end)
                numList = list(branchNums)
                num = numList.pop()
                # If the current branch position has more branches
                if(num-1 > 0):
                    numList.append(num-1)
                # No more branches for the current branch
                else:
                    print("necessary to remove, no more nums left in the branch")
                     # No more paths within this branch, pop index
                    indexList = list(pathIndex)
                    indexList.pop()
                    pathIndex = tuple(indexList)
                    # Pop the coords off cause done
                    branchList = list(branches)
                    branchList.pop()
                    branchList.pop()
                    branches = tuple(branchList)
                branchNums = tuple(numList)
                print("Nums within branc")
                print(branchNums)
                if(word == "u"):
                    # branchPath = 
                    cur = findPath(startCoor, lastMove, "u")
                    print("Recieving path from up")
                    print(branchPath)
                elif(word == "d"):
                    # branchPath = 
                    cur = findPath(startCoor, lastMove, "d")
                    print("Recieving path from down")
                    print(branchPath)
                elif(word == "l"):
                    # branchPath = 
                    cur = findPath(startCoor, lastMove, "l")
                    print("Recieving path from left")
                    print(branchPath)
                elif(word == "r"):
                    # branchPath = 
                    cur = findPath(startCoor, lastMove, "r")  
                    print("Recieving path from right")
                    print(branchPath)
                # If finished return!!
                if(cur == end): 
                    return cur
                print("Current position")
                print(cur)
                # If run into wall, remove from path
                # if(branchPath == ""):
                # Put the index of the starting point of the new branch
                # indexList = list(pathIndex)
                print("Ran into walllllll")
                print("Options branch")
                print(options)
                length = len(path)
                start = pathIndex[len(pathIndex)-1]
                print("need to remove from index " + str(start) + " to " + str(length))
                # indexList.append(len(indexList))
                # pathIndex = tuple(indexList)
                # Delete from index to end, aka path
                pathList = list(path)
                print(path)
                diff = length - start
                print("The difference is " + str(diff))
                for x in range(diff):
                    pathList.pop()
                # del pathList[pathIndex[len(pathIndex)-1]:length]
                print("Before converting back")
                print(pathList)
                path = tuple(pathList)
                print("After removing broken paths")
                print(path)
                print("Start position is ")
                print(startCoor)
                print("The branches left after end while")
                print(branches)
                print("The nubers left ")
                print(branchNums)
                # print("The ending x values are")
                # print(x)
            # else:
            #     print("didnt run into wall, returning")
            #     indexList = list(pathIndex)
            #     indexList.pop()
            #     pathIndex = tuple(indexList)
            #     print(path)
            #     # Pop the coords off cause done
            #     branchList = list(branches)
            #     c = branchList[len(branchList)-1]
            #     r = branchList[len(branchList)-2]
            #     print("After popping the branch")
            #     branches = tuple(branchList)
            #     return 
                    # return ""  
            # Out of for loop, pop the nums dont pop if using while loop
            # numList = list(branchNums)
            # numList.pop()
            # branchNums = tuple(numList)
            # # No more paths within this branch, pop index
            # indexList = list(pathIndex)
            # indexList.pop()
            # pathIndex = tuple(indexList)
            # # Pop the coords off cause done
            # branchList = list(branches)
            # branchList.pop()
            # branchList.pop()
            print("After popping the branch")
            branches = tuple(branchList)
            print(branches)
            print("popped off the index as well")
            print(pathIndex)
            print("nums left")
            print(branchNums)
            print("Options branch")
            print(options)
            return cur
        # Prioritize up down then right left
        # Go down
        elif(cur[0] < end[0] and "d" in optionsList):
            cur[0] = cur[0] + 1
            lastMove = "d"
            print("Priority down")
        # Go up
        elif(cur[0] > end[0] and "u" in optionsList):
            cur[0] = cur[0] - 1
            lastMove = "u"
            print("Priority up")
        # Go right
        elif(cur[1] < end[1] and "r" in optionsList):
            cur[1] = cur[1] + 1
            lastMove = "r"
            print("Priority right")
        # Go left
        elif(cur[1] > end[1] and "l" in optionsList):
            cur[1] = cur[1] - 1
            lastMove = "l"
            print("Priority left")
        # Follow path
        else:
            for word in optionsList:
                if(not word == move):
                    if(word == "u"):
                        # Go up
                        cur[0] = cur[0] - 1
                        lastMove = "u"
                        print("Force up")
                    elif(word == "d"):
                        # Go down
                        cur[0] = cur[0] + 1
                        lastMove = "d"
                        print("Force down")
                    elif(word == "r"):
                        # Go right
                        cur[1] = cur[1] + 1
                        lastMove = "r"
                        print("Force right")
                    elif(word == "l"):
                        # Go left
                        cur[1] = cur[1] - 1
                        lastMove = "l"
                        print("Force left")
        # path.append(lastMove)
        pathList = list(path)
        pathList.append(lastMove)
        path = tuple(pathList)
        print("THE PATH IS NOW:           dfdsf")
        print(path)
        print("THE NEW CURRENT:   is")
        print(cur)
        print("The ending is still   ")
        print(end)
        if(cur == end):
            print("Current and ending is equal")
            return cur
        else:
            print("THEY ARE STILL NOT TRUE")
    return cur

def sayMoves():
    global path
    ans = " "
    for x in path:
        if(x == "u"):
            ans += "up "
        elif(x == "d"):
            ans += "down "
        elif(x == "r"):
            ans += "right "
        elif(x == "l"):
            ans += "left"
    engine.say(ans)
    engine.runAndWait()