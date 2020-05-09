# an edge can be defined as sudden changes (discontinuity) in an image and they can encode just as information as pixels

import cv2
import numpy as np

image = cv2.imread('images/input.jpg',0)
height,width = image.shape

# sobel_x = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
# sobel_y = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)

# cv2.imshow('original',image)
# cv2.waitKey(0)
# cv2.imshow('sobel',sobel_x)
# cv2.waitKey(0)
# cv2.imshow('sobel',sobel_y)
# cv2.waitKey(0)
# cv2.imshow('comine',cv2.bitwise_or(sobel_x,sobel_y))
# cv2.waitKey(0)

# # 
# cv2.imshow('laplacian',cv2.Laplacian(image,cv2.CV_64F))
# cv2.waitKey(0)

# 
cv2.imshow('canny',cv2.Canny(image,50,100))
cv2.waitKey(0)
cv2.imshow('canny',cv2.Canny(image,30,130))
cv2.waitKey(0)
cv2.imshow('canny',cv2.Canny(image,10,150))
cv2.waitKey(0)
cv2.imshow('canny',cv2.Canny(image,20,200))
cv2.waitKey(0)

cv2.destroyAllWindows()
