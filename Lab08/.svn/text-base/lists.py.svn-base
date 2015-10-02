#!/usr/local/bin/python3.4
__author__ = 'ee364e10'

import numpy
import math



def find_median(list1, list2 ):
    merge = []

    print("First List: " , list1[:])
    print("Second List: ", list2)

    for i in list2:
        merge.append(i)
    for j in list1:
        merge.append(j)
    merge.sort()

    # median = numpy.median(merge)
    x = math.floor((len(merge)-1)/2)

    median = merge[x]

    median_flag = 1
    median = math.floor(median)
    List = []
    List.append(median)
    List.append(merge)
    tup = tuple(List)
    if median_flag == 0:
        print("Merged list: Not Implemented")
        print("Median: Not  Implemented")
    else:
        print("Merged list: " , tup[1])
        print("Median: " , tup[0])
    return tup

if __name__ == "__main__":
    merge_flag = 0
    median_flag = 0
    median = 0
    merge = []

    l_1 = input("Enter the first list of numbers: ")
    l1 = l_1.split()

    l_2 = input("Enter the second list of numbers: ")
    l2 = l_2.split()

    numl1 = []
    for i in l1:
        numl1.append(int(i))

    numl2 = []
    for j in l2:
        numl2.append(int(j))

    tup_out = find_median(numl1 , numl2)

