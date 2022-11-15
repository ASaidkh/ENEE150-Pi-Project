import smtplib
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

SMTP_SERVER = 'smtp.gmail.com' 
SMTP_PORT = 587 
GMAIL_USERNAME = 'enee150piproject@gmail.com' 
GMAIL_PASSWORD = 'vnxdcrdazpbsapar'  

class Emailer:
    def sendmail(self, recipient, subject, content, video):

        
        emailData = MIMEMultipart()
        emailData['Subject'] = subject
        emailData['To'] = recipient
        emailData['From'] = GMAIL_USERNAME

        
        emailData.attach(MIMEText(content))

        videoData = MIMEApplication(open(video, 'rb').read(), 'mp4')
        videoData.add_header('Content-Disposition', 'attachment; filename="video.mp4"')
        emailData.attach(videoData)

        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

    
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

       
        session.sendmail(GMAIL_USERNAME, recipient, emailData.as_string())
        session.quit

sender = Emailer()

video = 'video.mp4'
sendTo = 'alim.saidkhod@gmail.com'
emailSubject = "test"
emailContent = "Test at: " + time.ctime()
sender.sendmail(sendTo, emailSubject, emailContent, video)
