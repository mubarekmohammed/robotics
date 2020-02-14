#please install numpy and opencv before running the program
#pip list numpy for numpy OR 
#pip list cv2 for opencv
#object detection 
#still needs work as the objects center is still not collected right 

import numpy as np
import cv2


img_mug = cv2.imread("coffee_mug.png",1)

img_mug = cv2.resize(img_mug,(0,0),fx=0.4,fy=0.4)

gray=cv2.cvtColor(img_mug,cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,225,1)


cv2.imshow("Image Resized",img_mug)
cv2.imshow("AdaptiveThreshold",thresh)

cv2.imwrite("thresh_result.jpeg",thresh)

#_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


img2mug = img_mug.copy()
index = -1
thickness = 3
color = (255,0,0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img2mug,contours,index,color,thickness)
cv2.imshow("Contours",img2mug)
cv2.imwrite("Contours.jpeg",img2mug)


objects = np.zeros([img_mug.shape[0],img_mug.shape[1],3],'uint8')

for c in contours:
    cv2.drawContours(objects,[c],-1,color,-1)
    
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c,True)
    
    M = cv2.moments(c)
    if(M['m00'] == 0):
        continue
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.circle(objects,(cx,cy),2,(0,0,255),-1)
    print("Area: {}, Perimeter: {}".format(area,perimeter))
    
#cv2.imshow("Contours",objects)
cv2.imwrite("Contours_objects.jpg",objects)   
    
    




cv2.waitKey(0)

cv2.destroyAllWindows()