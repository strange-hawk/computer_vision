import cv2
import numpy as np

# dilation - add a layer of white pixels to the boundary from outside the image
# erosion - remove a layer of white pixels to the boundary from outside the image
# opening - erosion then dilation
# closing - dilation then erosion

image = cv2.imread('images/opencv_inv.png')
cv2.imshow('orig',image)
cv2.waitKey(0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(image,kernel,iterations=1)
cv2.imshow('erosion',erosion)
cv2.waitKey(0)
cv2.imshow('dilation',cv2.dilate(image,kernel,iterations=1))
cv2.waitKey(0)
cv2.imshow('opening',cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel,iterations=1))
cv2.waitKey(0)
cv2.imshow('closing',cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel,iterations=1))
cv2.waitKey(0)




cv2.destroyAllWindows()

image = cv2.imread('images/opencv.png')
cv2.imshow('orig',image)
cv2.waitKey(0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(image,kernel,iterations=1)
cv2.imshow('erosion',erosion)
cv2.waitKey(0)
cv2.imshow('dilation',cv2.dilate(image,kernel,iterations=1))
cv2.waitKey(0)
cv2.imshow('opening',cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel,iterations=1))
cv2.waitKey(0)
cv2.imshow('closing',cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel,iterations=1))
cv2.waitKey(0)