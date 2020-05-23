import cv2
import numpy as np

def ORB_detector(image,image_template):
    image1=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    orb =  cv2.ORB_create(1000,1.2)
    kp1,dp1 = orb.detectAndCompute(image1,None)
    kp2,dp2 = orb.detectAndCompute(image_template,None)

    # distance based matching

    bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
    matches = bf.match(dp1,dp2)
    matches = np.array(matches)
    # print(matches.shape)
    # print(matches[:10])
    # print('--'*50)
    matches = sorted(matches, key = lambda x: x.distance)
    return len(matches)

cap = cv2.VideoCapture(0)
image_template = cv2.imread('../images/self.jpg',0)
# cv2.imshow('iage',image_template)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
while(True):
    ret,frame = cap.read()
    # cv2.imshow('abc',frame)
    # if cv2.waitKey(1)==13:
    #     break
    height,width = frame.shape[:2]

    top_left_x = int(width/3)
    top_left_y = int((height/2) - (height/4))
    bottom_right_x = (width//3)*2
    bottom_right_y = (height//2) + (height//4)
    # print(frame.shape)
    # print((top_left_x,top_left_y))
    # print((bottom_right_x,bottom_right_y))
    # print(frame[top_left_y:bottom_right_y,top_left_x:bottom_right_x].shape)
    # cv2.imshow('abc',frame[top_left_y:bottom_right_y,top_left_x:bottom_right_x])
    # if cv2.waitKey(1)==13:
    #     break
    cv2.rectangle(frame,(top_left_x,top_left_y),(bottom_right_x,bottom_right_y),(255,0,45),3)
    cropped = frame[top_left_y:bottom_right_y,top_left_x:bottom_right_y]
    matches = ORB_detector(cropped,image_template)
    # matches = np.array(matches)
    output_string = 'matches' + str(matches)
    cv2.putText(frame,output_string,(450,50),cv2.FONT_HERSHEY_COMPLEX,2,(250,0,250),2)

    threshold = 350

    if matches>threshold:
        cv2.rectangle(frame,(top_left_x,top_left_y),(bottom_right_x,bottom_right_y),(255,7,8),3)
        cv2.putText(frame,'OBJECT FOUND',(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(250,0,250),2)
    
    cv2.imshow('object detector using orb',frame)
    if cv2.waitKey(1)==13:
        break

cv2.destroyAllWindows()

