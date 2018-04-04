import cv2
import numpy as np

img=cv2.imread('bookpage.jpg')

ret,thresh=cv2.threshold(img,12,255,cv2.THRESH_BINARY)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gaus=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
#gaus2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.COLOR_BGR2GRAY,115,1)

cv2.imshow('img',img)
cv2.imshow('thresh',thresh)
cv2.imshow('gray',gray)
cv2.imshow('gaus',gaus)
#cv2.imshow('gaus2',gaus2)
cv2.waitKey(0)
cv2.destroyAllWindows()
