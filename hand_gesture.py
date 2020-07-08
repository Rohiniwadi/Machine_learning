
import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)

while(True):
    ret , img = cap.read()
    img = cv2.flip(img,1)

    k = np.ones((5,5) , np.uint8)
    roi = img[100:400 ,100:400]

    cv2.rectangle(img , (100,100),(400,400),(0,255,0),0)
    hsv = cv2.cvtColor(roi , cv2.COLOR_BGR2HSV)


    lower_skin = np.array([0,20,70] ,np.uint8)
    upper_skin = np.array([20,255,255] ,np.uint8)

    mask = cv2.inRange(hsv,lower_skin ,upper_skin)
    mask = cv2.dilate(mask ,k ,iterations=4)
    blur = cv2.GaussianBlur(mask ,(5,5) ,100)
    _,thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    contours,hierarchy = cv2.findContours(thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours , key = lambda x: cv2.contourArea(x))

    print(cnt)

    hull = cv2.convexHull(cnt,returnPoints = False)
    print(hull)
    '''areahull = cv2.contourArea(hull)
    areacnt = cv2.contourArea(cnt)

    ratio = ((areahull - areacnt)/areacnt)*100'''
    
    defects = cv2.convexityDefects(cnt,hull)

    l=0
    for i in range(defects.shape[0]):
        s,e,f,d= defects[i,0]
        start = tuple(cnt[s][0])
        end =tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        pt =(10,180)

        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

        s= (a+b+c)/2
        ar =math.sqrt(s*(s-a)*(s-b)*(s-c))

        d = (2*ar)/a
        angle = math.acos((b**2+c**2-a**2)/(2*b*c))*57

        if angle<=90 and d>30:
            l+=1
            cv2.circle(roi,far,3,[0,0,255],-1)

        cv2.line(roi,start,end,[0,255,0],2)

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
    else:
        cv2.putText(img,'reposition',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
        
    cv2.imshow('mask',mask)
    cv2.imshow('image' ,img)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

    
