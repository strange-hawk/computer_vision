import cv2
import numpy as np


def sketch(image,template):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray,template,cv2.TM_SQDIFF_NORMED)
    min_value,max_value,min_loc,max_loc = cv2.minMaxLoc(result)
    print(min_value,max_value)
    return min_loc
    # or
    # result = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    # min_value,max_value,min_loc,max_loc = cv2.minMaxLoc(result)
    # return max_loc

    # threshold = 0.8
    # loc = np.where(result>=threshold)
    # return loc


image = cv2.imread('../images/self.jpg',0)
# cv2.imshow('a',image)
w,h = image.shape[::-1]
print(f'w is {w} and h is {h}')
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    top_left = sketch(frame,image)
    # print(top_left)
    bottom_right = (top_left[0]+w,top_left[1]+h)
    cv2.rectangle(frame,top_left,bottom_right,(255,0,0),3)
    cv2.putText(frame,'Animesh Gupta',(top_left[0]+w//2 - 15,top_left[1]-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv2.imshow('detection',frame)
    if cv2.waitKey(1)==13:
        break

cv2.destroyAllWindows()
