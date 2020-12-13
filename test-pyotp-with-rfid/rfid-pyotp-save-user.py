import time
import RPi.GPIO as GPIO
import mysql.connector
import pyotp
from mfrc522 import SimpleMFRC522

db = mysql.connector.connect(
    host="localhost",
    user="pyotpAdmin",
    passwd="hatami007",
    database="pyotpTestRFID"
)

cursor = db.cursor()
base32secret = pyotp.random_base32()
secret = base32secret
reader = SimpleMFRC522()

try:
    while True:
        print("Welcome")
        time.sleep(1)
        print("Place Card to register")
        id, text = reader.read()
        cursor.execute("SELECT id FROM users WHERE rfid_uid="+str(id))
        cursor.fetchone()
        
        if cursor.rowcount >= 1:
            print("Overwrite existing user?")
            overwrite = input ("Overwrite(Y/N)")
            if overwrite[0] == "Y" or overwrite [0] == "y":
                print("Overwriting user.")
                time.sleep(1)
                sql_insert = "UPDATE users SET name = %s WHERE rfid_uid=%s"
            else:
                continue;
        
        print("Type Your Name")
        name = input("Name: ")
        secret = base32secret
        sql_insert = "Insert into users (name, secret, rfid_uid) values (%s, %s, %s)"
        
        #cursor.execute(sql_insert_rfid)
        cursor.execute(sql_insert, (name, secret, id))
        db.commit()
        
        time.sleep(2)
        
        print("Registration Completed\nThank You\n")
        time.sleep(2)
        
except KeyboardInterrupt:
    print("\nApplication Stopped")

finally:
    GPIO.cleanup()