import time
import RPi.GPIO as GPIO
import mysql.connector
import pyotp
from mfrc522 import SimpleMFRC522
from gpiozero import Servo
from gpiozero import LED
from time import sleep

myGPIO=17 #GPIO 17, pin 11
led = LED(24) #GPIO 24, pin 18
 
servo = Servo(myGPIO)

db = mysql.connector.connect(
    host="localhost",
    user="pyotpAdmin",
    passwd="hatami007",
    database="pyotpTestRFID"
)

cursor = db.cursor()
cursor = db.cursor(buffered = True)
reader = SimpleMFRC522()

try:
    while True:
        
        servo.min() #lock
        led.on()
        print("Place card near the scanner")
        id, text = reader.read()
        cursor.execute("Select id, name, secret From users Where rfid_uid="+str(id))
        result = cursor.fetchone()
        
        if cursor.rowcount >= 1:
            print("Welcome, ", result[1])
            time.sleep(2)
            print("Type the code from your authenticator")
 
            count = 0
            while count < 3:
                cursor.execute("Select secret From users Where rfid_uid="+str(id))
                secret = result[2]
                totp = pyotp.TOTP(str(secret))
                otp = totp.now()
                
                code = input('')
                if code == otp:
                    led.off()
                    print("Code Valid, Opening the door")
                    servo.max() # unlock
                    time.sleep(2)
                    break
                else:
                    print("Invalid, Try again!")
                    count += 1
            if count == 3:
                print("Contact admin")
                
            time.sleep(2)

except KeyboardInterrupt:
    print("\nApplication Stopped")

finally:
    GPIO.cleanup()

