import cv2
import numpy as np

image=cv2.imread('../images/scan.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray=cv2.Canny(gray,50,200)
methods = ['cv2.RETR_EXTERNAL','cv2.RETR_TREE','cv2.RETR_LIST','cv2.RETR_CCOMP','cv2.RETR_FLOODFILL']
contour,hierarchy=cv2.findContours(gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(len(contour))
# for i in range(170,len(contour)):
#     # s=image.copy()
#     cv2.drawContours(image,contour[i],-1,(255,0,243),3)
#     cv2.imshow('abc'+str(i),image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

cv2.drawContours(image,contour[177],-1,(255,0,243),3)
cv2.imshow('im',image)
x,y,w,h = cv2.boundingRect(contour[177])
print(cv2.boundingRect(contour[177]))
cv2.waitKey(0)
cv2.destroyAllWindows()
