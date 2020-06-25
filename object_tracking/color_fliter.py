import numpy as np
import cv2

lower_limit = np.array([125,0,150])
upper_limit = np.array([175,255,255])
cap = cv2.VideoCapture(0)
while True:
    ret,frame= cap.read()
    hsv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image,lower_limit,upper_limit)
    cv2.imshow('cut out',cv2.bitwise_and(frame,frame,mask=mask))
    if(cv2.waitKey(1)==13):
        break
cv2.destroyAllWindows()