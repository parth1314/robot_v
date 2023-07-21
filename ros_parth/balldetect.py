import cv2
import numpy as np
cap=cv2.VideoCapture(0)
lower_range=np.array([126,188,47])
upper_range=np.array([179,255,255])
lower_range1=np.array([66,155,40])
upper_range1=np.array([98,255,255])
lower_range2=np.array([88,176,70])
upper_range2=np.array([133,255,255])

def blue(img):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_range2,upper_range2)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    g=[]
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            g.append(x)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,("DETECT"),(10,60),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
    print('Number of blue balls : ',str(len(g)))



def green(img):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_range1,upper_range1)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    b=[]
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            b.append(x)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,("DETECT"),(10,60),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
    print('Number of green balls : ',str(len(b)))

def red(img):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_range,upper_range)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    a = []
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            a.append(x)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame,("DETECT"),(10,60),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
    print('Number of red balls : ',str(len(a)))  

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    red(frame)
    green(frame)
    blue(frame)

    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()