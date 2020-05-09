import cv2
import numpy as np

image = cv2.imread('../parent/images/input.jpg')
height,width = image.shape[:2]

rotation_mat = cv2.getRotationMatrix2D((0,width/2),-90,1)
# cv2.imshow('abc',cv2.warpAffine(image,rotation_mat,(width,height)))
img1 = cv2.transpose(image)
img2 = cv2.transpose(img1)
# cv2.imshow('rotate',rotate_image)
cv2.imshow('imgage',image)
cv2.waitKey(0)
cv2.destroyAllWindows()