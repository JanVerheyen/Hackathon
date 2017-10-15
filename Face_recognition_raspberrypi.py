from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import RPi.GPIO as GPIO
from sendmail import mail

def sendUI_update(image_name):
    file = open('UI_update.txt','w')
    file.write(image_name)
    file.close()
    


# Initialise GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Initialise camera
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=camera.resolution)

# Initialise criteria for picture taking
take_foto = False
wait_sec = 60
i = 0
j = 0 

# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Capture frame-by-frame
    sec = int(round(time.time()))    
    # Grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Take foto when createria are met
    if take_foto==True and j<6:
        cv2.imwrite('Doormen/Doorman'+str(i)+'.png',image)
        take_foto = False
    
    if (sec%wait_sec) == 0 and j == 6:
        sec_prev = sec
        j = 0
        sendUI_update('Doormen/Doorman'+str(i)+'.png')
        # Send dat mail
        mail()
    
    # Display the resulting frame
    for (x,y,w,h) in faces:
         cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),1)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = image[y:y+h, x:x+w]
         if h>50 and j<6:
            take_foto=True
            i += 1
            j += 1
        
    # Show the frame
    #cv2.imshow("Doorcam", image)
    key = cv2.waitKey(1) & 0xFF
     
    # Clear the stream in preparation for the next frame
    rawCapture.truncate(0)
     
    # If the `q` key was pressed, break from the loop
    if (not GPIO.input(27)):
        i = 0
        j = 0
        break
        

        
