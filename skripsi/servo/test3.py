import time
import RPi.GPIO as GPIO
from servo import *

code = ("1234")

try:
    while True:
        lock() # The rotating thingy is at 90 degree
        pass_code = input("")
        if pass_code == code:
            print("Opening the door")
            unlock() #The rotating thingy is at 0 degree
            time.sleep(10)
            print("Locking the door")
            lock() #The rotating thingy is back at 90 degree
            
except KeyboardInterrupt:
    servo.stop() # or lock(), Im not sure
    
finally:
    GPIO.cleanup()
