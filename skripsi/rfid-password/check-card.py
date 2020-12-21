#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="admin-_rfid",
    passwd="hatami007",
    database="rfid_password"
)

password = "1234"

cursor = db.cursor()
reader = SimpleMFRC522()

try:
    while True:
        print("Place card near the scanner")
        id, text = reader.read()
        cursor.execute("SELECT id FROM card WHERE rfid_uid="+str(id))
        result = cursor.fetchone()

        if cursor.rowcount >= 1:
            print("Welcome")
            time.sleep(1)
            print("Please type in your password")
            password_check = input("Password: ")
            if password_check == password:
                print("Code correct")
                time.sleep(1)
                print("Opening the door")
                cursor.execute("INSERT INTO log (user_id) VALUES (%s)", (result[0],) )
            else:
                print("Incorrect Password")
            db.commit()
        else:
            print("User does not exist.")
        time.sleep(2)

except KeyboardInterrupt:
    print("\nApplication Stopped")

finally:
    GPIO.cleanup()
