__author__ = 'Evren Esat Ozkan'
# LoginDyn
#
# DynDns forcing free users to login montly.
# This snippet automates login process and emails to you IF CAN'T login to site.
# Attach this to a montly cron job

import smtplib
import mechanize

try:
    from settings import *
except ImportError:
    dyn_username = ''
    dyn_password = ''
    gmail_username = ''
    gmail_password = ''
    receiver = ''
    msg = 'FAILED TO LOGIN DYNDNS'


def logindyn():
    br = mechanize.Browser()
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) '
                                    'Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.open("https://account.dyn.com/entrance/")
    br.select_form(nr=0)
    br['username'] = dyn_username
    br['password'] = dyn_password
    return 'Change Password' in br.submit().read()


def notify():
    message = 'Subject: %s\n\n%s' % (msg, msg)
    if gmail_username and gmail_password and receiver:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(gmail_username, gmail_password)
        server.sendmail(gmail_username, receiver, message)
        server.quit()
    else:
        print("Mail isn't properly configured, can not notify")

if __name__ == '__main__':
    if not logindyn():
        notify()
        print("Something gone wrong")
    else:
        print("it's alright!")
