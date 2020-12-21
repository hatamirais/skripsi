import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep

servo = Servo(15)

try:
    while True:
        print("min")
        servo.min()
        sleep(3)
        print("mid")
        servo.mid()
        sleep(3)
        print("max")
        servo.max()
        sleep(3)

except KeyboardInterrupt:
    servo.min()
    print("Stoped")

finally:
    GPIO.cleanup()

