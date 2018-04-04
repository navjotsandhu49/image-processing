import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('F:\mcam pics\img1.JPG',cv2.IMREAD_GRAYSCALE) # ('FILE_NAME,0)
img2=cv2.imread('F:\mcam pics\img1.JPG',1)
# IMREAD_COLOR =1
# IMREAD_UNCHANGED = -1

#DRAWING ON IMAGE
cv2.line(img2,(0,0),(120,120),(0,255,255),3)
cv2.rectangle(img2,(20,20),(100,100),(0,255,0),5)
cv2.circle(img2,(150,150),(100),(0,255,255),-1) # for filling in the circle

cv2.imshow('image',img)
cv2.imshow('image2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(img,cmap='gray',interpolation='bicubic')
# plt.plot([30,100],[50,50],'c',linewidth=2)
# plt.show()

# cv2.imwrite('file_name',img) to save an image
