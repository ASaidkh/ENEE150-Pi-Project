import RPi.GPIO as GPIO 
from sendingemail import *
from camera import *

sender = Emailer()
sendto = 'alim.saidkhod@gmail.com'
emailSubject = "Motion Detected By Pi"
 
SENSOR_PIN = 23
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
 
while True:
    if GPIO.input() == 1: #insert sensor_pin as argument
        print ("motion detected")
        videoh264 = '/home/pi/' + time.ctime() + '.h264'
        videoMP4 = '/home/pi/' + time.ctime() + '.h264'
        convert(videoh264, videoMP4)
        
        emailContent = "Motion Detected at: " + time.ctime()
        sender.sendmail(sendTo, emailSubject, emailContent, videoMP4)
        time.sleep(0.1)
    elif GPIO.input() == 0:
        print ("no motion")
        time.sleep(0.1)
    else:
        print("No input")
        time.sleep(0.1)


GPIO.cleanup()