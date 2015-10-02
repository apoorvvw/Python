#!/usr/local/bin/python3.4

__author__ = 'ee364e10'
# import lists
from lists import find_median

if __name__ == "__main__":
    merge_flag = 0
    median_flag = 0
    median = 0

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
