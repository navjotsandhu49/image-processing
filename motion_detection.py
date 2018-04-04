import cv2
import numpy as np

cap=cv2.VideoCapture(0)
fgbg=cv2.createBackgroundSubtractorMOG2()

while True:
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    median = cv2.medianBlur(gray, 15)

    fgmask=fgbg.apply(gray)
    #fgmask=fgbg.apply(median)

    _,thresh = cv2.threshold(fgmask,12,255,cv2.THRESH_BINARY)

    _,contours,_=cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt = contours[max_index]

    x,y,w,h=cv2.boundingRect(cnt)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)
    # cv2.drawContours(frame,contours,-1,(255,0,255),1,)

    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
