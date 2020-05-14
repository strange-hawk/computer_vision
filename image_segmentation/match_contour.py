import cv2
import numpy as np

template = cv2.imread('../images/4star.jpg',0)
cv2.imshow('start',template)
cv2.waitKey(0)
cv2.destroyAllWindows()

target = cv2.imread('../images/shapestomatch.jpg')
target_gray = cv2.cvtColor(target,cv2.COLOR_BGR2GRAY)

ret,thresh1 = cv2.threshold(template,127,255,0)
ret,thresh2 = cv2.threshold(target_gray,127,255,0)

# find contours
contour,hierarchy = cv2.findContours(thresh1,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
zero = np.zeros((template.shape[0],template.shape[1]))
contour_sorted = sorted(contour,key=cv2.contourArea,reverse=True)
template_contour = contour_sorted[1]
contour,hierarchy = cv2.findContours(thresh2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
closest_contour=[]
for c in contour:
    match = cv2.matchShapes(template_contour,c,1,0.0)
    if match<0.15:
        closest_contour.append(c)
    else:
        continue

cv2.drawContours(target,closest_contour,-1,(255),3)
cv2.imshow('output',target)
cv2.waitKey(0)
cv2.destroyAllWindows()