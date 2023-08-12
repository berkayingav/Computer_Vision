import cv2
import numpy as np

img1 = cv2.imread("bitwise_1.png")
img2 = cv2.imread("bitwise_2.png")
#img3 = cv2.imread("castle.jpg")
#img4 = cv2.imread("kubat.jpg")
#img5 = cv2.resize(img3,(600,600))
#img6 = cv2.resize(img4,(600,600))
bit_and = cv2.bitwise_and(img2,img1)
bit_or = cv2.bitwise_or(img2,img1)
bit_xor = cv2.bitwise_xor(img2,img1)
bit_not = cv2.bitwise_not(img1) #notlar tersini alır beyazsa siyah gibi
bit_not2 = cv2.bitwise_not(img2)
#bit_and1 = cv2.bitwise_and(img6,img5)
cv2.imshow("bit_and",bit_and) # karşılaştırma yapar siyah 0 beyaz 1 diyerek
cv2.imshow("bit_or",bit_or)
cv2.imshow("bit_xor",bit_xor)
cv2.imshow("bit_not",bit_not)
cv2.imshow("bit_not2",bit_not2)
#cv2.imshow("bit_and1",bit_and1)

cv2.waitKey(0)
cv2.destroyAllWindows()