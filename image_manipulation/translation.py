import cv2
import numpy as np

image = cv2.imread('../parent/images/input.jpg')
height,width = image.shape[:2]
quarter_height,quarter_width = height/4,width/4
T = np.float32([[1,0,quarter_width],[0,1,0]])
img_translation = cv2.warpAffine(image,T,(width//2,height//2))
cv2.imshow('original',image)
cv2.waitKey(0)
cv2.imshow('affined',img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
