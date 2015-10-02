#!/usr/local/bin/python3.4

__author__ = 'ee364e10'

import sys
import os
import math
import re
from PIL import Image
from io import BytesIO
import base64


class Message:

    filePath = ""
    messageType = ""
    mess = ""
    base6 = ""
    xml = ""
    size = ""

    # Image.getData(band = None)
    # This will do the raster scan for you, and the band parameter will give R the first time by setting band = 0
    # readthedocs.org/en/latest/referance/Image.html

    def __init__(self , **kwargs):

        if len(kwargs) == 0 :
            raise ValueError

        # When a text file is given and we have to make the xml string out of it, given the filePath and the messageType
        elif 'filePath' in kwargs.keys() and 'messageType' in kwargs.keys():

            self.messageType = kwargs.pop("messageType")
            self.filePath = kwargs.pop("filePath")

            if self.messageType not in ['Text', 'GrayImage', 'ColorImage']:
                raise ValueError

            # ----------------------    TEXT  ----------------------------
            if self.messageType is 'Text':
                try:
                    with open(self.filePath,"r") as inputFile:

                        self.mess = inputFile.read()
                        self.size = len(self.mess)
                        #Base 64 encode the text
                        x = bytes(self.mess , 'UTF-8')#.encode('UTF-8')
                        self.base6 = str(base64.b64encode(x) , 'UTF-8')#.decode('UTF-8')
                except:
                    print("Text File not found")
                    raise ValueError

            # ----------------------   GRAYIMAGE  ---------------------------
            elif self.messageType is 'GrayImage':
                try:
                    img = Image.open(self.filePath)
                    # find the width and height
                    width = img.size[0]
                    height = img.size[1]
                    self.size = str(width)+","+str(height)
                    # Encode the data from the image
                    br = bytearray(img.getdata())
                    strr = base64.b64encode(br)
                    self.base6 = str(strr , 'UTF-8')

                except:
                    print("The Gray Image File cannot be opened")
                    raise ValueError

            # ----------------------   COLORIMAGE  ---------------------------
            elif self.messageType is 'ColorImage':
                try:
                    #Open image
                    img = Image.open(self.filePath , 'r')
                    width = img.size[0]
                    height = img.size[1]
                    self.size = str(width)+","+str(height)
                    # Find the RGB values for each of the pixels and put it in a bytearray
                    br = bytearray(img.getdata(0))
                    bb = bytearray(img.getdata(1))
                    bg = bytearray(img.getdata(2))
                    # This code is just appeneding all the bytearrays to 'br'
                    for i in bb:
                        br.append(i)
                    for j in bg:
                        br.append(j)
                    # ENCODE
                    strr = base64.b64encode(br)
                    self.base6 = str(strr , 'UTF-8')

                except:
                    print("The Color Image Image File cannot be opened")
                    raise ValueError


            # Write to string and make the xml String
            self.xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
            self.xml += "<message type=\""+self.messageType+"\" size=\""+ str(self.size)+"\" encrypted=\"False\">\n"
            # self.getXmlString()
            self.xml += self.base6 + "\n"
            self.xml += "</message>"
            # print("\nThe message for the input file : "+self.filePath+"\n")
            # print(self.xml)

            # At this point we have the message in "self.xml" read from the txt file

        # The given string is already in the xml format
        elif 'XmlString' in kwargs.keys():
            self.xml = kwargs.pop('XmlString')

        else:
            raise ValueError

    def getXmlString(self):
        # encode whatever is in self.mess and saves it to self.base6
        return self.xml

    """
    Return an integer representing the number of bytes in the current XML string representation. This
    can used as a guide for any medium to determine if it is suitable to carry this message or not.Raise anException
    when no data exists in the instance.
    """
    def getMessageSize(self):
        length = len(self.xml)
        if length is 0:
            raise Exception("No Data in instance")
        return length

    """
    Save Image to the target image, provide the message in an image
    Raise: 1. An Exception when no data exists in the instance
           2. A TypeError when the message is not an image type
    """
    def saveToImage(self , targetImagePath):

        if self.messageType not in ['GrayImage','ColorImage']:
            raise TypeError
        if len(self.xml) is 0:
            raise Exception('No data in instance')
        # Decoding is same for everyone
        message = self.mess
        decodedMessage = base64.b64decode(message)
        # ----------------------   GRAYIMAGE  ---------------------------
        if self.messageType == 'GrayImage':

            a = self.size.split(',')
            width = int(a[0])
            height = int(a[1])
            # make the decoded data into a gray image
            # 'L' - is the mode for Gray Image
            im = Image.frombytes('L' , [width,height] , decodedMessage)
            im.save(targetImagePath)

        # ----------------------   color IMAGE  ---------------------------
        elif self.messageType == 'ColorImage':

            width = int(self.size.split(',')[0])
            height = int(self.size.split(',')[1])

            band = width * height
            # The decoded message is encoded in form RRR...GGG...BBB...
            # Hence we seperate them as below
            red = decodedMessage[0:int(band)]
            green = decodedMessage[band:2*band]
            blue = decodedMessage[2*band:3*band]

            # Create new empty image and then fill up the particular bands of each pixels
            new= Image.new('RGB',[width , height])
            RGB = [(r,g,b ) for r, g ,b in zip(red , green , blue)] #Zip helps iterate over more than one variable in a for loop
            new.putdata(RGB)
            # This just saves it to the targetPath
            new.save(targetImagePath)


    def saveToTextFile(self, targetTextFilePath):
        if self.messageType != "Text":
            raise TypeError
        if len(self.xml) is 0:
            raise Exception('No data in instance')
        # Decode
        decodedMessage = base64.b64decode(self.mess)
        dM = str(decodedMessage , "UTF-8")
        # Write to file
        FileObject = open(targetTextFilePath,"w")
        FileObject.write(dM)

    """
    Using the XML structure provided, populate the message attributes, encode the stream into base64 string, and place it in.
    Raise an Exception when no data exists in the instance
    """
    def saveToTarget(self, targetPath):
        try:
            # Parse the text file here to extract the input string
            lines = self.xml.split('\n')
            for line in lines:
                f = re.search (r'<message type="(.*)" size="(.*)" encrypted="(.*)">',line)
                if f:
                    self.encoding = f.group(3)
                    self.size = f.group(2)
                    self.messageType = f.group(1)

                f = re.search(r'>\n(.*)\n</message>',self.xml)
                if f:
                    self.mess = f.group(1)

            # at this point we have the essentials extracted from the message, which includes the messageType
            # redirect to the appropriate function
            if self.messageType == 'Text':
                self.saveToTextFile(targetPath)
            elif self.messageType in ['ColorImage','GrayImage']:
                self.saveToImage(targetPath)
            else:
                raise TypeError

        except:
            Exception("Output File does not exist")
        # pass

class Steganography:

    def __init__(self , imagePath, direction = 'horizontal'):

        if direction not in ['horizontal' , 'vertical']:
            raise ValueError
        try:
            # Extract essentials and save them in class members
            img = Image.open(imagePath)
            self.width = img.size[0]
            self.height = img.size[1]
            self.maxSize = self.width * self.height / 8
        except:
            raise ValueError
        if img.mode not in  ['L']:
            raise TypeError
        # save the opened image and direction in class members
        self.img = img
        self.direction = direction

    def embedMessageInMedium(self , message, targetImagePath):

        if message.getMessageSize() > self.maxSize:
            raise ValueError('In function: embedMessageInMedium')

        g = []
        new = Image.new('L' , (self.width , self.height)) # new empty image to save the resultant

    ####################################################################

        # Get a bytearray from the given image to be used as the medium
        # Raster scan according to the direction given

        if self.direction == 'horizontal':
            for rows in range(self.height):
                for col in range(self.width):
                    g.append(self.img.getpixel((col,rows)))
            mediumImageBytes = bytearray(g)
            mediumImageBytes = self.img.getdata()

        elif self.direction == 'vertical':
            for col in range(self.width):
                for rows in range(self.height):
                    g.append(self.img.getpixel((col,rows)))
            mediumImageBytes = bytearray(g)
            new = self.img.transpose(Image.TRANSPOSE)
            mediumImageBytes = new.getdata()

    ########################################################################

        # binaryPixel = int(bin((list(mediumImageBytes)[0]))[2:])

        # The code below saves all the essentials from the XML into class variables
        lines = message.xml.split('\n')
        for line in lines:
            f = re.search (r'<message type="(.*)" size="(.*)" encrypted="(.*)">',line)
            if f:
                self.encoding = f.group(3)
                self.size = f.group(2)
                self.messageType = f.group(1)

            f = re.search(r'>\n(.*)\n</message>',message.xml)
            if f:
                self.mess = f.group(1)
        # self.mess="AB"

    ###########################################################################

        # Convert message to a stream (str) of 1s and 0s to be encoded

        messageBytes = bytes(message.xml , "UTF-8")
        str = ""
        for i in list(messageBytes):
            s = bin(i)[2:]
            while len(s) is not 8:
                s = "0"+s
            str += s
        # print(str)
        # print(int(bin((list(mediumImageBytes)[0]))[2:]))

    ############################################################################

    # Getting the data ready to be popped sequentially

        mediumImageList = list(mediumImageBytes)
        strList = list(str)
        strList.reverse()
        ff = []
        for k in strList:
            ff.append(int(k))
        strList = ff
        # print(strList)

############################################################################################

        #ENCODING HERE!! THIS IS THE REAL DEAL

        h = []  # output list

        # Iterate through the list of medium in decimal and change it according to the but popped from the XMLMessage bit stream

        for i in mediumImageList:

            if len(strList)!= 0:
                # Get the bit to be embedded
                bit = strList.pop()

                if bit == 0 and i%2 == 1:
                    h.append(i - 1)
                elif bit == 1 and i%2 == 0:
                    h.append(i + 1)
                else:
                    h.append(i)

            else:
                h.append(i)
        # print(mediumImageList)
        # print(h)

############################################################################################

        mediumImageBytes = bytes(h)
        new.putdata(mediumImageBytes)
        # If the image has been transposed earlier, invert it again, since thats how the in-built putdata function works
        if self.direction == 'vertical':
            new = new.transpose(Image.TRANSPOSE)
        new.save(targetImagePath)

############################################################################################

    def extractMessageFromMedium(self):
        # read data according to orientation
        if self.direction == 'horizontal':
            listed = list(self.img.getdata())
        elif self.direction == 'vertical':
            new = self.img.transpose(Image.TRANSPOSE)
            listed = list(new.getdata())

        a = ""
        g =[]
        c = 0

        for i in bytes(listed):

            # Look for the last bit and save it in a stream of 1s and 0s

            # if the decimal number is odd, last bit is 1 and if the decimal number is even the last bit is 0
            if i%2 == 0:
                a += "0"
            else:
                a += "1"
            c += 1
            # Every 8 bits save the generated byte as a decimal integer into a list
            if c == 8:
                g.append(int(a , 2))    # Here 2 is the base of the input
                c = 0
                a = ""
        # this code interprets the data into an xml, since there were problems with the string format
        g = bytes(g)
        xmlString = str(g).strip('b').strip('\'')
        lines = xmlString.split('\n')
        mess = ""
        for line in lines:
                f = re.search (r'<message type="(.*)" size="(.*)" encrypted="(.*)">(.*)</message>',line)
                if f:
                    mess = f.group(4).strip('\\').strip('n').strip('\\').strip('n')
                    encoding = f.group(3)
                    size = f.group(2)
                    messageType = f.group(1)
                else:
                    return None

        xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        xml += "<message type=\""+messageType+"\" size=\""+ str(size)+"\" encrypted=\"False\">\n"
        # self.getXmlString()
        xml += mess + "\n"
        xml += "</message>"

        m = Message(XmlString=xml)
        return m

if __name__ =="__main__":

    m = Message(filePath = 'files/small.txt' , messageType= 'Text')
    # m = Message(filePath = 'files/dog.png' , messageType= 'GrayImage')
    # m = Message(filePath = 'files/sunflower.png' , messageType= 'ColorImage')
    # m.saveToTarget('newFile.txt')

    s = Steganography(imagePath='files/dog.png' , direction='horizontal')
    s.embedMessageInMedium(m , "embdOut.png")
    ss  = Steganography(imagePath='embdOut.png' , direction='horizontal')
    mm = ss.extractMessageFromMedium()
    mm.saveToTarget("Text.txt")
    pass
