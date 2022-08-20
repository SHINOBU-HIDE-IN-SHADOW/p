import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab
import pyautogui
import time
import keyboard
run = True
class macroclass:
    def __init__(self,images):
        sift = cv2.xfeatures2d.SIFT_create()        
        kp1, des1 = sift.detectAndCompute(images,None)
        kp2, des2 = sift.detectAndCompute(wind,None)        
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1,des2, k=2)
        match_pts_screen = []
        for m1, m2 in matches:
                if m1.distance < 0.35*m2.distance:
                        idx = m1.trainIdx
                        match_pts_screen.append(kp2[idx].pt)
                
        if len(match_pts_screen) != 0:
                match_pts_screen = np.array(match_pts_screen)
                pyautogui.moveTo(match_pts_screen[0, 0]+20, match_pts_screen[0, 1]+2, 1)
                pyautogui.click(button = "left")
                time.sleep(0.5)
                match_pts_screen = 0
                
while run:
        #pyautogui fail safe
        pyautogui.PAUSE = 0.1
        #end program
        if keyboard.is_pressed("k"): 
                break
        screen_result = pyautogui.size()
        wind = np.array(ImageGrab.grab(bbox=(0,0,screen_result[0],screen_result[1])))
        wind = cv2.cvtColor(wind, cv2.COLOR_RGB2GRAY)
        hero_power = cv2.imread('D:\\Users\\lobot\Desktop\\pyprojects\\macro test\\shield.JPG', 0)
        game_start = cv2.imread('D:\\Users\\lobot\\Desktop\\pyprojects\\macro test\\start.JPG', 0)
        hero = cv2.imread('D:\\Users\\lobot\\Desktop\\pyprojects\\macro test\\warriiorh.JPG', 0)
        defeat = cv2.imread('D:\\Users\\lobot\\Desktop\\pyprojects\\macro test\\warriiorh.JPG', 0)
        ctc = cv2.imread('D:\\Users\\lobot\\Desktop\\pyprojects\\macro test\\Capture1.png', 0)
        macroclass(hero_power)
        macroclass(game_start)
        macroclass(hero)
        macroclass(ctc)
            
cv2.destroyAllWindows()
