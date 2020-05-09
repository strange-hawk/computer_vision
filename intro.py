import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('../parent/images/tobago.jpg')
cv2.imshow('tobaco',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
histogram = cv2.calcHist([image],[0],None,[256],[0,256])
plt.hist(image.ravel(),bins=256,range=[0,256])
plt.show()
color=['b','g','r']
for i,c in enumerate(color):
    hist = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(hist,color=c)
    plt.xlim([0,256])

plt.show()
