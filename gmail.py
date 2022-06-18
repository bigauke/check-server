import time 
import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)

    gmail_user = 'danielinhares@gmail.com'
    gmail_password = ''
    msg['Subject'] = subject
    msg['From'] = ""
    msg['To'] = to