import pyautogui
import time
import random
import keyboard
run = True
def click_low():
    pyautogui.click(729,645)
def click_high():
    pyautogui.click(631,645)
while run:
    ranchoise = click_high,click_low
    choice = random.choice(ranchoise)()
    pyautogui.click(choice)
    time.sleep(2)
    click_low()
    time.sleep(2)
    click_low()
    click_low()
    time.sleep(2)
    click_high()
    click_low()
    time.sleep(2)
    click_high()
    time.sleep(2)
    if keyboard.is_pressed('q'):
        break