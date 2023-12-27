import cv2
import os
import volumectrl as vol
import HandTrackingModule1 as hand
import time
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 5)
w , h = 640, 480

cam.set(3,w)
cam.set(4,h)
detect = hand.handDetector(detectionCon = 0.75)
tipIds = [4,8,12,16,20]
totalFingers =0
while True:
    
    success, image = cam.read()
    image = detect.findHands(image) 
    lmList = detect.findPosition(image, draw=False)
    #print(lmList)
    #cv2.imshow("Image",image)
    cv2.waitKey(1)
    if len(lmList) != 0:
        fingers = []
        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
 
        # 4 Fingers
        
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        counts  = fingers.count(1)
        # print(fingers)
        if(totalFingers != counts  ):
            totalFingers = counts
            if(counts !=0 ):
                print(totalFingers)
        else:
             continue
    