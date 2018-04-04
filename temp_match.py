import cv2
import numpy as np

img_bgr=cv2.imread('temp_img.jpg')
img_gr=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)

temp=cv2.imread('temp_match.jpg',0)
w,h=temp.shape[::-1]

res=cv2.matchTemplate(img_gr,temp,cv2.TM_CCOEFF_NORMED)
thresh=0.8
loc=np.where(res>=thresh)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)

cv2.imshow('detected',img_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()