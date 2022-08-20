import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab
import pyautogui
import time

run = True
while run:
    wind = np.array(ImageGrab.grab(bbox=(0,0,1365,767)))
    wind = cv2.cvtColor(wind, cv2.COLOR_RGB2GRAY)
    game_start = cv2.imread('D:\\Users\\lobot\\Desktop\\pyprojects\\macro test\\start.JPG', 0)
    sift2 = cv2.xfeatures2d.SIFT_create()        
    kp_gstart1, des_gstart1 = sift2.detectAndCompute(game_start,None)
    kp_gstart2, des_gstart2 = sift2.detectAndCompute(wind,None)        
    bf2 = cv2.BFMatcher()
    matches2 = bf2.knnMatch(des_gstart1,des_gstart2, k=2)
    match_pts_gstart = []
    for m1, m2 in matches2:
            if m1.distance < 0.3*m2.distance:
                idx = m1.trainIdx
                match_pts_gstart.append(kp_gstart2[idx].pt)
          
    if len(match_pts_gstart) != 0:
            match_pts_gstart = np.array(match_pts_gstart)
            pyautogui.click(match_pts_gstart[0, 0]+18, match_pts_gstart[0, 1], button = "left")