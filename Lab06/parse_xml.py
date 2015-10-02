#!/usr/local/bin/python3.4

__author__ = 'ee364e10'

import re
def convertToAttrib():
    x = 0
    y = 0
    point = 0
    ID = 0
    flag = 0
    with open("points.xml","r") as inputFile:
        FileObject = open('points_out.xml',"w")
        FileObject.write("<?xml version=\"1.0\"?>\n")
        FileObject.write("<coordinates>\n")
        for line in inputFile:
            str = line
            str = re.search(r'<.*>', str)
            if str != None:
                str = (str.group().strip('>').strip('<').strip('/'))
               # print(str)
                if str == 'point':
                    point = 1
                elif str[0] == 'X':
                    x = 1
                elif str[0] == 'Y':
                    y = 1
                elif str[0] == 'I':
                    ID = 1
                if ID == 1:
                    id = str[3] + str[4]
                    #print(id)
                    ID = 0
                    flag += 1
                if y == 1:
                    yy = str
                    yy = yy.strip('Y').strip('/').strip('<').strip('>')
                    #print(yy)
                    y = 0
                    flag += 1
            if x == 1 and str == None:
                    xx = line
                    x = 0
                    flag += 1
                    #print(xx)
            #print(flag)
            if flag == 3:
                kk = "\t<point ID=\"" + id.strip() + "\" X=\""+xx.strip() +"\" Y=\""+yy.strip()+"\" />\n"
                FileObject.write(kk)
                flag = 0
        FileObject.write("</coordinates>")
        FileObject.close();


def getGenres():
    list = []
    count = 1
    with open("books.xml","r") as inputFile:
        print("File opened")
        for line in inputFile:
            str = re.search(r'<.*>', line)
            if str != None:
                if str.group()[1] == 'g':
                    genre = (str.group().strip('<').strip('>').strip('genre').strip('<').strip('>').strip('/').strip('<'))
                    if count == 1:
                        list.append(genre)
                        count += 1
                    if genre not in list:
                        list.append(genre)
    list.sort()
    print(list)
    return list

def getAuthorOf(bookName):
    author = None
    with open("books.xml","r") as inputFile:
        print("File opened")
        for line in inputFile:
            str = re.search(r'<.*>', line)
            if str != None:
                if str.group()[1] == 'a':
                    author = (str.group().strip('<').strip('>').strip('author').strip('<').strip('>').strip('/').strip('<'))
                if str.group()[1] == 't':
                    b = (str.group().strip('<').strip('>').strip('title').strip('<').strip('>').strip('/').strip('<'))
                    if b == bookName:
                        return author
    return None

def getBookInfo(bookID):
    author = None
    flag = 0
    with open("books.xml","r") as inputFile:
        print("File opened")
        for line in inputFile:
            str = re.search(r'<.*>', line)
            if str != None:
                if str.group()[1] == 'b':
                    id = str.group().strip('<').strip('>').strip('book').strip().strip('id').strip('=').strip('"')
                    #print(id)
                    flag = 1
                if str.group()[1] == 'a':
                    author = (str.group().strip('<').strip('>').strip('author').strip('<').strip('>').strip('/').strip('<'))
                if str.group()[1] == 't':
                    b = (str.group().strip('<').strip('>').strip('title').strip('<').strip('>').strip('/').strip('<'))
                if  flag ==1 and id == bookID :
                    l= []
                    l.append(b)
                    l.append(author)
                    tuple(l)
                    return l
    return None

def getBooksby(authorName):
    list = []
    with open("books.xml","r") as inputFile:
        print("File opened")
        for line in inputFile:
            str = re.search(r'<.*>', line)
            if str != None:
                if str.group()[1] == 'a':
                    author = (str.group().strip('<').strip('>').strip('author').strip('<').strip('>').strip('/').strip('<'))
                if str.group()[1] == 't':
                    b = (str.group().strip('<').strip('>').strip('title').strip('<').strip('>').strip('/').strip('<'))
                    if author == authorName:
                        list.append(b)
    return list

def getBooksBelow(bookPrice):
    list = []
    count = 0
    with open("books.xml","r") as inputFile:
        print("File opened")
        for line in inputFile:
            str = re.search(r'<.*>', line)
            if str != None:
                if str.group()[1] == 't':
                    b = (str.group().strip('<').strip('>').strip('title').strip('<').strip('>').strip('/').strip('<'))
                if str.group()[1] == 'p' and str.group()[2] == 'r':
                    bp = (str.group().strip('<').strip('>').strip('price').strip('<').strip('>').strip('/').strip('<'))
                    bp = float(bp)
                    if bp < bookPrice:
                        list.append(b)
    return list

def searchForWord(word):
    list = []
    with open("books.xml","r") as inputFile:
        print("File opened")
        for line in inputFile:
            str = re.search(r'<.*>', line)
            if str != None:
                if str.group()[1] == 't':
                    b = (str.group().strip('<').strip('>').strip('title').strip('<').strip('>').strip('/').strip('<'))
                    b_list = b.split()
                    if word in b_list:
                        list.append(b)
                if str.group()[1] == 'd' and str.group()[2] == 'r':
                    des = (str.group().strip('<').strip('>').strip('description').strip('<').strip('>').strip('/').strip('<'))
                    des_list = des.split();
                    if word in des_list:
                        list.append(b)
    return list
    pass

if __name__ == "__main__":
    a= searchForWord("Grail")
    print(a)