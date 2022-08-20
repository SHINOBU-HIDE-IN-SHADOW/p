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
        pyautogui.PAUSE = 0.5
        #end program
        if keyboard.is_pressed("k"): 
                break
        wind = np.array(ImageGrab.grab(bbox=(0,0,1365,767)))
        wind = cv2.cvtColor(wind, cv2.COLOR_RGB2GRAY)
        hero_power = cv2.imread('D:\\Users\\lobot\Desktop\\pyprojects\\macro test\\shield.JPG', 0)
        game_start = cv2.imread('D:\\Users\\lobot\\Desktop\\pyprojects\\macro test\\start.JPG', 0)
        card_warrior = cv2.imread('D:\\Users\\lobot\\Desktop\\pyprojects\\macro test\\minionw.JPG', 0)
        card_all = cv2.imread('D:\\Users\\lobot\\Desktop\\pyprojects\\macro test\\minionwil.JPG', 0)

        #hero power
        sift = cv2.xfeatures2d.SIFT_create()        
        kp_hpower1, des_hpower1 = sift.detectAndCompute(hero_power,None)
        kp_hpower2, des_hpower2 = sift.detectAndCompute(wind,None)        
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des_hpower1,des_hpower2, k=2)
        match_pts_hpower = []
        for m1, m2 in matches:
                if m1.distance < 0.3*m2.distance:
                        idx = m1.trainIdx
                        match_pts_hpower.append(kp_hpower2[idx].pt)
                
        if len(match_pts_hpower) != 0:
                match_pts_hpower = np.array(match_pts_hpower)
                pyautogui.click(match_pts_hpower[0, 0], match_pts_hpower[0, 1], button = "left")
                time.sleep(2)
        else:
                time.sleep(0.5)

        #gmae start
        sift2 = cv2.xfeatures2d.SIFT_create()        
        kp_gstart1, des_gstart1 = sift2.detectAndCompute(game_start,None)
        kp_gstart2, des_gstart2 = sift2.detectAndCompute(wind,None)        
        bf2 = cv2.BFMatcher()
        matches2 = bf.knnMatch(des_gstart1,des_gstart2, k=2)
        match_pts_gstart = []
        for m1, m2 in matches2:
                if m1.distance < 0.3*m2.distance:
                        idx = m1.trainIdx
                        match_pts_gstart.append(kp_gstart2[idx].pt)
                
        if len(match_pts_gstart) != 0:
                match_pts_gstart = np.array(match_pts_gstart)
                pyautogui.click(match_pts_gstart[0, 0], match_pts_gstart[0, 1], button = "left")
                

        #card player
        sift2 = cv2.xfeatures2d.SIFT_create()        
        kp_wcard1, des_wcard1 = sift2.detectAndCompute(card_warrior,None)
        kp_wcard2, des_wcard2 = sift2.detectAndCompute(wind,None)        
        bf2 = cv2.BFMatcher()
        matches2 = bf.knnMatch(des_wcard1,des_wcard2, k=2)
        match_pts_wcard = []
        for m1, m2 in matches2:
                if m1.distance < 0.75*m2.distance:
                        idx = m1.trainIdx
                        match_pts_wcard.append(kp_wcard2[idx].pt)
                
        if len(match_pts_wcard) != 0:
                match_pts_wcard = np.array(match_pts_wcard)
                pyautogui.dragTo(match_pts_wcard[0, 0], match_pts_wcard[0, 1]-900, button = "left") 

        #p;ay card all
        sift2 = cv2.xfeatures2d.SIFT_create()        
        kp_cardall1, des_cardall1 = sift2.detectAndCompute(card_all,None)
        kp_cardall2, des_cardall2 = sift2.detectAndCompute(wind,None)        
        bf2 = cv2.BFMatcher()
        matches2 = bf.knnMatch(des_cardall1,des_cardall2, k=2)
        match_pts_cardall = []
        for m1, m2 in matches2:
                if m1.distance < 0.75*m2.distance:
                        idx = m1.trainIdx
                        match_pts_cardall.append(kp_cardall2[idx].pt)
                
        if len(match_pts_cardall) != 0:
                match_pts_cardall = np.array(match_pts_cardall)
                pyautogui.dragTo(match_pts_cardall[0, 0], match_pts_cardall[0, 1]-900, button = "left") 
     
        pyautogui.click()       


cv2.destroyAllWindows()
