import cv2
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
def click_event(event,x,y,flags,params):
    if event==cv2.EVENT_RBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x)+" , "+str(y)
        cv2.putText(frame,text,(x,y),font,1,(10,10,10),1,cv2.LINE_AA)
        cv2.imshow('display',frame)
        cv2.waitKey(1500)
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=str(frame[y,x,0])
        green=str(frame[y,x,1])
        red=str(frame[y,x,2])
        text2=red+","+green+","+blue
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,text2,(x,y),font,0.5,(0,0,255),1,cv2.LINE_AA)
        cv2.imshow('display',frame)
        cv2.waitKey(1500)
while (cap.isOpened()):
    ret, frame=cap.read()
    if (ret):
        frame=cv2.flip(frame,flipCode=1)
        cv2.putText(frame,'Know your RGB',(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1,cv2.LINE_AA)
        cv2.imshow('display',frame)
        cv2.setMouseCallback('display',click_event)
        if (cv2.waitKey(1)==ord('q')):
            text="Closing..."
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,text,(30,40),font,1,(255,255,255),1,cv2.LINE_AA)
            cv2.imshow('display',frame)
            cv2.waitKey(1000)
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
