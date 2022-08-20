import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab
import pyautogui
import time



start = time.time() #현재시간
while True:
    end = time.time() #현재시간
    if int(end - start) == 120:
        print("inif")
        start = end
        test = np.array(ImageGrab.grab(bbox=(16,62,1028,630)))#pillow으로 화면 이미지를 가져오고 array으로 위치저장
        test = cv2.cvtColor(test, cv2.COLOR_RGB2GRAY) #화면을 그레이로 cv2로 변경
        
        train_elix = cv2.imread('collect/elix.jpg', 0)#이미지 가져오기 1
        train_gold = cv2.imread('collect/gold.jpg', 0)#이미지 가져오기 2
        
        #############   elix collection ###################
        sift = cv2.xfeatures2d.SIFT_create() #cv2 sift알고이증 불러오기(특징점을 계산함)       
        kp_elix1, des_elix1 = sift.detectAndCompute(train_elix,None) #이미지를 발견하고 값을 산청함!
        kp_elix2, des_elix2 = sift.detectAndCompute(test,None)  #이미지를 발견하고 값을 산청함@
        bf = cv2.BFMatcher() #bfmatcher함수 불러오기
        matches = bf.knnMatch(des_elix1,des_elix2, k=2)#두값을 저장
        
        match_pts_elix = [] #set생성 (값받기)
        for m1, m2 in matches:
            if m1.distance < 0.65*m2.distance:#두값을 비교
                idx = m1.trainIdx#받은값을
                match_pts_elix.append(kp_elix2[idx].pt)#ser에 추가
          
        if len(match_pts_elix) != 0:#만약 set에 값이 있을경우
            match_pts_elix = np.array(match_pts_elix)#위치를 numpy로 저장
            pyautogui.click(match_pts_elix[0, 0]+16, match_pts_elix[0, 1]+62, button='left')#클릭
        
        else:
            print("sorry ! no elixers farmed yet")#아닐경우 출력
        
      ###   (x, y, 'left')  
        ################  gold collection #############################
        sift2 = cv2.xfeatures2d.SIFT_create()        
        kp_gold1, des_gold1 = sift2.detectAndCompute(train_gold,None)
        kp_gold2, des_gold2 = sift2.detectAndCompute(test,None)        
        bf2 = cv2.BFMatcher()
        matches2 = bf.knnMatch(des_gold1,des_gold2, k=2)
        
        match_pts_gold = []
        for m1, m2 in matches2:
            if m1.distance < 0.70*m2.distance:
                idx = m1.trainIdx
                match_pts_gold.append(kp_gold2[idx].pt)
          
        if len(match_pts_gold) != 0:
            match_pts_gold = np.array(match_pts_gold)
            pyautogui.click(match_pts_gold[0, 0]+16, match_pts_gold[0, 1]+62, button='left')
        
        else:
            print("sorry ! no gold farmed yet")
        
        if cv2.waitKey(1) == 27:#키를 입력받을 경우 정지
            break