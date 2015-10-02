#! /usr/bin/env python3.4
__author__ = 'ee364e10'

import glob

def generateReportForAllUser():
    f = open("users.txt")
    directoryUsers = {}
    count = 0
    for line in f:
        if count ==1 or count == 0:
            count = count + 1
        else:
            a = line.split("|")
            fullName = a[0]

            b = fullName.split(",")
            fName = b[0]
            lName = b[1].strip()

            userID = a[1].strip()

            directoryUsers[userID] = fName + " " + lName

    #At this point there is a dictionary relating usernames to their IDs

    files = glob.glob('/home/ecegrid/a/ee364e10/ee364e10/Lab04/reports/report*')
    dict={}
    for f in files:
        count = 0
        with open(f,"r") as inputFile:
            total = 0.00
            summer = 0
            for line in inputFile:
                lister = []
                count += 1

                if count == 1:
                    c = line.split(":")
                    userID = c[1].strip()
                    continue
                    #print("({})".format(userID))
                elif count == 2 or count == 3 or count == 4:
                    continue

                 #So far we have the usernames

                d = line.split()
                summer += int(d[2])
                q = d[3].split("$")
                total += float(q[1])

                lister.append(summer)
                lister.append(total)

                tupler = tuple(lister)

                s = directoryUsers[userID]
                dict[s] = tupler

                #print("({} : {})".format(s,dict[s]))
    #dict = dict.sort()
    return dict

def generateReportForAllViruses():
    files = glob.glob('/home/ecegrid/a/ee364e10/ee364e10/Lab04/reports/report*')
    dict={}
    for f in files:
        count = 0
        total = 0.00
        summer = 0
        with open(f,"r") as inputFile:

            for line in inputFile:
                lister = []
                count += 1
                if count == 1:
                    c = line.split(":")
                    userID = c[1].strip()
                    continue
                    #print("({})".format(userID))
                elif count == 2 or count == 3 or count == 4:
                    continue

                 #So far we have the usernames

                d = line.split()    #This is the whole line
                summer += int(d[2]) #Total number of users

                q = d[3].split("$") #Split the dollar amount
                total += float(q[1])#Add to total

                lister.append(summer)
                lister.append(total)
                tupler = tuple(lister)

                s = d[1].strip()
                dict[s] = tupler
                dict[s]
                #print("({} : {})".format(s,dict[s]))
    return dict

def getUserWithoutReports():
    usersWITH = generateReportForAllUser();
    f = open("users.txt")
    directoryUsers = []
    count = 0
    i = 0
    s = set()
    for line in f:
        if count ==1 or count == 0:
            count = count + 1
        else:
            a = line.split("|")
            fullName = a[0]

            b = fullName.split(",")
            fName = b[0]
            lName = b[1].strip()

            userID = a[1].strip()

            directoryUsers.append(fName + " " + lName)


    ret = []
    for i in directoryUsers:
        r = usersWITH.get(i,"False")
        if r == "False3":
            ret.append(i)

    return ret

def getTotalSpending():
    f = open("users.txt")
    directoryUsers = {}
    count = 0
    for line in f:
        if count ==1 or count == 0:
            count = count + 1
        else:
            a = line.split("|")
            fullName = a[0]

            b = fullName.split(",")
            fName = b[0]
            lName = b[1].strip()

            userID = a[1].strip()

            directoryUsers[userID] = fName + " " + lName

    #At this point there is a dictionary relating usernames to their IDs

    files = glob.glob('/home/ecegrid/a/ee364e10/ee364e10/Lab04/reports/report*')
    dict={}
    total = 0.00
    summer = 0
    for f in files:
        count = 0
        with open(f,"r") as inputFile:
            for line in inputFile:
                lister = []
                count += 1

                if count == 1:
                    c = line.split(":")
                    userID = c[1].strip()
                    continue
                    #print("({})".format(userID))
                elif count == 2 or count == 3 or count == 4:
                    continue

                 #So far we have the usernames

                d = line.split()
                summer += int(d[2])
                q = d[3].split("$")
                total += float(q[1])

                lister.append(summer)
                lister.append(total)

                tupler = tuple(lister)

                s = directoryUsers[userID]
                dict[s] = tupler

                #print("({} : {})".format(s,dict[s]))
    #dict = dict.sort()
    return total

if __name__ == "__main__":
    a= getUserWithoutReports()
    print(a)