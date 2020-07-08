import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
l=[]
cap = cv2.imread("IMG1.jpg")
#cap.set(3, 200) #set width of the frame
#cap.set(4, 200) #set height of the frame
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
age_list = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)', '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']
gender_list = ['Male', 'Female']

def load_caffe_models():
    age_net = cv2.dnn.readNetFromCaffe('deploy_age.prototxt', 'age_net.caffemodel')
    gender_net = cv2.dnn.readNetFromCaffe('deploy_gender.prototxt', 'gender_net.caffemodel')
    return (age_net, gender_net)

def image_detector(age_net, gender_net):
    #font = cv2.FONT_HERSHEY_SIMPLE
    a=2
    global cap
    while a<12:
        
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
        gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        if(len(faces)>0):
            print("Found {} faces".format(str(len(faces))))
        for (x, y, w, h )in faces:
            cv2.rectangle(cap, (x, y), (x+w, y+h), (255, 255, 0), 2)
            face_img = cap[y:y+h, h:h+w].copy()
            blob = cv2.dnn.blobFromImage(face_img, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
            gender_net.setInput(blob)
            gender_preds = gender_net.forward()
            gender = gender_list[gender_preds[0].argmax()]
            print("Gender : " + gender)
            l.append(gender_preds[0].argmax()+1)

            age_net.setInput(blob)
            age_preds = age_net.forward()
            age = age_list[age_preds[0].argmax()]
            print("Age Range: " + age)
            #overlay_text = "%s %s" % (gender, age)
            cv2.putText(cap,"{} : {}".format(gender,age), (x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.9, 200)
            cap = cv2.resize(cap, (500,500), interpolation = cv2.INTER_AREA)
 
            
            cv2.imshow( "image",cap)
            path="IMG"+str(a)+".jpg"
            cap=cv2.imread(path)
            a+=1
            time.sleep(2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
def  classifie():
    age_net, gender_net = load_caffe_models()
    image_detector(age_net, gender_net)
    x=[1,2,3,4,5,6,7,8,9,10]
    ax1 = plt.subplot(212)
    ax1.bar(x,l,align="center")
    ax1.set_title("predicted values")
    y=[2,2,2,2,1,1,1,1,1,1]
    
    ax2 = plt.subplot(211)
    ax2.bar(x, y,align='center')
    ax2.set_title("Actual values")
    ax1.set_xticks([0,1,2,3,4,5,6,7,8,9])
    ax2.set_xticks([0,1,2,3,4,5,6,7,8,9])
    ax1.set_yticks([1,2])
    ax2.set_yticks([1,2])
    ax1.set_yticklabels(['Male','Female'])
    ax2.set_yticklabels(['Male','Female'])
    plt.subplots_adjust( wspace=0.05, hspace=0.4)
    plt.show()
    
