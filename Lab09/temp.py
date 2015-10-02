#!/usr/local/bin/python3.4

__author__ = 'ee364e10'

import re
def moreReg(filename):
    with open(filename,"r") as inputFile:
       for line in inputFile:


           f = re.search(r'<(?P<course>ECE\d{3})\sscore=\"(?P<marks>\d{2})\"\sgrade=\"(?P<grade>[A-Z]?)\"/>',line)
           if f:
               #Process the marks and shit
               print(f.group("course"))


if __name__ == "__main__":
    a= moreReg('goldGrades.xml')
    print(a)