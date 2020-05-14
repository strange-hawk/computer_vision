import cv2
import numpy as np

image = cv2.imread('../images/hand.jpg')
img_copy = image.copy()
cv2.imshow('original house',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
n = len(contours)-1
contour_sorted = sorted(contours,key = cv2.contourArea,reverse=False)[:n]

for i,c in enumerate(contour_sorted):
    hull = cv2.convexHull(c)
    cv2.drawContours(image,[hull],0,(255,0,240),3)
    cv2.imshow('hull',image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
