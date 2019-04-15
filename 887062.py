#Submission for UP887062

from graphics import *

#I decided to use global variables as my loop variables for two reasons. 
#Firstly, it demonstrates I understand the problem and haven't brute forced it
#Secondly, it allows for the program to be modified with smaller or larger 
#- patches by simply changing one variable. 
PAT_SIZE = 100
PAT_STEP = PAT_SIZE // 5
H_PAT_STEP = PAT_STEP // 2

def getInputs():
#Takes inputs from the user, stores the chosen colours and defines the lengths 
#- of other lists used in the program (patch type & colour)
    acceptedWinSizes = [5, 7, 9]
    acceptedColours = ['red', 'green', 'blue', 'magenta', 'orange', 'pink']
    chosenColours = []
    while True:
        winSize = input("Enter a valid window size (5, 7, 9) ")
        winSize = winSize.replace(" ", "")
        if winSize.isdigit():
            winSize = int(winSize)
            if winSize in acceptedWinSizes:
                # I have predefined the length of these lists to allow for 
                #- simple indexing later on
                patchType = [0] * (winSize ** 2) 
                patchColours = [""] * (winSize ** 2)
                winSize *= PAT_SIZE
                break
        print("Invalid window size")
    while len(chosenColours) < 3: 
        colour = input(
            "Enter a valid colour (red, green, blue, magenta, orange or pink) ")
        colour = colour.replace(" ", "")
        colour = colour.lower()
        if colour in acceptedColours:
            if colour in chosenColours:
                print("{0} has already been selected".format(colour.title()))
            else:
                chosenColours.append(colour)
        else:
            print("Invalid colour")
    return winSize, chosenColours, patchType, patchColours
    
def createWindow(winSize):
    win = GraphWin("UP887062's Coursework", winSize, winSize)
    win.setBackground('white')
    return win

def drawRectangle(win, p1, p2, colour):
    rectangle = Rectangle(p1, p2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)
    return rectangle 
    
#The rectangles and circles drawn are also stored in a list for further interaction

def drawCircle(win, centre, radius, colour):
    circ = Circle(centre, radius).draw(win)
    circ.setFill(colour)
    circ.setOutline(colour)
    return circ

def patchSix(win, startX, startY, colour):
    colourList = ['white', colour]
    patch = []
    for y in range(startY, startY + PAT_SIZE, PAT_STEP):
        for x in range(startX, startX + PAT_SIZE, PAT_STEP):
            colourIndex = (x // PAT_STEP) % 2
            if (y / PAT_STEP) % 2 == 0:
                colourIndex -= 1
            rect = drawRectangle(win, Point(x, y), Point(x + PAT_STEP, 
                                    y + PAT_STEP), colourList[colourIndex])
            patch.append(rect)
            for k in range(H_PAT_STEP // 2, PAT_STEP, H_PAT_STEP):
                for l in range(H_PAT_STEP // 2, PAT_STEP, H_PAT_STEP):
                    circ = drawCircle(win, Point(x + l, y + k), H_PAT_STEP // 2
                                                , colourList[colourIndex - 1])
                    patch.append(circ)
    return patch

#patchSix() & patchTwo() take the starting X & Y coords then, using modulus to 
#- distinguish odd and even lines, draw the patterns with the defined colour. 
#It also stores the patches as a list, which will then be added to the patchRepo 
#- list for use later on

def patchTwo(win, startX, startY, colour):
    patch = []
    for y in range(startY + H_PAT_STEP, startY + PAT_SIZE, PAT_STEP):
        for x in range(startX + H_PAT_STEP, startX + PAT_SIZE, PAT_STEP):
            hiBox = Text(Point(x, y), "hi!")
            hiBox.setTextColor(colour)
            hiBox.setSize(int(round(H_PAT_STEP * 0.8)))
            hiBorder = drawRectangle(win, Point(x - H_PAT_STEP, y - H_PAT_STEP), 
                                Point(x + H_PAT_STEP, y + H_PAT_STEP), colour)
            hiBorder.setFill('white')
            hiBox.draw(win)
            patch.append(hiBox)
            patch.append(hiBorder)
    return patch
    
def colAndRow(x, y):
    col = round(x // PAT_SIZE)
    row = round(y // PAT_SIZE)
    return col, row

#colAndRow() & patchIndex() have been split due to patchIndex being used on it's
#- own in functions like sectionOne()

def patchIndex(winSize, x, y):
    col, row = colAndRow(x, y)
    return int(row * (winSize / PAT_SIZE) + col)

def sectionOne(win, winSize, patchColours, colour, patchType, patchRepo):
#Draws the top left corner of the patchwork which doesn't involve changing patch
#Patch colour & type are stored as well as the objects themselves     
    for y in range(0, winSize - PAT_SIZE, PAT_SIZE):
        for x in range(0, winSize - PAT_SIZE - y, PAT_SIZE):
            index = patchIndex(winSize, x, y)
            patchType[index] = 1
            patchColours[index] = colour
            sixList = patchSix(win, x, y, colour)
            patchRepo[index] = sixList
    return patchRepo, patchType, patchColours

def sectionTwo(win, winSize, chosenColours, patchType, patchColours, patchRepo):
#Draws the bottom right corner of the patchwork. As well as alternating the 
#- columns (again using modulus), I have conditions on lines 135-136 that ensure
#- the third selected colour is used when needed.     
    for x in range(winSize - PAT_SIZE, -1, -PAT_SIZE):
        yStart = abs(x - winSize) - PAT_SIZE
        for y in range(yStart, winSize, PAT_SIZE):
            if x < winSize - PAT_SIZE and x >= PAT_SIZE * 2 and \
                y < winSize - PAT_SIZE and y > yStart:
                    colour = chosenColours[2]
            else:
                colour = chosenColours[1]
            index = patchIndex(winSize, x, y)
            patchColours[index] = colour
            if x % (PAT_SIZE * 2) == 0:
                patchType[index] = 2
                twoList = patchTwo(win, x, y, colour)
                patchRepo[index] = twoList
            else:
                patchType[index] = 1
                sixList = patchSix(win, x, y, colour)
                patchRepo[index] = sixList
    return patchRepo, patchType, patchColours

def createPatchwork(win, winSize, chosenColours, patchType, patchColours):
#Creates the patchwork and stores all data needed for the challenege features
    patchRepo = [[]] * ((winSize // PAT_SIZE) ** 2)
    patchRepo, patchType, patchColours = sectionOne(win, winSize, patchColours,
                        chosenColours[0], patchType, patchRepo)
    patchRepo, patchType, patchColours = sectionTwo(win, winSize, chosenColours, 
                                            patchType, patchColours, patchRepo)
    return patchRepo, patchType, patchColours

def drawBorder(win, borderP1, borderP2):
    border = drawRectangle(win, borderP1, borderP2, "")
    border.setOutline('black')
    border.setWidth(3)
    return border

def deletePatch(patchRepo, index):
    for i in patchRepo[index]:
        i.undraw()

def switchPatch(win, borderP1, patchType, patchColours, index, patchRepo):
#Switches the patch and stores the new patch type
    intBorderP1X, intBorderP1Y = int(borderP1.getX()), int(borderP1.getY())
    if patchType[index] == 1:
        patch = patchTwo(win, intBorderP1X, intBorderP1Y, patchColours[index])
        patchType[index] = 2
    else:
        patch = patchSix(win, intBorderP1X, intBorderP1Y, patchColours[index])
        patchType[index] = 1
    patchRepo[index] = patch

#No pre-condition required for switchPatch() or newPatch() as this is completed 
#- before the functions are called 

def newPatch(win, patchType, colour, index, borderP1, patchColours, patchRepo):
#Adds the final digit patch (patchTwo) and stores the type / colour
    twoList = patchTwo(win, int(borderP1.getX()), int(borderP1.getY()) , colour)
    patchType[index] = 2
    patchColours[index] = colour
    patchRepo[index] = twoList

def clickDetails(p1, winSize):
#Determines the patch that has been clicked and defines the points needed to 
#- draw the border. Both the index and border points are returned 
    pX, pY = p1.getX(), p1.getY()
    col, row = colAndRow(pX, pY)
    index = patchIndex(winSize, pX, pY)
    borderP1 = Point((col * PAT_SIZE), (row * PAT_SIZE))
    borderP2 = Point((col * PAT_SIZE) + PAT_SIZE, (row * PAT_SIZE) + PAT_SIZE)
    return borderP1, borderP2, index

def interact(win, winSize, patchType, patchColours, patchRepo):
#This function controls the challenge features of the program. 
#It uses conditional statements to determine which function to call. 
    while True:
        p1 = win.getMouse()
        borderP1, borderP2, index = clickDetails(p1, winSize)
        border = drawBorder(win, borderP1, borderP2)
        chosenKey = ""
        while chosenKey != 'Return':
            colourInitials = ['r', 'g', 'b', 'm', 'o', 'p']
            chosenKey = win.getKey()
            if chosenKey == 'd' and patchType[index] != 0:
                deletePatch(patchRepo, index)
                patchType[index] = 0
            elif chosenKey == 's'and patchType[index] != 0:
                deletePatch(patchRepo, index)
                border.undraw()
                switchPatch(win, borderP1, patchType, patchColours, index, 
                                                                    patchRepo)
                border.draw(win)
            elif chosenKey in colourInitials and patchType[index] == 0:
                colourList = ['red','green','blue','magenta','orange','pink']
                colour = colourList[colourInitials.index(chosenKey)]
                border.undraw()
                newPatch(win, patchType, colour, index, borderP1, patchColours, 
                                                                    patchRepo)
                border.draw(win)
        border.undraw()

def main():
#Essentially the program takes the users inputs, creates a window, draws the 
#- patchwork and then lets the user interact with it. 
    winSize, chosenColours, patchType, patchColours = getInputs()
    win = createWindow(winSize)
    patchRepo, patchType, patchColours = createPatchwork(win, winSize, 
                                        chosenColours, patchType, patchColours)
    interact(win, winSize, patchType, patchColours, patchRepo)

main()