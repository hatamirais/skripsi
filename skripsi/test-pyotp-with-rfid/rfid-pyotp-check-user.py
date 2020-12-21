import time
import RPi.GPIO as GPIO
import mysql.connector
import pyotp
from mfrc522 import SimpleMFRC522
import display
#from servo import *
from servo2 import *
from gpiozero import Servo


db = mysql.connector.connect(
    host="localhost",
    user="pyotpAdmin",
    passwd="hatami007",
    database="pyotpTestRFID"
)

cursor = db.cursor()
reader = SimpleMFRC522()
mylcd = display.lcd()


try:
    while True:
        #lock()
        myServo.min()
        print("Place card near the scanner")
        mylcd.lcd_display_string("Place card near",1)
        mylcd.lcd_display_string("the scanner",2)
        id, text = reader.read()
        cursor.execute("Select id, name, secret From users Where rfid_uid="+str(id))
        result = cursor.fetchone()
        
        if cursor.rowcount >= 1:
            mylcd.lcd_clear()
            print("Welcome, ", result[1])
            mylcd.lcd_display_string("Welcome",1)
            mylcd.lcd_display_string(result[1],2)
            time.sleep(2)
            mylcd.lcd_clear()
            print("Type the code from your authenticator")
            mylcd.lcd_display_string("Type in the code",1)
            
            cursor.execute("Select secret From users Where rfid_uid="+str(id))
            secret = result[2]
            

            totp = pyotp.TOTP(str(secret))
            otp = totp.now()
            
            your_code = input('')
            
            mylcd.lcd_display_string(your_code,2)
            
            if your_code == otp:
                mylcd.lcd_clear()
                print("Code Valid, Opening the door")
                mylcd.lcd_display_string("Code Valid",1)
                mylcd.lcd_display_string("Opening the door",2)
                myServo.mid()
                #unlock()
                time.sleep(5)
                myServo.min()
            else:
                mylcd.lcd_display_string("Invalid Code",1)
                print("Invalid")
                
            time.sleep(5)
            mylcd.lcd_clear()
            
            
except KeyboardInterrupt:
    mylcd.lcd_clear()
    print("\nApplication Stopped")

finally:
    GPIO.cleanup()