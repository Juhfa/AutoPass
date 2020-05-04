#!/usr/bin/env python3

import string
import random
import os
import sys
from pyfiglet import figlet_format
from termcolor import cprint

# Creates Master Directory "Passwords" on startup of application
homedir = os.path.expanduser("~")
passdir = os.path.join( homedir, ".passwords" )

cprint(figlet_format('Auto Pass'), 'magenta', attrs=['bold'])


# Takes input on the platform and creates subdir under Master dir
while True:
    platform = input("What platform is this password for: ")
    passdir = os.path.join( passdir, platform )

    if os.path.exists(passdir):
        print("That platform already exists, please choose a new platform")
    else:
        break

if not os.path.exists(passdir):
     os.makedirs(passdir)


# Func that uses letters and ints, using randchoice
def genPass(size = 8, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
# User inputs number of chars the pass should be

password_Length = int(input('How many characters in your password: '))
password = genPass(password_Length)


filepath = os.path.join(passdir, 'password.txt')



with open(filepath, 'w+') as f:
    f.write(password)


