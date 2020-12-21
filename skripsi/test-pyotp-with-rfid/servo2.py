import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep

myGPIO = 15

myCorrection = 0.45
maxPW = (2.0 + myCorrection)/1000
minPW = (1.0 - myCorrection)/1000

myServo = Servo(myGPIO, \
                min_pulse_width = minPW,\
                max_pulse_width = maxPW)
'''
def lock():
    myServo.min()
    return

def unlock():
    myServo.mid()
    return
'''
'''
try:
    while True:
        print("Unlock")
        unlock()
        sleep(4)
        print("Lock")
        lock()
        sleep(4)
        
except KeyboardInterrupt:
    print("Stoped")

finally:
    GPIO.cleanup()

'''