import cv2
import numpy as np

img1=cv2.imread('3D-Matplotlib.png')
img2=cv2.imread('mainsvmimage.png')

add=img1+img2
add2=cv2.add(img1,img2) #added all the pixel values
add3=cv2.addWeighted(img1,0.4,img2,0.6,0)

cv2.imshow('add1',add)
cv2.imshow('add2',add2)
cv2.imshow('add3',add3)
cv2.waitKey(0)
cv2.destroyAllWindows()