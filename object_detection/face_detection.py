import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('../Haarcascades/haarcascade_frontalface_default.xml')

image = cv2.imread('../images/Trump.jpg')
height,width=int(image.shape[0]*1.5),int(image.shape[1]*1.5)
cv2.imshow('image',image)
cv2.waitKey(0)
image2=cv2.resize(image,dsize=(height,width))
cv2.imshow('image',image2)
cv2.waitKey(0)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('image',gray)
cv2.waitKey(0)

faces = face_classifier.detectMultiScale(gray,5,5)

if faces is ():
    print('no faces to display')

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,126),3)
    cv2.imshow('face detction',image)
    cv2.waitKey(0)

cv2.destroyAllWindows()