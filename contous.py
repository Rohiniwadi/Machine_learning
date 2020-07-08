import cv2
import numpy as np
import math

img = cv2.imread("hand.jpg")
img = cv2.flip(img ,1)
img = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img,(5,5),10)

_,thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
contours,hierarchy = cv2.findContours(thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
cnt = max(contours , key = lambda x: cv2.contourArea(x))

hull = cv2.convexHull(cnt , returnPoints =False)
defects = cv2.convexityDefects(cnt , hull)

l=0
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])


    a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
    c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

    s= (a+b+c)/2
    ar =math.sqrt(s*(s-a)*(s-b)*(s-c))
    d = (2*ar)/a
    angle = math.acos((b**2+c**2-a**2)/(2*b*c))*57

    if angle<=90 and d>30:
        l+=1
        cv2.circle(img,far,3,[0,0,255],-1)

    cv2.line(img,start,end,[0,255,0],2)

l+=1

font = cv2.FONT_HERSHEY_SIMPLEX
if l==1:
    cv2.putText(img,'1',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
elif l==2:
    cv2.putText(img,'2',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
elif l==3:
    cv2.putText(img,'3',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
elif l==4:
    cv2.putText(img,'4',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
elif l==5:
    cv2.putText(img,'5',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)

#cv2.drawContours(img , cnt,-1,(0,0,255),3)
cv2.imshow('contours' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
