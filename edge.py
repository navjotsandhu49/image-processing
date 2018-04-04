import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()

    edge=cv2.Canny(frame,100,100) # change parameters to increase the noise
    lap=cv2.Laplacian(frame,cv2.CV_64F) # can be used to make edge detectors

    cv2.imshow('real',frame)
    cv2.imshow('edge',edge)
    cv2.imshow('lap',lap)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
