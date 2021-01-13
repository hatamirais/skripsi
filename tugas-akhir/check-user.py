import time
import RPi.GPIO as GPIO
import mysql.connector
import pyotp
from mfrc522 import SimpleMFRC522
from gpiozero import Servo
from time import sleep

myGPIO=17
 
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
        
        #Start
        
        servo.min() #lock
        print("Place card near the scanner")
        id, text = reader.read()
        cursor.execute("Select id, name, secret From users Where rfid_uid="+str(id))
        result = cursor.fetchone()
        
        if cursor.rowcount >= 1:
            start = time.time()
            print("Welcome, ", result[1])
            #time.sleep(2)
            print("Type the code from your authenticator")
            
            cursor.execute("Select secret From users Where rfid_uid="+str(id))
            secret = result[2]
            

            totp = pyotp.TOTP(str(secret))
            otp = totp.now()
            
            your_code = input('')
            
            
            if your_code == otp:
                print("Code Valid, Opening the door")
                servo.max() # unlock
                #time.sleep(2)
                end = time.time()
                print("Process finish in = ", end - start)
            else:
                print("Invalid")
                end = time.time()
                print("Process finish in = ", end - start)
                
            #time.sleep(3)
            
            #End
except KeyboardInterrupt:
    print("\nApplication Stopped")

finally:
    GPIO.cleanup()

