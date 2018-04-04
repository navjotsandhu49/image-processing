import cv2
import numpy as np

cap= cv2.VideoCapture(0)

while True:
   _ , frame=cap.read()
   hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

   lower_red=np.array([150,150,50])# for filterting red color out of the background
   up_red=np.array([255,200,180]) # for filterting red color out of the background

   mask=cv2.inRange(hsv,lower_red,up_red)
   res=cv2.bitwise_and(frame,frame,mask=mask)

   #BLURRING
   kernal=np.ones((15,15),np.float32)/225
   smoothed=cv2.filter2D(res,-1,kernal)
   gaus=cv2.GaussianBlur(res,(15,15),0)
   median=cv2.medianBlur(res,15)                  #best
   bilateral=cv2.bilateralFilter(res,15,75,75)

   ker=np.ones((5,5),np.uint8)
   erosion=cv2.erode(mask,ker,iterations=1)
   dilation=cv2.dilate(mask,ker,iterations=1)

   opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,ker)
   close=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,ker)

   # cv2.imshow('frame',frame)
   # cv2.imshow('mask', mask)
   #cv2.imshow('smoothed',smoothed)
   #cv2.imshow('gaus', gaus)
   cv2.imshow('opening', opening)
   cv2.imshow('close', close)
   cv2.imshow('median', median)
   #cv2.imshow('bilateral', bilateral)
   cv2.imshow('res', res)

   if cv2.waitKey(1) & 0xFF==ord('q'):
       break

cv2.destroyAllWindows()
cap.release()
