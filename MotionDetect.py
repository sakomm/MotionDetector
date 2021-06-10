import cv2
import numpy as np
from datetime import datetime


path = "C:\\Users\\sakom\\OneDrive\\Pictures\\3Motion"

threshold = 0
avgVal = 0
avgPrev = 0

vid = cv2.VideoCapture(0)

threshold = input("enter sensitivity threshold [1 - 10]: ")
  
while(True):
    ret, frame = vid.read()
    frame = cv2.GaussianBlur(frame, (7, 7), 1.41)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('img',frame)

    edge = cv2.Canny(frame, 0, 50)

    cv2.imshow('Canny Edge', edge)

    if(avgPrev == 0):
        avgPrev = np.average(edge)
    else:
        if(abs(avgPrev - np.average(edge)) > (threshold * 100)):
            now = datetime.now()
            name  = now.strftime("%d/%m/%Y %H:%M:%S")
            cv2.imwrite(name,frame)
            
    # Introduce 20 milisecond delay. press q to exit.
    if cv2.waitKey(20) == ord('q'):
        break

# time.sleep(.25)

vid.release()
cv2.destroyAllWindows()
