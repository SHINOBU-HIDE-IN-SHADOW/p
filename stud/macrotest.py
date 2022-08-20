import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab
import pyautogui
import time
import keyboard
run = True

while run:
        #pyautogui fail safe
        pyautogui.PAUSE = 0.1
        #end program
        if keyboard.is_pressed("k"): 
                break
        wind = np.array(ImageGrab.grab(bbox=(0,0,1365,767)))
        wind = cv2.cvtColor(wind, cv2.COLOR_RGB2GRAY)
        hero_power = cv2.imread('D:\\Users\\lobot\Desktop\\pyprojects\\macro test\\shield.JPG', 0)
        game_start = cv2.imread('D:\\Users\\lobot\\Desktop\\pyprojects\\macro test\\start.JPG', 0)
        card_warrior = cv2.imread('D:\\Users\\lobot\\Desktop\\pyprojects\\macro test\\minionw.PNG', 0)
        card_all = cv2.imread('D:\\Users\\lobot\\Desktop\\pyprojects\\macro test\\minionwil.PNG', 0)
        hero = cv2.imread('D:\\Users\\lobot\\Desktop\\pyprojects\\macro test\\warriiorh.JPG', 0
                
        #card player
        sift = cv2.xfeatures2d.SIFT_create() 
        kp_wcard1, des_wcard1 = sift.detectAndCompute(card_warrior,None)
        kp_wcard2, des_wcard2 = sift.detectAndCompute(wind,None)
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks=50)   # or pass empty dictionary
        flann = cv2.FlannBasedMatcher(index_params,search_params)
        matches = flann.knnMatch(des_wcard1,des_wcard2,k=2)

        matchesMask = [[0,0] for i in range(len(matches))]
        # ratio test as per Lowe's paper
        for i,(m,n) in enumerate(matches):
                if m1.distance < 0.4*m2.distance:
                        idx = m1.trainIdx
                        matchesMask.append(kp_wcard2[idx].pt)
                
        if len(match_pts_wcard) != 0:
                match_pts_wcard = np.array(match_pts_wcard)
                pyautogui.click(match_pts_wcard[0, 0], match_pts_wcard[0, 1], button = "left") 
                pyautogui.dragTo(match_pts_wcard[0, 0], match_pts_wcard[0, 1]-450, button = "left") 
        
cv2.destroyAllWindows()
