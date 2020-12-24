from pad4pi import rpi_gpio
import RPi.GPIO as GPIO
import time

KEYPAD = [
    [1, 2, 3, "A"],
    [4, 5, 6, "B"],
    [7, 8, 9, "C"],
    ["*", 0, "#", "D"]
]

password = "1234"
type_password = ""

ROW_PINS = [5,6,13,19] # BCM numbering
COL_PINS = [12,16,20,21] # BCM numbering

def cleanup():
    global keypad
    keypad.cleanup()

def correct_passcode_entered():
    print("Passcode accepted. Access granted.")
    
def incorrect_passcode_entered():
    print("Incorrect passcode. Access denied.")

def digit_entered(key):
    global type_password, password

    type_password += str(key)
    print(type_password)

    if len(type_password) == len(password):
        if type_password == password:
            correct_passcode_entered()
        else:
            incorrect_passcode_entered()

def non_digit_entered(key):
    global type_passwowrd

    if key == "*" and len(type_password) > 0:
        type_passwowrd = type_password[:-1]
        print(type_password)

def printKey(key):
    print(key)
    
def key_pressed(key):
    try:
        int_key = int(key)
        if int_key >= 0 and int_key <= 9:
            digit_entered(key)
    except ValueError:
        non_digit_entered(key)
        
try:
    factory = rpi_gpio.KeypadFactory()

    keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
    
    keypad.registerKeyPressHandler(key_pressed)
    
    print("Enter your password ")
    print("Press * to clear previous digit.")
    
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Closing")
finally:
    GPIO.cleanup()