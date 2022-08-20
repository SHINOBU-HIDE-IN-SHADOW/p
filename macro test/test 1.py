import pyautogui
import keyboard
i = True
while i:
    if keyboard.is_pressed('q'):
        pyautogui.screenshot("1.jpg", region=(1300,1300,500,500))
        pyautogui.screenshot("2.jpg", region=(500,600,300,500))
    if keyboard.is_pressed('k'):
        i = False
        break


