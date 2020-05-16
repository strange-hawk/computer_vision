import cv2
import numpy as np

image = cv2.imread('../images/someshapes.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# cv2.imshow('orig',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# threshold
ret,thresh = cv2.threshold(gray,127,255,0)

# contour
contour,hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
n=len(contour)
contour = sorted(contour,key=cv2.contourArea)[:n-1]
for cnt in contour:
    epsilon = 0.01*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    if(len(approx)==3):
        text = 'triangle'
        cv2.drawContours(image,[approx],-1,(255,125,100),-1)
        M = cv2.moments(cnt)
        cx,cy = int(M['m10']/M['m00']),int(M['m01']/M['m00'])
        cv2.putText(image,text,(cx-20,cy),cv2.FONT_HERSHEY_PLAIN,1,(25,125,40),2)
        cv2.imshow('image',image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    elif len(approx)==4:
        x,y,w,h = cv2.boundingRect(cnt)
        if(abs(w-h)<=3):
            cv2.drawContours(image,[approx],-1,(120,125,100),-1)
            M = cv2.moments(cnt)
            cx,cy = int(M['m10']/M['m00']),int(M['m01']/M['m00'])
            cv2.putText(image,'square',(cx-20,cy),cv2.FONT_HERSHEY_PLAIN,1,(255,125,100),2)
            cv2.imshow('image',image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        else:
            cv2.drawContours(image,[approx],-1,(255,125,190),-1)
            M = cv2.moments(cnt)
            cx,cy = int(M['m10']/M['m00']),int(M['m01']/M['m00'])
            cv2.putText(image,'rectangle',(cx-20,cy),cv2.FONT_HERSHEY_PLAIN,1,(255,125,100),2)
            cv2.imshow('image',image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    elif len(approx)==10:
        cv2.drawContours(image,[approx],-1,(25,25,100),-1)
        M = cv2.moments(cnt)
        cx,cy = int(M['m10']/M['m00']),int(M['m01']/M['m00'])
        cv2.putText(image,'star',(cx-20,cy),cv2.FONT_HERSHEY_PLAIN,1,(255,125,100),2)
        cv2.imshow('image',image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif len(approx)>10:
        cv2.drawContours(image,[approx],-1,(25,125,10),-1)
        M = cv2.moments(cnt)
        cx,cy = int(M['m10']/M['m00']),int(M['m01']/M['m00'])
        cv2.putText(image,'circle',(cx-20,cy),cv2.FONT_HERSHEY_PLAIN,1,(255,125,100),2)
        cv2.imshow('image',image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # print(len(approx))

