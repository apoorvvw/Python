#!/usr/local/bin/python3.4

__author__ = 'ee364e10'

import sys
import os
import string
import re

def expressionGroups(filename):
    u = 'Error'
    if os.path.exists(filename) and os.R_OK:
        with open(filename, 'r') as inputFile:
            for line in inputFile:
                f = re.findall(r"def\s+(([a-z][A-Z])(\w|-|__)+)\((,*)\)", line)
                list = []
                if f:
                    for i in f:
                        for j in i:
                            list.append(j)
                        Name = list[0]
                        print (Name)
                        args = list[-1].split(',')
                        argList = []
                        for arg in args:
                            argList.append(arg.strip())
                        len1 = len(argList)
                        i = 0
                        while i < len1:
                            print("Arg"+str(i+1) + ": "+str(argList[i]))
                            i += 1
                else:
                    print(u + ": Cannot read " + filename)


if __name__ == "__main__" :
    expressionGroups('module2.in')
