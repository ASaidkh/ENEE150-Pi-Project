import RPi.GPIO as GPIO 
import time
 
SENSOR_PIN = #add sensor pin
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
 
while True:
    if GPIO.input() == 1: #insert sensor_pin as argument
        print ("motion detected")
        time.sleep(0.1)
    elif GPIO.input() == 0:
        print ("no motion")
        time.sleep(0.1)
    else:
        print("No input")
        time.sleep(0.1)


GPIO.cleanup()