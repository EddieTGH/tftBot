import pyautogui as pyA
import time
import cv2
from datetime import datetime
from twilio.rest import Client
import os
 
 
def getIntoFirstGame():
    time.sleep(3)
 
    pic1 = pyA.locateOnScreen('vImages/playButton.PNG', confidence = 0.75)
    if pic1 != None:
        pic1 = pyA.center(pic1)
        pic1X, pic1Y = pic1
        time.sleep(1)
        pyA.moveTo(pic1X, pic1Y) 
        time.sleep(1)
        pyA.click(pic1X, pic1Y) 
        pyA.click(pic1X, pic1Y) 
        
 
        
    else:
        return
 
    time.sleep(3)
 
    
    pic2 = pyA.locateOnScreen('vImages/death1.PNG', confidence = 0.75)
    if pic2 != None:
       #print("Pic found!")
        pic2 = pyA.center(pic2)
        pic2X, pic2Y = pic2
        time.sleep(1)
        pyA.moveTo(pic2X, pic2Y)
        time.sleep(1)
        pyA.click(pic2X, pic2Y)
        pyA.click(pic2X, pic2Y)
    
    else:
        return
 
    time.sleep(3)
 
 
    pic3 = pyA.locateOnScreen('vImages/start.PNG', confidence = 0.75)
    if pic3 != None:
       #print("Pic found!")
        pic3 = pyA.center(pic3)
        pic3X, pic3Y = pic3
        time.sleep(1)
        pyA.moveTo(pic3X, pic3Y)
        time.sleep(1)
        pyA.click(pic3X, pic3Y)
        pyA.click(pic3X, pic3Y)
 
    

    else:
        return
 
 
def checkInGame():
 
    loop = True
 
    while loop:
        time.sleep(3)
        pic4 = pyA.locateOnScreen('vImages/career.PNG', confidence = 0.75)
        if pic4  == None:
            print("in game!")
            loop = False
        else: 
            print('still in the lobby yet')
            
        
 
def altTab():
    time.sleep(1)
    pyA.hotkey('alt', 'tab')  
    time.sleep(1)
    pyA.click(700,400)
    time.sleep(2)
    
def move():
    time.sleep(2)
    pyA.click(400,400)
    pyA.keyDown('w')
    time.sleep(2)
    pyA.keyUp('w')
    pyA.keyDown('d')
    time.sleep(2)
    pyA.keyUp('d')
    pyA.keyDown('a')
    time.sleep(2)
    pyA.keyUp('a')
    
def inGameandJoinNext():
    time.sleep(2)
    altTab()
    print("should be back in vs code")
    for i in range (0,8):
        time.sleep(45)
        print('about to commence movement and check if game done')
        altTab()
        time.sleep(15)
        pic4 = pyA.locateOnScreen('vImages/playAgain.PNG', confidence = 0.65)
        pic5 = pyA.locateOnScreen('vImages/skipbutton.PNG', confidence = 0.75)
        pic6 = pyA.locateOnScreen('vImages/skipbutton1.PNG', confidence = 0.75)
        if pic4 != None or pic5 != None or pic6 != None:
            altTab()
            print('exited early')
            break                                                                                                                                        
        else:
            move()
        altTab()
        
        print('movement done')
            
    altTab()
    if pic6 != None:
        pic6 = pyA.center(pic6)
        pic6X, pic6Y = pic6
        time.sleep(1)
        pyA.moveTo(pic6X, pic6Y)
        time.sleep(1)
        pyA.click(pic6X, pic6Y)
        pyA.click(pic6X, pic6Y)
        print('clicked the skip button')
        loop = False

 
    loop = True
    print('movement is DONE. checking if game is done')
    while loop:
        pic5 = pyA.locateOnScreen('vImages/skipButton1.PNG', confidence = 0.75)
        if pic5 != None:
            pic5 = pyA.center(pic5)
            pic5X, pic5Y = pic5
            time.sleep(1)
            pyA.moveTo(pic5X, pic5Y)
            time.sleep(1)
            pyA.click(pic5X, pic5Y)
            pyA.click(pic5X, pic5Y)
            print('going into next game')
            time.sleep(3)

        pic4 = pyA.locateOnScreen('vImages/playAgain.PNG', confidence = 0.75)
        if pic4 != None:
            time.sleep(2)
            pyA.hotkey('win', 'prntscrn')
            time.sleep(2)
            pic4 = pyA.center(pic4)
            pic4X, pic4Y = pic4
            time.sleep(1)
            pyA.moveTo(pic4X, pic4Y)
            time.sleep(1)
            pyA.click(pic4X, pic4Y)
            pyA.click(pic4X, pic4Y)
            print('going into next game')
            loop = False
 
def inGameandJoinNext2():
    
    altTab()
    
    time.sleep(420) #7 mins
    print('about to commence movement')
    altTab()
    time.sleep(8)
    while True:
        pic4 = pyA.locateOnScreen('vImages/playAgain.PNG', confidence = 0.65)
        pic5 = pyA.locateOnScreen('vImages/skipbutton.PNG', confidence = 0.75)
        pic6 = pyA.locateOnScreen('vImages/skipbutton1.PNG', confidence = 0.75)
        if pic4 != None or pic5 != None or pic6 != None:
            print('exited early')
            break                                                                                                                                        
        else:
            move()
            time.sleep(10)
            
    print('game is done')
            
    if pic6 != None:
        pic6 = pyA.center(pic6)
        pic6X, pic6Y = pic6
        time.sleep(1)
        pyA.moveTo(pic6X, pic6Y)
        time.sleep(1)
        pyA.click(pic6X, pic6Y)
        pyA.click(pic6X, pic6Y)
        print('clicked the skip button')
        loop = False

 
    loop = True
    print('movement is DONE. checking if game is done')
    while loop:
        pic5 = pyA.locateOnScreen('vImages/skipButton1.PNG', confidence = 0.75)
        if pic5 != None:
            pic5 = pyA.center(pic5)
            pic5X, pic5Y = pic5
            time.sleep(1)
            pyA.moveTo(pic5X, pic5Y)
            time.sleep(1)
            pyA.click(pic5X, pic5Y)
            pyA.click(pic5X, pic5Y)
            print('going into next game')
            time.sleep(3)

        pic4 = pyA.locateOnScreen('vImages/playAgain.PNG', confidence = 0.75)
        if pic4 != None:
            time.sleep(2)
            pyA.hotkey('win', 'prntscrn')
            time.sleep(2)
            pic4 = pyA.center(pic4)
            pic4X, pic4Y = pic4
            time.sleep(1)
            pyA.moveTo(pic4X, pic4Y)
            time.sleep(1)
            pyA.click(pic4X, pic4Y)
            pyA.click(pic4X, pic4Y)
            print('going into next game')
            loop = False
 


def main():
    getIntoFirstGame()
    while True:
        checkInGame()
        inGameandJoinNext2()
    
 
 
 
    
 
 
main()
 

