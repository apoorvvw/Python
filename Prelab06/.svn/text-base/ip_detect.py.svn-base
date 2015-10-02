#!/usr/local/bin/python3.4
__author__ = 'ee364e10'

import re
def moreRegExp(filename):
    with open(filename,"r") as inputFile:
       for line in inputFile:
            u = ''
            flag = re.match(r'(0{0,2}\d+)\.(0{0,2}\d+).(0{0,2}\d+)\.(0{0,2}\d+):(\d+).*',line)
            if flag:
                u = 'Valid'
            if int(flag.group(1)) > 256 or int(flag.group(2)) > 256 or int(flag.group(3)) > 256 or int(flag.group(4)) > 256 :
                u = 'Invalid IP Address'
            if not int(flag.group(5)) <= 32767:
                u = 'Invalid Port Number'
            if int(flag.group(5)) <= 1024:
                u = 'Valid (root privileges required)'

            print(flag.group() + " " + u)

if __name__ == "__main__":
    a= moreRegExp('addys.in')
    print(a)