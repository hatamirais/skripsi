#https://www.explainingcomputers.com/pi_servos_video.html

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(10,GPIO.OUT)
servo = GPIO.PWM(10,50)

servo.start(0)

def unlock():
    servo.ChangeDutyCycle(7)

def lock():
    servo.ChangeDutyCycle(2)

        
def reset():
  unlock()  


try:
    while True:
        lock()
        #time.sleep(5)
        #unlock()
        
        
except KeyboardInterrupt:
    print("Stoped")
    servo.stop()
    servo.ChangeDutyCycle(0)

finally:
    GPIO.cleanup()
