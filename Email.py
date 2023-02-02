
from email.message import EmailMessage
import ssl
import smtplib

email_sender = ""
email_password = ''
email_receiver = input("Send to: ")

subject = input("Subject: ")
body = input("Enter message: ")

em = EmailMessage()
em['From'] = email_sender
em['To']=  email_receiver
em['subject']= subject
em.set_content(body)

context = ssl._create_unverified_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())
print("e-mail sent!")
