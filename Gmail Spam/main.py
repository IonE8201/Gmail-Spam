import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os

'''
Please Use This App Moderately! Otherwise, this is the article. And You Be Have Problems.
'''

try:    
    time.sleep(1.5)
    a = input("Please write your gmail: ")
    b = input("Please write your password: ")
    c = input("Please write gmail-victim: ")
    d = input("Please write your message: ")
    time.sleep(1)
    print("*WARNING* STARTED *WARNING*")
    time.sleep(1)

    SentValue = 0

    while True:
        from_email = a
        password = b
        
        msg = MIMEMultipart()
        
        to_email = c
        message = d
        
        msg.attach(MIMEText(message, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        SentValue += 1

        print('Sent')

        from_email = a
        password = b
        
        msg = MIMEMultipart()
        
        to_email = c
        message = d
        
        msg.attach(MIMEText(message, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        SentValue += 1

        print('Sent')

        from_email = a
        password = b
        
        msg = MIMEMultipart()
        
        to_email = c
        message = d
        
        msg.attach(MIMEText(message, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        SentValue += 1

        print('Sent')

        if SentValue >= 20:
            print("Sent Value Has Reached 20")
            time.sleep(3)
            os.system("cls")
            break
        else:
            None

except smtplib.SMTPAuthenticationError:
    print("%UNKNOWN PASSWORD OR USERNAME%")
    time.sleep(3)
except TypeError:
    print("%FILL IN FIELDS%")
    time.sleep(3)
except UnicodeDecodeError:
    print("%PLEASE CHECK YOUR FIELDS, BEACUSE ERROR IN FIELD RAISE THE ERROR [UnicodeDecodeError]%")
    time.sleep(3)
except UnicodeEncodeError:
    print("%PLEASE CHECK YOUR FIELDS, BEACUSE ERROR IN FIELD RAISE THE ERROR [UnicodeEncodeError]%")
    time.sleep(3)
