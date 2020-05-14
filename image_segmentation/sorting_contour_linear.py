import cv2
import numpy as np

def x_cord_contour(image):
    if cv2.contourArea(image)>10:
        M = cv2.moments(image)
        return int(M['m10']/M['m00'])

def y_contour(image):
    if cv2.contourArea(image)>10:
        M = cv2.moments(image)
        return int(M['m01']/M['m00'])


def draw_circle_middle_unsorted(image,c):
    M = cv2.moments(c)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.circle(image,(cx,cy),10,(255,255,0),-1)
    cv2.imshow('random',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def draw_circle_middle(image,c):
    M = cv2.moments(c)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.circle(image,(cx,cy),10,(255,255,0),-1)
    cv2.imshow('sorted',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = cv2.imread('../images/bunchofshapes.jpg')
cv2.imshow('original',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
gray = cv2.cvtColor(image.copy(),cv2.COLOR_BGR2GRAY)
gray = cv2.Canny(gray,30,200)
# gray = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contour,hierarchy = cv2.findContours(gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(image,contour,-1,(255,255,0),3)
contour_sorted_left_right = sorted(contour,key=x_cord_contour,reverse=False)

# drawing circles on unsorted contours
# for i,c in enumerate(contour):
#     draw_circle_middle_unsorted(image.copy(),c)

# drawing circles on sorted contours
# for i,c in enumerate(contour_sorted_left_right):
#     draw_circle_middle(image.copy(),c)

# labeling the figures and cropping the figures
for i,c in enumerate(contour_sorted_left_right):
    cv2.drawContours(image,[c],-1,(255,0,255),5)
    M = cv2.moments(c)
    cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    cv2.putText(image,str(i+1),(cx,cy),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),5)
    print(cv2.boundingRect(c))
    x,y,w,h = cv2.boundingRect(c)
    cropped_image=image[y:y+h , x:x+w]
    # cv2.imshow('cropped_image',cropped_image)
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


cv2.imshow('contour',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
