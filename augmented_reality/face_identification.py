import numpy as np
import cv2
import dlib

PREDICTOR_PATH = '/Users/animeshgupta/Downloads/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(PREDICTOR_PATH)
detector = dlib.get_frontal_face_detector()

class TooManyFaces(Exception):
    pass

class NoFaces(Exception):
    pass

def get_landmarks(im):
    rects = detector(im,1)
    if len(rects)>1:
        raise TooManyFaces
    if len(rects) ==0:
        raise NoFaces

    # print(predictor(im,rects[0]).parts())
    # print(rects[0,0])
    # print(len(predictor(im,rects[0]).parts()))
    # for p in rects[0]:
    #     print(p)
    # print(rects[0])
    left,right,top,bottom = rects[0].left(),rects[0].right(),rects[0].top(),rects[0].bottom()
    # print('left',left)
    # print('right',right)
    # print('top',top)
    # print('bottom',bottom)
    # print('height',rects[0].height())
    # print('width',rects[0].width())

    # dlib rectangle are of the form (left,top,right+1,bottom+1)
    cv2.rectangle(im,(left,top),(right,bottom),color=(255,0,0))
    # a,b=rects[0].dcenter()
    # cv2.circle(im,(a,b),4,color=(255,0,0),thickness=2)
    # cv2.circle(im,rects[0].dcenter(),3,color=(255,0,0))
    cv2.imshow('temp',im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    # cv2.rectangle(im,rects[0,0,1],rects[1],color=(0,255,255),thickness=2)
    return im,np.matrix([[p.x, p.y] for p in predictor(im,rects[0]).parts()])


def annotate_landmarks(im,landmarks):
    im = im.copy()
    im2 = np.full((im.shape[:-1]),255,np.uint8)
    for idx,point in enumerate(landmarks):
        pos = (point[0,0],point[0,1])
        im2[point[0,1]-2:point[0,1]+2,point[0,0]-2:point[0,0]+2]=(0)
        cv2.putText(im,str(idx),pos,cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.4,color=(0,0,255))
        cv2.circle(im,pos,2,color=(0,0,255))
    cv2.imshow('temp',im2)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return im


image= cv2.imread('../images/orig_image.jpg')
cv2.imshow('abv',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
image,landmarks = get_landmarks(image)
image_with_landmarks = annotate_landmarks(image,landmarks)
cv2.imshow('result',image_with_landmarks)
cv2.waitKey(0)
cv2.destroyAllWindows()