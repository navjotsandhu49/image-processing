import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('opencv-feature-matching-image.jpg',0)
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

temp=cv2.imread('opencv-feature-matching-template.jpg',0)

orb=cv2.ORB_create()

kp1,des1 = orb.detectAndCompute(img,None)
kp2,des2 = orb.detectAndCompute(temp,None)

bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

matches=bf.match(des1,des2)
matches=sorted(matches,key=lambda x:x.distance) # sorting matches according to the distance

img2=cv2.drawMatches(img,kp1,temp,kp2,matches[:10],None,flags=2)
plt.imshow(img2)
plt.show()