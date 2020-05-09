import cv2
import numpy as np

image = cv2.imread('../parent/images/elephant.jpg')
cv2.imshow('elephant',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows
height,width = image.shape[:2]
q = np.zeros(image.shape,dtype=np.uint8)
q[int(height/4):int(2*height/3),int(width/4):int(2*width/3)] = image[int(height/4):int(2*height/3),int(width/4):int(2*width/3)]
# image2 = image[int(height/4):int(2*height/3),int(width/4):int(2*width/3)]
cv2.imshow('image',q)
cv2.waitKey(2000)

kernel_2d = np.ones((7,7),np.float32)/49
for i in range(3):
    image = cv2.filter2D(image,-1,kernel_2d)
    # cv2.imshow('kernel '+str(i+1),image)
    # cv2.waitKey(0)
# # image_kernelified = cv2.filter2D(image,-1,kernel_2d)
print(image.dtype)
blur_image=cv2.bitwise_or(q,image)
blur_image[int(height/4):int(2*height/3),int(width/4):int(2*width/3)]=q[int(height/4):int(2*height/3),int(width/4):int(2*width/3)]
cv2.imshow('kernel',blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
blur = cv2.blur(image,(3,3))
cv2.imshow('blur',blur)
cv2.waitKey(0)
cv2.imshow('gaussian blur',cv2.GaussianBlur(image,(3,3),0))
cv2.waitKey(0)
cv2.imshow('median blur',cv2.medianBlur(image,5))
cv2.waitKey(0)
cv2.imshow('bilateral',cv2.bilateralFilter(image,7,400,300))
cv2.waitKey(0)
cv2.destroyAllWindows()