import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((512,512,3),dtype=np.uint8)
img2 = np.full((512,512,3),255,dtype=np.uint8)
# print(img2)
cv2.imshow('white canvas',img2)
cv2.waitKey(0)
cv2.rectangle(image,(0,0),(511,511),(255,255,0),-1)
cv2.line(img2,(0,0),(511,511),(255,0,0),25)
cv2.imshow('black canvas',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.putText(image,'Hello World!',(75,290),cv2.FONT_HERSHEY_DUPLEX,2,(0,255,255),2)
cv2.imshow('black canvas',image)
cv2.waitKey(0)
# cv2.destroyWindow('black canvas')
# cv2.imshow('white canvas',img2)
# cv2.waitKey(0)
cv2.destroyAllWindows()
# np.ndarray()