import cv2
import numpy as np

image = cv2.imread('images/scan.jpg')
cv2.imshow('image',image)
cv2.waitKey(0)

points_A = np.float32([[320,15],[700,215],[85,610],[530,780]])
points_B = np.float32([[0,0],[520,0],[0,894],[520,894]])
m = cv2.getPerspectiveTransform(points_A, points_B)
warp = cv2.warpPerspective(image,m,(520,894))
cv2.imshow('warped',warp)
cv2.waitKey(0)
cv2.destroyAllWindows()

# in affine only 3 are required
