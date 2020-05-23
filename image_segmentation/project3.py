import cv2
import numpy as np
import keyboard

image = cv2.imread('../images/blobs.jpg')
# cv2.imshow('orig',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

params = cv2.SimpleBlobDetector_Params()
detector = cv2.SimpleBlobDetector_create(params)
# detector.empty()
keypoints = detector.detect(image)
print(len(keypoints))

# draw blobs on image
blank_page = np.zeros((10,10))
blobs = cv2.drawKeypoints(image,keypoints,blank_page,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.putText(blobs,'total number of blobs'+str(len(keypoints)),(20,550),cv2.FONT_HERSHEY_SIMPLEX,1,(100,0,255),2)
cv2.imshow('blobs',blobs)
cv2.waitKey(0)
# cv2.destroyAllWindows()

t = True
a=0.5
while(t):

    params = cv2.SimpleBlobDetector_Params()

    params.filterByArea = True
    params.minArea = 100

    params.filterByCircularity = True
    params.maxCircularity = 0.9

    params.filterByConvexity = False
    params.minConvexity = 0.2

    params.filterByInertia = True
    params.minInertiaRatio = 0.01
    params.maxInertiaRatio = a

    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(image)
    blobs = cv2.drawKeypoints(image,keypoints,blank_page,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('blobs with filter',blobs)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(a)
    if(keyboard.is_pressed('q')):
        t=False
        # break
    a=a+0.05
