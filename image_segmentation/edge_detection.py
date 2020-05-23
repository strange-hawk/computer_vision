import cv2
import numpy as np

image = cv2.imread('../images/input.jpg')
print(image.shape)
# cv2.imshow('image',image)
# cv2.waitKey(0)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray,100,170)

lines = cv2.HoughLines(edged,1,np.pi/180,300)
print(lines.shape)
for i in lines:
    i=i.reshape((2,))
    rho,theta = i
    a = np.cos(theta)
    b = np.sin(theta)
    x0,y0 = rho*a,rho*b
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(image,(x1,y1),(x2,y2),(255,0,0),2)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# probabilistic hough lines
imge2 = np.full((image.shape[0],image.shape[1]),255,np.uint8)
# cv2.imshow('image',imge2)
# cv2.waitKey(0)
lines = cv2.HoughLinesP(edged,1,np.pi/180,125,20,10)
for i in lines:
    i=i.reshape(4,1)
    x1,y1,x2,y2=i
    cv2.line(imge2,(x1,y1),(x2,y2),(25),2)
cv2.imshow('image',imge2)
# np.full()
cv2.waitKey(0)
cv2.destroyAllWindows()
    
