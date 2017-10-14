import cv2
import time

cap = cv2.VideoCapture(0)
cap.set(3, 1280) #WIDTH
cap.set(4, 720) #HEIGHT

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

take_foto = False
#select wait-time for new pictures to be taken 
wait = 5
i = 0
j = 0

while(True):
    # Capture frame-by-frame
    sec = int(round(time.time()))
    ret, frame = cap.read()
    
    #take foto when createria are met
    if take_foto==True and j<6:
        cv2.imwrite('Doormen\Doorman'+str(i)+'.png',frame)
        take_foto = False
        
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    #
    if (sec%wait) == 0 and j == 6:
        sec_prev = sec
        j = 0
        
    # Display the resulting frame
    for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]
         if h>300 and j<6:
            take_foto=True
            i += 1
            j += 1
         
    cv2.imshow('Doorcam',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
