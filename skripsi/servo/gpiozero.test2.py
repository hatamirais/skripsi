import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep

servo = Servo(15)

def lock():
    Servo.min()

def unlock():
    Servo.mid()

try:
    while True:
        print("Lock")
        lock()
        sleep(3)
        print("Unlock")
        unlock()
        sleep(3)

except KeyboardInterrupt:
    print("Stoped")

finally:
    GPIO.cleanup()