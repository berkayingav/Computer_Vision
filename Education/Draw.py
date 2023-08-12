import cv2
import numpy as np



tuval = np.zeros((512,512,3),dtype=np.uint8) + 255

cv2.line(tuval,(50,50),(512,512),(255,0,0),thickness=5)
cv2.line(tuval,(100,50),(450,450),(0,0,255),thickness=7)

cv2.rectangle(tuval,(20,20),(50,50),(0,255,0),thickness=2)   #içi dolu dikdörtgen istiyorsan thickness -'li olsun
cv2.rectangle(tuval,(50,50),(150,150),(0,255,0),thickness=-1)

cv2.circle(tuval,(250,250),100,(0,0,255),thickness=5) # 250 merkezi 100 yarıçapı

#üçgen için ayrı fonksiyon olmadığından line fonksiyonu kullanarak çizeceğiz.

p1=(100,200)
p2=(50,50)
p3=(300,100)

cv2.line(tuval,p1,p2,(0,0,0),4)
cv2.line(tuval,p2,p3,(0,0,0),4)
cv2.line(tuval,p1,p3,(0,0,0),4)

#rectangle ile beşgen ve yamuk oluşturcaz

points = np.array([[[110,200],[330,200],[290,220],[100,100]]],np.int32)
#3 tane kesikli parantez olması sebebi 3D array oluşturmak istediğimiz içindir.
cv2.polylines(tuval,[points],True,(0,0,100),thickness=5)  #dörtgen kapalı olsun istiyosak true açık olcak ise false

cv2.ellipse(tuval,(300,300),(100,50),0,0,360,(255,255,0),-1)

while True:
    cv2.imshow("Tuval",tuval)
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break
    cv2.destroyAllWindows()