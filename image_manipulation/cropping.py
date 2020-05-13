import cv2
import numpy as np

image = cv2.imread('../parent/images/input.jpg')
height,width = image.shape[:2]
start_row,end_row = int(width*0.25), int(width*0.75)
start_height,end_height = int(height*0.25), int(height*0.75)
cropped_image = image[start_height:end_height, start_row:end_row ]
cv2.imshow('orig',image)
cv2.waitKey(0)
cv2.imshow('crop',cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()