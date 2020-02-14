#script converts the snapshot of a coffee mug into HSV and thresholding. 

import numpy as np
import cv2


img = cv2.imread("coffee_mug.png",1)


img = cv2.resize(img,(0,0),fx = 0.5, fy=0.5)


hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

res,thresh = cv2.threshold(hsv[:,:,0],25,255,cv2.THRESH_BINARY_INV)



#cv2.imshow("threshold",thresh)

#displays the edges of the coffee mug
edges = cv2.Canny(img,50,100)

cv2.imshow("Canny",edges)
cv2.imwrite("Coffee_mug_Canny.jpg",edges)


cv2.waitKey(0)

cv2.destroyAllWindows()