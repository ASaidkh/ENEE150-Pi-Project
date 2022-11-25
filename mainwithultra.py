from sensor import *
from sendingemail import *
from camera import *

sender = Emailer()
sendto = 'alim.saidkhod@gmail.com'
emailSubject = "Motion Detected By Pi"

while True:
    dist = distance()
    if dist < 10: 
        print("Motion detected close by")
        recordMP4("/home/pi/video.h264", "/home/pi/video.mp4")
        emailContent = "Something detected close by at: " + ctime()
        sender.sendmail(sendto, emailSubject, emailContent, "/home/pi/video.mp4")
    else:
        print("Nothing within 10 cm")
    time.sleep(.1)