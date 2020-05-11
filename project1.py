import cv2
import numpy as np
import keyboard

def auto_canny(image,sigma=0.33):
    v = np.median(image)
    lower = int(max(0,(1.0 - sigma*v)))
    upper = int(min(255,(1.0 + sigma*v)))
    return cv2.Canny(image,lower,upper)




def sketch(frame,t):
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)
    high_thresh,thresh_im = cv2.threshold(img_gray_blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    low_thresh = int(0.5*(high_thresh))
    canny_edge = cv2.Canny(img_gray_blur,35,t)
    # canny_edge = cv2.Canny(img_gray_blur,35,70)
    ret,mask = cv2.threshold(canny_edge,70,255,cv2.THRESH_BINARY)
    return mask

cap = cv2.VideoCapture(0)
t=35
while True:
    ret,frame = cap.read()
    cv2.imshow('live',sketch(frame,55))
    # if(keyboard.is_pressed('n')):
    #     t=t+5
    #     print(t)
    # if(keyboard.is_pressed('p')):
    #     t=t-5
    #     print(t)
    if cv2.waitKey(1)==13:
        print(f'final t is {t}')
        break

# after tuning

cap.release()
cv2.destroyAllWindows()
