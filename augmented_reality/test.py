import numpy as np
import cv2
import dlib
import time
from imutils import face_utils

PREDICTOR_PATH = '/Users/animeshgupta/Downloads/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(PREDICTOR_PATH)
detector = dlib.get_frontal_face_detector()

class TooManyFaces(Exception):
    pass

class NoFaces(Exception):
    pass


def get_landmarks(im):
    rects = detector(im,0)
    # print(rects)
    
    im2 = np.full((im.shape[:]),255,np.uint8)
    if len(rects) == 0:
        return im2
    # landmarks = np.matrix([[p.x, p.y] for p in predictor(im,rects[0]).parts()])
    # for idx,point in enumerate(landmarks):
    #     im2[point[0,1]-4:point[0,1]+4,point[0,0]-4:point[0,0]+4,:]=(255,0,255)
    # cv2.rectangle(im2,(left,top),(right,bottom),color=(255,0,0))
    left,right,top,bottom = rects[0].left(),rects[0].right(),rects[0].top(),rects[0].bottom()
    # print(im.shape)
    # print(left,right,top,bottom)
    # cv2.rectangle(im2,(left,top),(right,bottom),color=(255,56,4),thickness=3)
    for rect in rects:
        shape = predictor(im,rect)
        shape = face_utils.shape_to_np(shape)
        for x,y in shape:
            cv2.circle(im2,(x,y),6,(0,245,29),-1)
    return im2[top-100:bottom+100,left-100:right+100,:]


cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    # frame = cv2.resize(frame,None,fx=0.75,fy=0.75,interpolation=cv2.INTER_LINEAR)
    # cv2.namedWindow('Resize frame',cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('Resize frame',int(1280*0.75),int(720*0.75))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = get_landmarks(frame)
    # image_with_landmarks = annotate_landmarks(frame,landmarks)
    # cv2.imshow('ar',image_with_landmarks)
    cv2.imshow('frame',frame)
    if(cv2.waitKey(1)==13):
        break
    # time.sleep(0.1)

cap.release()
cv2.destroyAllWindows()
