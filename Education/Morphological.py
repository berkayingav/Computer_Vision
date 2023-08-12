import cv2
import numpy as np

img = cv2.imread("castle.jpg",0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
diletion = cv2.dilate(img,kernel,iterations = 1) # kalınlastırma islemi
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)   #gürültü kaldırma openi close yaparsan bozulmalar düzeltilir
cv2.imshow("morpho",opening)
cv2.imshow("erosion",erosion)
cv2.imshow("diletion",diletion)
cv2.waitKey(0)
cv2.destroyAllWindows