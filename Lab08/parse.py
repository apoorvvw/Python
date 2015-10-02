#!/usr/local/bin/python3.4

__author__ = 'ee364e10'

import sys

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Usage: parse.py [filename]")
        exit

    filename = sys.argv[1]
    # print("The filename sis : " , filename)
    c = 0
    try:
        with open(filename,"r") as inputFile:
                for line in inputFile:
                    if c is not 0:
                        str = ""
                        sum = 0
                        count = 0
                        avg = 0
                        x = line.split()
                        length = len(x)
                        # print("Length is ",length)
                        for i in x:
                            try:
                                sum += float(i)
                            except(ValueError):
                                str += i
                                str += " "
                                count += 1
                        # print("Length - Count  is ",length - count)
                        if count is not  0:
                            avg = sum / (length - count)
                        else:
                            avg = sum / length
                        # print(avg , str)
                        sys.stdout.write("{0:.3f} {1}\n".format(avg , str))
                    else:
                        sys.stdout.write(line)
                    c +=1
    except IOError:
        print(filename , "is not a readable file.")
