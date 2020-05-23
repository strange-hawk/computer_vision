import cv2
import numpy as np

def capture(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier('../Haarcascades/haarcascade_frontalface_default.xml')
    faces = cascade.detectMultiScale(gray,1.3,5)
    return faces

def capture_eye(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cascade_eye = cv2.CascadeClassifier('../Haarcascades/haarcascade_eye.xml')
    eyes= cascade_eye.detectMultiScale(gray)
    return eyes

cap = cv2.VideoCapture(0)
while(True):
    res,frame = cap.read()
    faces = capture(frame)
    if faces is ():
        # print('no face')
        cv2.putText(frame,'no face',(450,50),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,245),3)
    else:
        for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,245),2)
            # cv2.putText(frame,'face found',(x+(w)//2,y+h+50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,245),3)
            roi = frame[y:y+h , x:x+w]
            eyes = capture_eye(roi)
            for ex,ey,ew,eh in eyes:
                cv2.rectangle(roi,(ex,ey),(ex+ew,ey+eh),(255,0,245),2)
                # cv2.putText(roi,'face found',(ex+(ew)//2,ey+eh+50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,245,0),2)
    cv2.imshow('face',frame)
    if cv2.waitKey(1) == 13 :
        break

cv2.destroyAllWindows()
