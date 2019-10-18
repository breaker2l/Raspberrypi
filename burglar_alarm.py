#maik schmidt
#Parts Needed A half sized breadboard,PIR sensor , TMP36 Temperature sensor , MCP3008-I/P analog to digitsal converter , Six female/male humper wires
from pir import *
from camera import *
from email_notification import *
import time

PIR_PIN = 23
PREFIX = 'photo/alert'
EMAIL_SERVER = 'smtp.gmail.com:587'
EMAIL_USER = 'me@example.com'
EMAIL_PWD = 't0p$ecret'

pir = PassiveInfraredSensor(PIR_PIN)
camera = Camera()
notifier = EmailNotification(EMAIL_SERVER, EMAIL_USER ,EMAIL_PWD)
i=0
last_state = False
while True:
    if (pir.motion_detected() == True):
        if (last_state == False):
            print 'INTRUDER ALERT!'
            image_file = PREFIX + '{0}.jpg'.format(i)
            camera.take_photo(image_file)
            i = i +1
            last_state = True
   else:
       if (last_state == True):
           time.sleep(1)
           last_state = False;
