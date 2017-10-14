from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time


camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Display the resulting frame
    for (x,y,w,h) in faces:
         cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),1)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = image[y:y+h, x:x+w]
         
    # show the frame
    cv2.imshow("Doorcam", image)
    key = cv2.waitKey(1) & 0xFF
     
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
     
    # if the `q` key was pressed, break from the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
#take_foto = False
##select wait-time for new pictures to be taken 
#wait = 5
#i = 0
#j = 0

#while(True):
    # Capture frame-by-frame
#    sec = int(round(time.time()))
    
    #take foto when createria are met
#    if take_foto==True and j<6:
#        cv2.imwrite('Doormen\Doorman'+str(i)+'.png',frame)
#        take_foto = False
            
            
#    if (sec%wait) == 0 and j == 6:
#        sec_prev = sec
#        j = 0
        
    # Display the resulting frame
#    for (x,y,w,h) in faces:
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = frame[y:y+h, x:x+w]
#         if h>300 and j<6:
#            take_foto=True
#            i += 1
#            j += 1
        
