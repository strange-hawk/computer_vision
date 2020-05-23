import cv2
import numpy as np

image = cv2.imread('../images/input.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create(1000)
keypoints = orb.detect(gray,None)
keypoints,descriptors = orb.compute(image,keypoints)
image = cv2.drawKeypoints(image,keypoints,np.array([]),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('descriptos',image)
cv2.waitKey(0)
cv2.destroyAllWindows()