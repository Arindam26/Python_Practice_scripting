import smtplib

sender = 'arindam.roni@gmail.com'
receiver = 'arindam.roni@gmail.com'

message = """From: {}
To: {}
Subject: SMTP test

This is a test message""".format(sender, receiver)

try:
    smptpObj = smtplib.SMTP('localhost')
    smptpObj.sendmail(sender, receiver, message)
    print("Successfully sent mail")
except smtplib.SMTPException as e:
    print("Unable to send the mail", e)
