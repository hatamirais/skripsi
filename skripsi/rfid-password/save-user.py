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

cursor = db.cursor()
reader = SimpleMFRC522()


try:
    while True:
        print("Place card to register")
        id, text = reader.read()
        cursor.execute("SELECT id FROM card WHERE rfid_uid="+str(id))
        cursor.fetchone()
        
        if cursor.rowcount >= 1:
            print("Overwrite existing user?")
            overwrite = input("Overwite (Y/N)? ")
            if overwrite[0] == 'Y' or overwrite[0] == 'y':
                print("Overwriting user.")
                time.sleep(1)
                sql_insert = "UPDATE card SET name = %s WHERE rfid_uid=%s"
            else:
                continue;
        else:
            sql_insert = "INSERT INTO card (name, rfid_uid, password) VALUES (%s, %s, %s)"
        
        print('Enter new name')
        new_name = input("Name: ")
        print('Enter password')
        new_password = input("Password: ")    
        cursor.execute(sql_insert, (new_name, id, new_password))
        db.commit()
        
        print("User "+ new_name + " is saved")
        time.sleep(2)
finally:
    GPIO.cleanup()