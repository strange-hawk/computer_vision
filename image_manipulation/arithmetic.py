import cv2
import numpy as np

# image = cv2.imread('../parent/images/input.jpg')
# t=np.ones(image.shape,dtype=np.uint8)*50
# cv2.imshow('orig',image)
# cv2.waitKey(0)
# cv2.imshow('added',cv2.add(image,t))
# cv2.waitKey(0)
# cv2.imshow('sub',cv2.subtract(image,t))
# cv2.waitKey(0)
# cv2.destroyAllWindows()

square = np.zeros((300,300),dtype=np.uint8)
cv2.rectangle(square,(40,40),(260,260),(255,0,0),-1)
cv2.imshow('square',square)
cv2.waitKey(0)

ellipse = np.zeros((300,300),np.uint8)
cv2.circle(ellipse,(150,150),110,(255,0,0),-1)
# cv2.ellipse(ellipse,(150,150),3,180,255,-1)
cv2.imshow('ellipse',ellipse)
cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.imshow('and',cv2.bitwise_and(square,ellipse))
cv2.waitKey(0)
cv2.imshow('or',cv2.bitwise_or(square,ellipse))
cv2.waitKey(0)
cv2.imshow('xor',cv2.bitwise_xor(square,ellipse))
cv2.waitKey(0)
cv2.imshow('not',cv2.bitwise_not(square,ellipse))
cv2.waitKey(0)
cv2.destroyAllWindows()