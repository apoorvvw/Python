#!/usr/local/bin/python3.4


__author__ = 'ee364e10'

"""
Lab05 for ECE 364
"""
import glob
def getLargestProduct():
    print()


def getListProduct(numList):
    prod = 1
    for i in numList:
        prod = prod * i
    print(prod)
    return prod

def partition(numList,n):
    L=[]
    #print(numList)
    count = 0
    x=len(numList)
    for j in range(x-3):
        print(numList[j:j+4])
        L.append(numList[j:j+4])
        count = count + 1
    return L

def gertLargestPartition(numList,n):
    K = []
    R = partition(numList,n)
    max = 0
    for i in R:
        E=[]
        print(i)
        prod = getListProduct(i)
        E.append(i)
        if max < prod:
            max = prod
            E.append(max)
            K.append(tuple(E))
    return K

def getDirectory():
    f = glob.glob('Phone*')
    dicT = {}
    with open("Phone Directory.txt","r") as inputFile:
        for line in inputFile:
            a = line.split()
            name=[]
            name.append(a[0].strip())
            name.append(a[1].strip())
            name.append(a[2].strip())
            nameT =  tuple(name)
            c = a[3]
            d = a[4]
            dicT[nameT] = c + " " + d
    return dicT

def getPhoneByPartialName(name):
    L=[]
    dic = getDirectory()
    for key in dic.keys():
        #print(dic[key])
        if ( name == key[0] or name == key[2]):
            L.append(dic[key])
    return L

def reverseLookUp(areaCode):
    f = glob.glob('Phone*')
    dicT = {}
    with open("Phone Directory.txt","r") as inputFile:
        for line in inputFile:
            a = line.split()
            name=[]
            name.append(a[0].strip())
            name.append(a[1].strip())
            name.append(a[2].strip())
            nameT =  tuple(name)
            c = a[3].strip(")").strip("(")
            dicT[c] = nameT
    L = []
    for key in dicT.keys():
        #print(key)
        if ( areaCode == key):
            L.append(dicT[key])
    return L

if __name__ == "__main__":
    a = [1,2,3,5,6,7]
    a= partition(a,2)
    print('HEllo')
    print(a)