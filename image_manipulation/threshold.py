import cv2
import numpy as np

image = cv2.imread('images/origin_of_Species.jpg',0)
cv2.imshow('orig',image)
cv2.waitKey(0)
# works only on grayscale images

thresh,img = cv2.threshold(image,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# print(thresh)
cv2.imshow('127 binary threshold',img)
cv2.waitKey(0)
thresh,img = cv2.threshold(image,0,255,cv2.THRESH_OTSU)
# print(thresh)
cv2.imshow('0 binary threshold',img)
cv2.waitKey(0)
cv2.destroyAllWindows()