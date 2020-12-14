import pyautogui as pyA
import time
import cv2
from datetime import datetime

#load me into tft matches all night     if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/notread.png', confidence = 0.75) != None:



def getIntoFirstGame():
    time.sleep(3)

    pic1 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/TFTtab2.png', confidence = 0.75)
    if pic1 != None:
        print("Pic found!")
        pic1 = pyA.center(pic1)
        pic1X, pic1Y = pic1
        time.sleep(1)
        pyA.click(pic1X, pic1Y) 
        pyA.mouseDown()
        pyA.mouseUp()
    else:
        print("Did not find first TFT Tab")
        return

    time.sleep(3)

    pic2 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/playbutton.PNG', confidence = 0.75)
    pic22 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/partybutton.PNG', confidence = 0.75)
    if pic2 != None:
        print("Pic found!")
        pic2 = pyA.center(pic2)
        pic2X, pic2Y = pic2
        time.sleep(1)
        pyA.click(pic2X, pic2Y) 
        pyA.mouseDown()
        pyA.mouseUp()
    elif pic22 != None:
        print("Pic found!")
        pic22 = pyA.center(pic22)
        pic22X, pic22Y = pic22
        time.sleep(1)
        pyA.click(pic22X, pic22Y) 
        pyA.mouseDown()
        pyA.mouseUp()
    else:
        print("Did not find play button")
        return

    time.sleep(3)


    pic3 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/teamfighttab.PNG', confidence = 0.75)
    if pic3 != None:
        print("Pic found!")
        pic3 = pyA.center(pic3)
        pic3X, pic3Y = pic3
        time.sleep(1)
        pyA.click(pic3X, pic3Y)
        pyA.mouseDown()
        pyA.mouseUp() 
    else:
        print("Did not find team fight tab")
        return

    time.sleep(3)

    pic4 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/confirmbutton.PNG', confidence = 0.75)
    if pic4 != None:
        print("Pic found!")
        pic4 = pyA.center(pic4)
        pic4X, pic4Y = pic4
        time.sleep(1)
        pyA.click(pic4X, pic4Y) 
        pyA.mouseDown()
        pyA.mouseUp()
    else:
        print("Did not find the confirm button")
        return

    time.sleep(4)


    pic5 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/findMatchbutton.PNG', confidence = 0.75)
    if pic5 != None:
        print("Pic found!")
        pic5 = pyA.center(pic5)
        pic5X, pic5Y = pic5
        time.sleep(1)
        pyA.click(pic5X, pic5Y) 
        pyA.mouseDown()
        pyA.mouseUp()
    else:
        print("Did not find the find match button")
        return

    time.sleep(3)


    notinGame = True
    while notinGame:
        pic6 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/Accept2.PNG', confidence = 0.9)
        if pic6 != None:
            print("Pic found!")
            pic6 = pyA.center(pic6)
            pic6X, pic6Y = pic6
            time.sleep(1)
            pyA.click(pic6X, pic6Y) 
            pyA.mouseDown()
            pyA.mouseUp()
        else:
            print("Did not find the match accepted button. Trying again")

        time.sleep(3)
        #Check if I am in the match
        if (pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/TFTTab2.PNG', confidence = 0.75)) == None:
            notinGame = False
            print("i am now in game")

    
    print("end of getIntofirstgame script")
    print(datetime.now())
    

def surrender():
    time.sleep(3)
    pyA.hotkey('esc')
    s1 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/surrenderButton.PNG', confidence = 0.75)
    if s1 != None:
        print("Pic found!")
        s1 = pyA.center(s1)
        s1X, s1Y = s1
        time.sleep(1)
        pyA.click(s1X, s1Y)
        pyA.click(s1X, s1Y) 
        pyA.mouseDown()
        pyA.mouseUp()

    else:
        print("Did not find the surrender1 button")
        return

    time.sleep(3)


    s2 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/surrender2Button.PNG', confidence = 0.75)
    if s2 != None:
        print("Pic found!")
        s2 = pyA.center(s2)
        s2X, s2Y = s2
        time.sleep(1)
        pyA.click(s2X, s2Y) 
        pyA.click(s2X, s2Y) 
        pyA.mouseDown()
        pyA.mouseUp()

    else:
        print("Did not find the surrender2 button")
        return

    time.sleep(2)

def exitGame():
    time.sleep(3)
    ex = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/exitButton.PNG', confidence = 0.75)
    if ex != None:
        print("Pic found!")
        ex = pyA.center(ex)
        exX, exY = ex
        time.sleep(1)
        pyA.click(exX, exY)  #this click does not work and does not take me out of the game 
        pyA.click(exX, exY) #double clicking does not work either
        pyA.mouseDown()
        pyA.mouseUp()
        print('exit now button clicked')
        print(datetime.now())
        return 10

    else:
        print("Did not find the exit button")
        print(datetime.now())
        if pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/gameIsOver.PNG') != None:
            print("I proabbly got first becaues the game exited by itself lol!")
            print(datetime.now())
            return 10
        elif pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/okButt.PNG') != None:
            print("I proabbly got first becaues the game exited by itself lol!")
            print(datetime.now())
            return 10
        elif pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/playagainbutton.PNG') != None:
            print("I proabbly got first or second becaues the game exited by itself lol!")
            print(datetime.now())
            return 10
        else:
            return 2

def reEnter():

    okButton = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/okButt.PNG', confidence = 0.75)
    if okButton != None:
        okButton = pyA.center(okButton)
        okButtonX, okButtonY = okButton
        time.sleep(1)
        pyA.click(okButtonX, okButtonY) 
        pyA.mouseDown()
        pyA.mouseUp()
        print('finished quest ok button clicked')
        print(datetime.now())

    time.sleep(3)

    okButton = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/okButt.PNG', confidence = 0.75)
    if okButton != None:
        okButton = pyA.center(okButton)
        okButtonX, okButtonY = okButton
        time.sleep(1)
        pyA.click(okButtonX, okButtonY) 
        pyA.mouseDown()
        pyA.mouseUp()
        print('finished quest ok button clicked')
        print(datetime.now())

    time.sleep(3)

    

    okButton = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/okButt.PNG', confidence = 0.75)
    if okButton != None:
        okButton = pyA.center(okButton)
        okButtonX, okButtonY = okButton
        time.sleep(1)
        pyA.click(okButtonX, okButtonY) 
        pyA.mouseDown()
        pyA.mouseUp()
        print('finished quest ok button clicked')
        print(datetime.now())
    
    time.sleep(3)

    okButton = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/okButt.PNG', confidence = 0.75)
    if okButton != None:
        okButton = pyA.center(okButton)
        okButtonX, okButtonY = okButton
        time.sleep(1)
        pyA.click(okButtonX, okButtonY) 
        pyA.mouseDown()
        pyA.mouseUp()
        print('finished quest ok button clicked')
        print(datetime.now())
        
    time.sleep(3)

    okButton = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/okButt.PNG', confidence = 0.75)
    if okButton != None:
        okButton = pyA.center(okButton)
        okButtonX, okButtonY = okButton
        time.sleep(1)
        pyA.click(okButtonX, okButtonY) 
        pyA.mouseDown()
        pyA.mouseUp()
        print('finished quest ok button clicked')
        print(datetime.now())
    
    time.sleep(4)


    playAgain = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/playagainbutton.PNG', confidence = 0.75)
    if playAgain != None:
        print("Pic found!")
        playAgain = pyA.center(playAgain)
        playAgainX, playAgainY = playAgain
        time.sleep(1)
        pyA.click(playAgainX, playAgainY) 
        pyA.mouseDown()
        pyA.mouseUp()
        print('playagain button clicked')
        print(datetime.now())
    else:
        print("Did not find the play again button")
        print(datetime.now())
        return

    time.sleep(4)

    
    pic5 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/findMatchbutton.PNG', confidence = 0.75)
    if pic5 != None:
        pic5 = pyA.center(pic5)
        pic5X, pic5Y = pic5
        time.sleep(1)
        pyA.click(pic5X, pic5Y) 
        pyA.mouseDown()
        pyA.mouseUp()
        print('found the re find match button for next game')
        print(datetime.now())
    else:
        print("Did not find the re-find match button")
        print(datetime.now())
        return 6

    time.sleep(3)


    notinGame = True
    while notinGame:
        pic6 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/Accept2.PNG', confidence = 0.9)
        if pic6 != None:
            pic6 = pyA.center(pic6)
            pic6X, pic6Y = pic6
            time.sleep(1)
            pyA.click(pic6X, pic6Y)
            pyA.mouseDown()
            pyA.mouseUp() 
            print('found the match accepted button for the next match')
            print(datetime.now())
        else:
            print("Did not find the match accepted button. Trying again")
            print(datetime.now())

        time.sleep(3)
        #Check if I am in the match
        if (pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/TFTTab2.PNG', confidence = 0.75)) == None:
            notinGame = False
            print("i am now in game")
            print(datetime.now())

    
    print("re enter script done")
    print(datetime.now())



def positionChecker():
    pos = pyA.position()
    return pos

def reset():
    pass

def placeDownChamps():
    notinGame = True
    while notinGame:
        time.sleep(6)
        re = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/refresh.PNG', confidence = 0.9)
        if re != None:
            print('match has finished loading and I am now in planning phase')
            print(datetime.now())
            notinGame = False
        else:
            print("Match still loading screen, refresh not found")
        
        
    dragChamp()
    print('hopefully those champs were dragged in')

def placeDownChamps2():
    notinGame = True
    while notinGame:
        time.sleep(6)
        re = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/refresh.PNG', confidence = 0.9)
        if re != None:
            print('match has finished loading and I am now in planning phase')
            print(datetime.now())
            notinGame = False
        else:
            print("planning phase not found for dragging champs 2")
        
        
    dragChamp2()
    print('hopefully those champs were dragged in')


def buyXP():
    notinGame = True
    while notinGame:
        time.sleep(6)
        re = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/buyXP.PNG', confidence = 0.9)
        if re != None:
            dragChamp2()
            re = pyA.center(re)
            reX, reY = re
            time.sleep(1)
            pyA.click(reX, reY)
            print('buying xp now')
            print(datetime.now())
            x = 0
            while x < 20:
                pyA.mouseDown()
                time.sleep(0.2)
                pyA.mouseUp()
                x+=1
                #time.sleep(0.25)
            notinGame = False
            
        else:
            print("xp not found (planning phase not found)")
        
def buyXP2():
    notinGame = True
    while notinGame:
        time.sleep(6)
        #lvl5 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/lvl5.PNG', confidence = 0.9)
        re = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/buyXP.PNG', confidence = 0.9)
        if re != None:
            re = pyA.center(re)
            reX, reY = re
            time.sleep(1)
            pyA.click(reX, reY)
            print('buying xp now')
            print(datetime.now())
            x = 0
            while x < 14:
                pyA.mouseDown()
                time.sleep(0.2)
                pyA.mouseUp()
                if (x % 3 == 0):
                    lvl7 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/lvl7.PNG', confidence = 0.9)
                    if lvl7 != None:
                        x = 100
                x+=1
                #time.sleep(0.25)
                
            notinGame = False
        else:
            print("xp not found (planning phase not found)")    
    dragGoodChamp()

def dragGoodChamp():
    checking = True
    while checking:
        re = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/refresh.PNG', confidence = 0.9)
        g1 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/4Champ.PNG', confidence = 0.9)
        g2 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/bigChamp.PNG', confidence = 0.8)
        g3 = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/5champ.PNG', confidence = 0.8)
        if g3 != None:
            g3 = pyA.center(g3)
            g3X, g3Y = g3
            pyA.click(g3X, g3Y)
            pyA.mouseDown()
            time.sleep(0.2)
            pyA.mouseUp()
        if g2 != None:
            g2 = pyA.center(g2)
            g2X, g2Y = g2
            pyA.click(g2X, g2Y)
            pyA.mouseDown()
            time.sleep(0.2)
            pyA.mouseUp()
        if g1 != None:
            g1 = pyA.center(g1)
            g1X, g1Y = g1
            pyA.click(g1X, g1Y)
            pyA.mouseDown()
            time.sleep(0.2)
            pyA.mouseUp()
        elif re != None:
            re = pyA.center(re)
            reX, reY = re
            pyA.click(reX, reY)
            pyA.mouseDown()
            time.sleep(0.2)
            pyA.mouseUp()
            time.sleep(1)
        else:
            checking = False
        


def dragChamp():
    x1 = 573
    y = 1003
    x2 = 828

    x11 = 423
    x22 = 547
    yy = 782
    pyA.mouseDown(x1,y)
    time.sleep(0.5)
    pyA.mouseUp(x1,y)
    time.sleep(1)
    pyA.mouseDown(x2,y)
    time.sleep(0.5)
    pyA.mouseUp(x2,y)
    time.sleep(1)

    '''
    pyA.mouseDown(x11,yy)
    time.sleep(0.5)
    pyA.moveTo(700,600,1)
    time.sleep(0.5)
    pyA.mouseUp()
    time.sleep(1)
    pyA.mouseDown(x22,yy)
    time.sleep(0.5)
    pyA.moveTo(780,600,1)
    time.sleep(0.5)
    pyA.mouseUp()
    time.sleep(1) '''


def dragChamp2():
    x1 = 573
    y = 1003
    x2 = 1000

    x11 = 423
    x22 = 547
    yy = 782
    pyA.mouseDown(x1,y)
    time.sleep(0.5)
    pyA.mouseUp(x1,y)
    time.sleep(1)
    pyA.mouseDown(x2,y)
    time.sleep(0.5)
    pyA.mouseUp(x2,y)
    time.sleep(1)

    '''
    pyA.mouseDown(x11,yy)
    time.sleep(0.5)
    pyA.moveTo(700,600,1)
    time.sleep(0.5)
    pyA.mouseUp()
    time.sleep(1)
    pyA.mouseDown(x22,yy)
    time.sleep(0.5)
    pyA.moveTo(780,600,1)
    time.sleep(0.5)
    pyA.mouseUp()
    time.sleep(1) '''


def inGame():
    inGame = True
    while inGame:
        planning = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/planningphase2.PNG', confidence = 0.7)
        if planning != None:
            cultist = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/cultist.PNG', confidence = 0.7)
            keeper = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/keeper.PNG', confidence = 0.7)
            if cultist != None: 
                cultist = pyA.center(cultist)
                cultistX, cultistY = cultist
                time.sleep(1)
                pyA.click(cultistX, cultistY)
                pyA.mouseDown()
                pyA.mouseUp() 
            elif keeper != None:
                keeper = pyA.center(keeper)
                keeperX, keeperY = keeper
                time.sleep(1)
                pyA.click(keeperX, keeperY)
                pyA.mouseDown()
                pyA.mouseUp() 
            else: 
                buyXP = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/buyXP.PNG', confidence = 0.9)
                if buyXP != None: 
                    buyXP = pyA.center(buyXP)
                    buyXPX, buyXPY = buyXP
                    time.sleep(1)
                    pyA.click(buyXPX, buyXPY)
                    pyA.mouseDown()
                    pyA.mouseUp() 
                refresh = pyA.locateOnScreen('/Users/edmon/Desktop/League/tftBot/refresh.PNG', confidence = 0.9)
                if refresh != None: 
                    refresh = pyA.center(refresh)
                    refreshX, refreshY = refresh
                    time.sleep(1)
                    pyA.click(refreshX, refreshY)
                    pyA.mouseDown()
                    pyA.mouseUp() 
        








def main():
    getIntoFirstGame()
    keepGoing = True
    while keepGoing:
        time.sleep(1000)
        surrender()
        exitGame()
        reEnter()



def main2():
    getIntoFirstGame()
    keepGoing = True
    while keepGoing:
        time.sleep(600)
        print(" 5 min left ")
        time.sleep(120)
        print('3 minute left')
        time.sleep(120)
        print('One minute left')
        time.sleep(60)
        x = 3
        while x < 5:
            time.sleep(20)
            x = exitGame()
            print(x)
        print('recognized game finished!')
        time.sleep(7)
        if reEnter() == 6:
            print('program is stopping')
            break
def main25():
    getIntoFirstGame()
    keepGoing = True
    while keepGoing:
        placeDownChamps()
        time.sleep(240)
        #placeDownChamps()
        time.sleep(180)
        print(" 5 min left ")
        time.sleep(120)
        print('3 minute left')
        time.sleep(120)
        print('One minute left')
        time.sleep(60)
        x = 3
        while x < 5:
            time.sleep(20)
            x = exitGame()
            print(x)
        print('recognized game finished!')
        time.sleep(7)
        if reEnter() == 6:
            print('program is stopping')
            break
def main3():
    getIntoFirstGame()
    keepGoing = True
    while keepGoing:
        placeDownChamps()
        time.sleep(240)
        #placeDownChamps()
        time.sleep(180)
        print(" 5 min left ")
        time.sleep(120)
        print('3 minute left')
        buyXP()
        time.sleep(120)
        print('One minute left')
        time.sleep(60)
        x = 3
        while x < 5:
            time.sleep(20)
            x = exitGame()
            print(x)
        print('recognized game finished!')
        time.sleep(7)
        if reEnter() == 6:
            print('program is stopping')
            break

def main4():
    getIntoFirstGame()
    keepGoing = True
    while keepGoing:
        #placeDownChamps()
        time.sleep(240) #4
        #placeDownChamps()
        time.sleep(180)#3
        print("4 min left before buyxp")
        time.sleep(120)#2
        print('2 minute left before buyxp')
        time.sleep(120)#2
        time.sleep(180)#3
        buyXP2()
        time.sleep(300)#5
        print('1 min left')
        time.sleep(60)#1
        x = 3
        while x < 5:
            time.sleep(20)
            x = exitGame()
            print(x)
        print('recognized game finished!')
        time.sleep(7)
        if reEnter() == 6:
            print('program is stopping')
            break
    
def main5():
    buyXP2()

#main()
#main2()
#main3()
main4()
#main5()