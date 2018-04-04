import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')#to save the video
out=cv2.VideoWriter('out.avi',fourcc,20.0,(640,480))#to save the video
while True:
    ret,frame=cap.read()
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.rectangle(frame,(50,50),(150,150),(150,0,130),2)
    out.write(frame)#to save the video
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release() #to save the video
cv2.destroyAllWindows()