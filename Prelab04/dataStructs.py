#!#!/usr/local/bin/python3.4
# __author__ = 'ee364e10'
"""
PreLab0 for ECE 364:
"""
import glob

def getWordFrequency():
    files = glob.glob('/home/ecegrid/a/ee364e10/ee364e10/Prelab04/files/*.txt')
    dict={}
    for f in files:
        with open(f,"r") as inputFile:
            for line in inputFile:
                for word in line.split():
                    if word in dict:
                        dict[word] = dict[word] + 1
                    elif word not in dict:
                        dict[word] = 1
    return dict

def getDuplicates():

    return

def getPurchaseReport():
    files = glob.glob('/home/ecegrid/a/ee364e10/ee364e10/Prelab04/purchases/*purchase*')
    dict={}
    a=[]
    transactionID = 0
    for f in files:
        with open(f,"r") as inputFile:
            count = 0
            cost = 0.00
            for line in inputFile:
                #print(count)
                if count == 1 or count == 0 :
                    count=count+1
                    continue
                else:
                    a = (line.split())
                    item = a[0]
                    cost = int(a[1]) + cost
            dict[transactionID]= cost
            #print("{} : {}".format(transactionID,dict[transactionID]))
            transactionID = transactionID + 1
    return dict

def getTotalSold():
    pass


if __name__ == "__main__":
    dict = getWordFrequency()
    for t in range(len(dict)):
        print("{} : {}".format(t,dict[t]))




