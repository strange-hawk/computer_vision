import cv2
import numpy as np


def get_area(contour_list):
    area=[]
    for i in contour_list:
        area.append(cv2.contourArea(i))
    return area


image = cv2.imread('../images/bunchofshapes.jpg')
# cv2.imshow('image',image)
# cv2.waitKey(0)
cv2.destroyAllWindows()

blank_image = np.zeros((image.shape[0],image.shape[1],3))
blank_image2 = np.zeros((image.shape[0],image.shape[1],3))


original_image = image.copy()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# finding canny edges
edged = cv2.Canny(gray,30,210)
# cv2.imshow('edge',edged)
# cv2.waitKey(0)
cv2.destroyAllWindows()

# find contours
contours,hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
sorted_contours = sorted(contours,key=cv2.contourArea,reverse=True)
cv2.drawContours(blank_image,[contours[0]],-1,(255,255,0),3)
cv2.imshow('minimum area',blank_image)
cv2.waitKey(0)
cv2.drawContours(blank_image2,[sorted_contours[0]],-1,(255,255,0),3)
cv2.imshow('maximum area',blank_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(cv2.contourArea(contours[3]))