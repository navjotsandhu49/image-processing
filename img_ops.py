import cv2
import numpy as np

img =cv2.imread('img1.JPG',1)
px=img[23,200]

roi=img[100:150,100:150] #region of image
img[0:50,0:50]=roi #paste a region of image to another region
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(roi)