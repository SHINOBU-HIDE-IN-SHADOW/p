from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab
import pyautogui
import time
import keyboard
run = True

Builder.load_file("kivrmac.kv")

pyautogui.PAUSE = 0.1

screen_result = pyautogui.size()
wind = np.array(ImageGrab.grab(bbox=(0,0,screen_result[0],screen_result[1])))
wind = cv2.cvtColor(wind, cv2.COLOR_RGB2GRAY)
hero_power = cv2.imread('D:\\Users\\lobot\Desktop\\pyprojects\\macro test\\shield.JPG', 0)
game_start = cv2.imread('D:\\Users\\lobot\\Desktop\\pyprojects\\macro test\\start.JPG', 0)
hero = cv2.imread('D:\\Users\\lobot\\Desktop\\pyprojects\\macro test\\warriiorh.JPG', 0)
defeat = cv2.imread('D:\\Users\\lobot\Desktop\\pyprojects\\macro test\\shield.JPG', 0)

class macroclass:
    def __init__(self,images):
        sift = cv2.xfeatures2d.SIFT_create()        
        kp1, des1 = sift.detectAndCompute(images,None)
        kp2, des2 = sift.detectAndCompute(wind,None)        
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1,des2, k=2)
        match_pts_screen = []
        for m1, m2 in matches:
                if m1.distance < 0.3*m2.distance:
                        idx = m1.trainIdx
                        match_pts_screen.append(kp2[idx].pt)
                
        if len(match_pts_screen) != 0:
                match_pts_screen = np.array(match_pts_screen)
                pyautogui.click(match_pts_screen[0, 0]+20, match_pts_screen[0, 1]+2, button = "left")
                time.sleep(0.7)
                pyautogui.click()

class MyLayout(Widget):

    def press(self):
        
       while run:
            macroclass(hero_power)
            macroclass(game_start)
            macroclass(hero)
            pyautogui.click()

    def end(self):
           cv2.destroyAllWindows()
           
            
cv2.destroyAllWindows()

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()