import smtplib

sender = 'arindam.roni@gmail.com'
receiver = ['arindam.roni@gmail.com']

message = """From: Arindam<arindam.roni@gmail.com>
To: Arindam<arindam.roni@gmail.com>
subject: SMTP email test

this is a test message
"""

try:
    test = smtplib.SMTP('localhost')
    test.sendmail(sender, receiver, message)
    print("successfully sent mail")
except smtplib.SMTPException:
    print("Error: unable to send mail")
