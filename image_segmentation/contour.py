# contour are contiuous lines or curves that bound or cover the full boundary of an object in image

import cv2
import numpy as np

image = cv2.imread('../images/shapes_donut.jpg')
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray,30,200)

# find contours
contours,heirarchy = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image,contours,-1,(255,0,0),5)
cv2.imshow('contour image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(heirarchy)

# cv2.RETR_EXTERNAL considers only outermot contours
# cv2.RETR_LIST considers all contours