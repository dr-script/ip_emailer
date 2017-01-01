#Import needed modules
from ipgrabber import ipGet
import time
from emailer import emailer

#Variables
ipAddress = ipGet()
version = 'v12.15.16'

#Add time so it runs this code every 6 hours
def delay(x):
    time.sleep(x)

#Start menu to get current IP Address or run email-er
def intro():
    print('Welcome To IP Request',
          '\n     ',version)
    delay(1)
    selection()

def selection():
    print('\nChoose From The Following: \n'
          '\nEnter 1 to request IP Address'
          '\nEnter 2 to Run IP Emailer\n')
    delay(.5)
    userInput = input('Choice: ')

    if userInput == '1':
        print('')
        print('Your IP Address is:', ipAddress)
        delay(2)
        selection()

    elif userInput == '2':
        emailer()

    else:
        print('Incorrect Choice.')
        selection()

intro()

