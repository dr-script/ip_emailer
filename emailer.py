from ipgrabber import ipGet
import smtplib
import time

def delay(x):
    time.sleep(x)

def emailer():
    gmail_username = 'example@example.com'
    gmail_password = 'password'
    global x

    try:
        ip = ipGet()
        x = ip
    except:
        print('Failed to get IP Address...')
        delay(60)
        emailer()

    sender = 'your_email@email.com'
    to = ['Sending_to@email.com']
    subject = 'Current IP Address'
    body = 'Your Current IP Address:', ip

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sender, ", ".join(to), subject, body)

    try:
        conn = smtplib.SMTP('smtp.gmail.com', 587)
        print(conn.ehlo())
        print(conn.starttls())
        print(conn.login(gmail_username, gmail_password))
        conn.sendmail(sender, to, email_text)
        print(conn.quit())
        delay(1)
        print('\nEmail Sent\n')
        delay(1)
        print('IP Address emailed:', ip)
        delay(60)
        checker()
    except:
        print('\nSomething went wrong....')
        delay(300)
        emailer()

def checker():
    #global x
    try:
        y = ipGet()
    except:
        print('Error - Could not check IP')
        delay(60)
        checker()
    if y == x:
        print('\nSame IP Address')
        delay(1)
        print('\nCurrent IP:', y)
        delay(1)
        print('\nIP In Email', x)
        delay(21600)
        checker()
    else:
        delay(60)
        emailer()



