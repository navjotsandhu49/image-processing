import cv2
import numpy as np
c=False
#body_cascade=cv2.CascadeClassifier('haarcascade_fullbody.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)

while True:
    _,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # body=body_cascade.detectMultiScale(gray,1.3,5)
    # for (x,y,w,h) in body:
    #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        if faces.any():
            c=True
        else:
            c=False
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,23,0),2)
        roi_gray=gray[y:y+h,x:x+h]
        roi_color=img[y:y+h,x:x+h]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.3,5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 23, 255), 2)


    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
