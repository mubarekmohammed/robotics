import numpy as np
import cv2

img = cv2.imread("coffee_mug.png",1)

img_BW = cv2.imread("coffee_mug.png",0)

print(img.shape)

min_img = cv2.resize(img,(0,0),fx=0.4,fy=0.4)
min_imgBW = cv2.resize(img_BW,(0,0),fx=0.5,fy=0.5)

hsv = cv2.cvtColor(min_img,cv2.COLOR_BGR2HSV)



h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

min_img_hsv = np.concatenate((h,s,v),axis=1)

print(hsv.shape)

print(min_img.shape)

ret,min_sat= cv2.threshold(s,40,255,cv2.THRESH_BINARY)

min_sat = cv2.resize(min_sat,(0,0),fx=1,fy=1)

adapt_thres= cv2.adaptiveThreshold(min_imgBW,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,151,1)

cv2.imshow("Adaptive threshold",adapt_thres)
cv2.imshow("minimum saturation",min_sat)

cv2.imshow("Image",min_img_hsv)



cv2.waitKey(0)

cv2.destroyAllWindows()