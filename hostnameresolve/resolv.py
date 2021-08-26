#!/usr/bin/env python
""" This script checks if a hostname resolves to an IP address
Text file with one hostname per line is passed as parameter
The script will output up.txt and down.txt
"""
import socket
import sys

if len(sys.argv) <= 1:
    print('Usage: resolv.py -i input')
    exit(1)

with open(sys.argv[2], "r") as ins:
    for line in ins:
        try:
            data = socket.gethostbyname_ex(line.strip('\n'))
            with open('up.txt', 'a') as f:
                print(line.strip('\n'), file=f)
        except:
            with open('down.txt', 'a') as f:
                print(line.strip('\n'), file=f)
