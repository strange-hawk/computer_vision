import cv2
import numpy as np

image = cv2.imread('../images/house.jpg')
img_copy = image.copy()
cv2.imshow('original house',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

for i,c in enumerate(contours):
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img_copy,(x,y),(x+w,y+h),(255,0,255),2)
    cv2.imshow('contour'+str(i+1),img_copy)
    cv2.waitKey(0)

cv2.destroyAllWindows()

for i,c in enumerate(contours):
    acc=cv2.arcLength(c,True)
    poly = cv2.approxPolyDP(c,acc,True)
    cv2.drawContours(image,c,-1,(255,0,255),2)
    cv2.imshow('approx contour',image)
    cv2.waitKey(0)
cv2.destroyAllWindows()

