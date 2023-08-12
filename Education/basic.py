import cv2
import numpy as np

img = cv2.imread("kubat.jpg")
img = cv2.resize(img, (600,600))
dimension = img.shape
print(dimension)
color = img[150,200]
print("BGR",color)

blue= img[420,500,0]
print("blue:",blue)

cv2.imshow("deneme",img)

green = img[420,500,1]
print("green",green)

red = img[420,500,2]
print("red",red)

new_blue = img[420,500,0] = 250  #mavi değerini değiştiriyoruz
print("yeni mavi:", new_blue)

blue1 = img.item(150,200,0)   #farklı mavi rengi değiştirme yöntemi
print("blue1:",blue1)
img.itemset((150,200,0),172)
print("new blue1:",img[150,200,0])

cv2.waitKey(0)
cv2.destroyAllWindows()