import cv2
import numpy as np

image = cv2.imread('../parent/images/input.jpg')
image_scaled=[]
scale_format=['INTER_CUBIC','INTER_LINEAR','INTER_AREA','INTER_NEAREST','INTER_LANCZOS4']
image_scaled.append(cv2.resize(image,(900,400),interpolation = cv2.INTER_CUBIC))
image_scaled.append(cv2.resize(image,(900,400),interpolation = cv2.INTER_LINEAR))
image_scaled.append(cv2.resize(image,(900,400),interpolation = cv2.INTER_AREA))
image_scaled.append(cv2.resize(image,(900,400),interpolation = cv2.INTER_NEAREST))
image_scaled.append(cv2.resize(image,(900,400),interpolation = cv2.INTER_LANCZOS4))
for i in range(5):
    cv2.imshow(scale_format[i],image_scaled[i])
    cv2.waitKey(0)
cv2.destroyAllWindows()

# another way of rescaling i.e. pyrup, pyrdown
image1 = cv2.pyrUp(image)
image2= cv2.pyrDown(image1)
cv2.imshow('a',image)
cv2.waitKey(0)
cv2.imshow('b',image1)
cv2.waitKey(0)
cv2.imshow('c',image2)
cv2.waitKey(0)
cv2.destroyAllWindows()