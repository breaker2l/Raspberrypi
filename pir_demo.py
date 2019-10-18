from pir import *
import time

PIR_PIN = 23
pir = PAssiveInfraredSensor(PIR_PIN)

last_state = False
while True:
     if (pir.motion_detected() == True):
         if (last_state == False):
             print("Movement detected")
             last_state = True
             
     else:
         if (last_state == True):
             print("No movement detected")
             time.sleep(2)
             last_state = False;
