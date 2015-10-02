#!/usr/local/bin/python3.4
__author__ = 'ee364e10'
import sys
import vtools


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("Usage: verilog2vhdl.py [infile] [outfile]")
        exit(1)
    try:
        fp = open(sys.argv[1] , "r")
    except IOError as e:
        print("Error: ",e)
        exit(2)
    filename = sys.argv[1]
    # print("The filename sis : " , filename)
    c = 0
    try:
        with open(filename,"r") as inputFile:
                for line in inputFile:
                    try:
                        a = vtools.parse_net(line)
                    except ValueError as e:
                        print("Error: input File is not a valid Verilog port map!")
                        print(e)
                        exit(4)
    except:
        pass