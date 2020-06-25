import numpy as np
import cv2
import dlib
import time
from imutils import face_utils

PREDICTOR_PATH = '/Users/animeshgupta/Downloads/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(PREDICTOR_PATH)
detector = dlib.get_frontal_face_detector()

def get_landmarks(im):
    rects = detector(im,1)
    if(len(rects)>1):
        pass
    if(len(rects)==0):
        pass
    return np.matrix([[p.x, p.y]for p in predictor(im,rects[0]).parts()])

def annotate_landmarks(im, landmarks):
    im = im.copy()
    for idx,point in enumerate(landmarks):
        pos = (point[0,0], point[0,1])
        cv2.putText(im,str(idx+1),pos,cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.4, color=(0,255,0))
        cv2.circle(im,pos,3,color=(0,255,245))
    return im

def top_lip(landmarks):
    top_lip_points = []
    for i in range(48,53):
        top_lip_points.append(landmarks[i])
    for i in range(61,64):
        top_lip_points.append(landmarks[i])
    # print('top lips',top_lip_points)
    top_lip_all_points = np.squeeze(np.asarray(top_lip_points))
    # print('top lip all points',top_lip_all_points)
    top_lip_mean = np.mean(top_lip_all_points,axis=0)
    # print('mean',top_lip_mean)
    return top_lip_mean[:1]

def bottom_lip(landmarks):
    bottom_lip_points = []
    for i in range(48,53):
        bottom_lip_points.append(landmarks[i])
    for i in range(61,64):
        bottom_lip_points.append(landmarks[i])
    # print('top lips',top_lip_points)
    bottom_lip_all_points = np.squeeze(np.asarray(bottom_lip_points))
    # print('top lip all points',top_lip_all_points)
    bottom_lip_mean = np.mean(bottom_lip_all_points,axis=0)
    # print('mean',top_lip_mean)
    return bottom_lip_mean[:1]

image = cv2.imread('../images/orig_image.jpg')
landmarks = get_landmarks(image)
lip_distance = np.abs(top_lip(landmarks)-bottom_lip(landmarks))
if(lip_distance>20):
    print('perform whatever you want to do')
else:
    print('nothing')

