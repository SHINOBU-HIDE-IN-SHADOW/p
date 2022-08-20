import pyautogui
import time
import keyboard
run = True
def event():  
  while run:
          if keyboard.is_pressed("k"):
            position_mouse = pyautogui.position()
            print (position_mouse)
            time.sleep(0.1)
          if keyboard.is_pressed("q"):
            break    
event()