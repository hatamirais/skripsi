#from servo import *
from servo2 import *

try:
    while True:
        text = input(" ")
        count = 0
        while count != 3:
            if text == ("unlock"):
                unlock()
            elif text == ("lock"):
                lock()
            else:
                print("Unknown Command")
            
except KeyboardInterrupt:
    print("\nApplication Stopped")

finally:
    GPIO.cleanup()