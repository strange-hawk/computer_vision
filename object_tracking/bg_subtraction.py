import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cv2.ocl.setUseOpenCL(False)
ret,frame = cap.read()
average = np.float32(frame)
# fg_bg = cv2.createBackgroundSubtractorKNN()
fg_bg = cv2.createBackgroundSubtractorMOG2()
while True:
    ret,frame = cap.read()
    cv2.accumulateWeighted(frame,average,0.01)
    frame = cv2.convertScaleAbs(average)
    # frame = fg_bg.apply(frame)
    cv2.imshow('fg',frame)
    if(cv2.waitKey(1)==13):
        break
