import cv2
import numpy as np

image = cv2.imread('images/input.jpg',2)
kernel_2d = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
sharpen_image = cv2.filter2D(image,-1,kernel_2d)
cv2.imshow('orig',image)
cv2.waitKey(0)
cv2.imshow('sharp',sharpen_image)
cv2.waitKey(0)
cv2.destroyAllWindows()