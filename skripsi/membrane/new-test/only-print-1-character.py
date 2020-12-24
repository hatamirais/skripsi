from pad4pi import rpi_gpio
import RPi.GPIO as GPIO
import time

KEYPAD = [
    [1, 2, 3, "A"],
    [4, 5, 6, "B"],
    [7, 8, 9, "C"],
    ["*", 0, "#", "D"]
]

ROW_PINS = [5,6,13,19] # BCM numbering
COL_PINS = [12,16,20,21] # BCM numbering


def printKey(key):
    print(key)

# printKey will be called each time a keypad button is pressed
try:
    factory = rpi_gpio.KeypadFactory()

    keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
    
    keypad.registerKeyPressHandler(printKey)
    
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Closing")
finally:
    GPIO.cleanup()