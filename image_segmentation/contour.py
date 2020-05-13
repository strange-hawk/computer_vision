# contour are contiuous lines or curves that bound or cover the full boundary of an object in image

import cv2
import numpy as np

image = cv2.imread('../images/shapes.jpg')
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray,30,200)
