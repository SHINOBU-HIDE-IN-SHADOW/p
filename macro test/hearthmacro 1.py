import pyautogui
import keyboard
import time
a = pyautogui.locateCenterOnScreen("D:\\Users\\lobot\\Desktop\\pygame projects\\pyautoui macro test\\MODECHOOSE.JPG",confidence= 0.7)
b = pyautogui.locateCenterOnScreen("D:\\Users\\lobot\\Desktop\\pygame projects\\pyautoui macro test\\shield.JPG" ,confidence= 0.5)
c = pyautogui.locateCenterOnScreen("D:\\Users\\lobot\\Desktop\\pygame projects\\pyautoui macro test\\start.JPG" ,confidence= 0.7)
def gamestart():
    pyautogui.moveTo(c)
    pyautogui.moveTo(b)
    time.sleep(0.5)
def heropower():
    pyautogui.click()
    time.sleep(2)
run = True
def event():
    while run:
        if keyboard.is_pressed("k"):
            break 
        pyautogui.PAUSE = 0.5
        gamestart()
        heropower()
        if pyautogui.click(c):
            break
        if pyautogui.click(c):
            break
event()
