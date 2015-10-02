#!/usr/local/bin/python3.4
__author__ = 'ee364e10'
import re
def simpleRegExpression(filename):
    with open(filename,"r") as inputFile:
        for line in inputFile:
            str = line
            str = re.sub(r'(\d+).(\d+)', r'\1.\2/100', str)
            match = re.search(r'@[\w\.-]+', str)
            # print(match.group())
            if match:
                a = match.group()
                if a == "@purdue.edu":
                    print(re.sub(r'@[\w\.-]+', '@ecn.purdue.edu' , str))
                else:
                    print(line)


if __name__ == "__main__":
    a = [1,2,3,5,6,7]
    a= simpleRegExpression('Part2.in')
    print(a)