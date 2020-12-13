import time
import RPi.GPIO as GPIO
import mysql.connector
import pyotp
from mfrc522 import SimpleMFRC522
import base64

db = mysql.connector.connect(
    host="localhost",
    user="pyotpAdmin",
    passwd="hatami007",
    database="pyotpTestRFID"
)

cursor = db.cursor()
reader = SimpleMFRC522()

try:
    while True:
        print("Place card near the scanner")
        id, text = reader.read()
        cursor.execute("Select id, secret From users Where rfid_uid="+str(id))
        result = cursor.fetchone()
        
        if cursor.rowcount >= 1:
            print("Welcome")
            time.sleep(1)
            print("Type the code from your authenticator")
            
            cursor.execute("Select secret From users Where rfid_uid="+str(id))
            secret = result[1]
            
            print("Secret: ", secret)
            
            encoded = secret.encode("utf-8")
            b32encoded = base64.b32encode(encoded)
            print(b32encoded)
            
            totp = pyotp.TOTP(b32encoded)

            otp = totp.now()

            your_code = input('')
            if your_code == otp:
                print("Valid")
            else:
                print("Invalid")
            
except KeyboardInterrupt:
    print("\nApplication Stopped")

finally:
    GPIO.cleanup()
