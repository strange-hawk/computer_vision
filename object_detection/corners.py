import cv2
import numpy as np

image = cv2.imread('../images/chess.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# coner harris reures the dtype to be float32
gray = np.float32(gray)
a=[1,2,3]
harris_corner = cv2.cornerHarris(gray,3,3,0.05)
kernel = np.ones((5,5),np.uint8)
# cv2.imshow('',kernel)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# harris_corner = cv2.dilate(harris_corner,kernel,iterations=3)
# image[harris_corner > 0.25 * harris_corner.max()]=[0,127,0]
# cv2.imshow('j',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# good features to track
corners = cv2.goodFeaturesToTrack(gray,100,0.5,1)
print(corners.shape)
for c in corners:
    x,y=c[0]
    x,y=int(x),int(y)
    cv2.rectangle(image,(x-10,y-10),(x+10,y+10),(0,120,34),3)
cv2.imshow('j',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.sift