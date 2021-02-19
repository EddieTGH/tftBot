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
        time.sleep(20)
        pic3 = pyA.locateOnScreen('vImages/gun2.PNG', confidence = 0.55)
        if pic3 != None:
            print("in game!")
            loop = False
        else:
            print("did not find gun")
            
        
 
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
    pyA.keyUp('w')
    
def inGameandJoinNext():
    
    altTab()
    for i in range (0,4):
        time.sleep(120)
        print('commence movement')
        altTab()
        pic4 = pyA.locateOnScreen('vImages/skipbutton.PNG', confidence = 0.75)
        if pic4 != None:
            altTab()
            break
        else:
            move()
        altTab()
        print('movement done')
    
    altTab()
 
    loop = True
 
    while loop:
        pic4 = pyA.locateOnScreen('vImages/playAgain.PNG', confidence = 0.75)
        if pic4 != None:
        #print("Pic found!")
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
        inGameandJoinNext()
    
 
 
def main2():
    for i in range(0,2):
        print('hi')
        break
        print('no')
 
 
main()
 

