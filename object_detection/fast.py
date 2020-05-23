import cv2
import numpy as np

image= cv2.imread('../images/input.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('orig',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
fast = cv2.FastFeatureDetector_create()
# fast = cv2.FastFeatureDetector(params)
# fast.empty()
keypoints = fast.detect(gray,None)
print(f'no. of keypoints detected {len(keypoints)}')
image = cv2.drawKeypoints(image,keypoints,np.array([]),(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('image with keypoints',image)
cv2.waitKey(0)
cv2.destroyAllWindows()