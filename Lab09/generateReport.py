#!/usr/local/bin/python3.4
__author__ = 'ee364e10'

import re
def moreReg(filename):

    dict=[]

    with open(filename,"r") as inputFile:
       FileObject = open('finalGrades.xml',"w")
       FileObject.write("<?xml version=\"1.0\"?>\n")
       FileObject.write("<students>\n")
       for line in inputFile:

           f = re.search(r'<(?P<id>\w{3})>(?P<name>.*):\[',line)



           # AT this point I have the name and the id. Now generate the course grades and stuff
           if f:
               FileObject.write("   <student name=\""+f.group("name")+"\" id=\""+f.group("id")+"\">\n")
               print(f.group("id"))

               ff = re.search(r':(.*)<',line)
               g = ff.group(1)

               if g[8] == ",":
                   gg = g.strip().split(",")
               elif g[8] == ";":
                   gg = g.strip().split(";")
               for i in gg:
                   i = i.strip()
                   j = i.strip("[").strip("]")

                   course = j.split(":")[0]
                   marks = j.split(":")[1]

                   # dict[course] = marks

                   print(int(marks))

                   letter = 'A'

                   if int(marks)>=90 and int(marks)<=100:
                       letter = 'A'
                   elif int(marks)>=80 and int(marks)<90:
                       letter = 'B'
                   elif int(marks)>=70 and int(marks)<80:
                       letter = 'C'
                   elif int(marks)>=60 and int(marks)<70:
                       letter = 'D'
                   elif int(marks)<60:
                       letter = 'F'
                   print(course+" : "+marks+" : "+letter)
                   # fg = re.search(r'<(?P<course>ECE\d{3})\sscore=\"(?P<marks>\d{2})\"\sgrade=\"(?P<grade>[A-Z]?)\"/>',line)
                   FileObject.write("      <ECE"+course+ " score=\""+marks+"\" grade=\""+letter+"\"" +">\n")
               FileObject.write("   </student>\n")

       FileObject.write("</students>\n")

if __name__ == "__main__":
    a= moreReg('rawGrades.xml')


    # f = re.search(r'<(?P<course>ECE\d{3})\sscore=\"(?P<marks>\d{2})\"\sgrade=\"(?P<grade>[A-Z]?)\"/>',line)
