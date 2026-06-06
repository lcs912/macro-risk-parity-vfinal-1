import smtplib
import os
from email.mime.text import MIMEText

def send_email(msg):

    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    receiver = os.getenv("EMAIL_TO")

    mail = MIMEText(msg)
    mail["Subject"] = "Macro Risk Parity Daily Signal"
    mail["From"] = sender
    mail["To"] = receiver

    server = smtplib.SMTP("smtp.qq.com", 587)
    server.starttls()

    server.login(sender, password)
    server.sendmail(sender, receiver, mail.as_string())
    server.quit()
