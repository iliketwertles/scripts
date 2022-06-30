#!/usr/bin/env python
import sys
import os
import subprocess

ulib = '~/.config/tfetch/library/'

def neofetch(arg1):
    n = 'neofetch --ascii '
    cmd = n + arg1
    subprocess.run(cmd)

#checking if library exists
if os.path.isfile(ulib) == False:
    print('Library not found, creating empty directory...\n*Note this will be empty until you fill it*')
    os.mkdir(ulib)

ascii = ulib + sys.argv[1]
if os.path.isfile(ascii) == False:
    print('No file in library with that name')
    neofetch(' ')
else:
    neofetch(ascii)
