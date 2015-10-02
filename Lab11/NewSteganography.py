#!/usr/local/bin/python3.4
__author__ = 'ee364e10'

import sys
import os
import math
import re
from PIL import Image
from io import BytesIO
import base64
from Steganography import Message
import SteganographyGUI
from PySide.QtGui import *

class NewSteganography():

    def __init__(self , imagePath, direction = 'horizontal'):
        self.imgpath = imagePath
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
        xml += "<message type=\""+messageType+"\" size=\""+ str(size)+"\" encrypted=\""+encoding+"\">\n"
        # self.getXmlString()
        xml += mess + "\n"
        xml += "</message>"

        m = Message(XmlString=xml)
        return m
    def wipeMedium(self):
        mediumImageBytes = self.img.getdata()
        mediumImageList = list(mediumImageBytes)

        h = []
        for i in mediumImageList:
            if i % 2 == 0:
              h.append(i)
            else:
                h.append(i-1)
        mediumImageBytes = bytes(h)
        new = Image.new('L' , (self.width , self.height))
        new.putdata(mediumImageBytes)
        new.save(self.imgpath)   # ********* CHANGE THS
    def checkIfMessageExists(self):
        listed = list(self.img.getdata())
        a = ""    # each 8 bit character
        g =[]     # list of characters
        c = 0     # flag to check if 8 bits are covered
        flag = 0; # Flag to check if the loop has reached the second ">" character
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
                character = int(a,2)
                g.append(character)    # Here 2 is the base of the input
                if character == 62:
                    flag += 1
                    if flag is 2:
                        break
                c = 0
                a = ""
        g = bytes(g)
        requiredString = ""
        try:
            requiredString = str(g, 'UTF-8')
        except:
            pass
        f = re.search (r'<message type="(.*)" size="(.*)" encrypted="(.*)">',requiredString)
        if f:
            messageType = f.group(1)
            output = tuple([True , messageType])
        else:  # If the message is not found after reading it horizontally, try reading vertically
            a = ""    # each 8 bit character
            g =[]     # list of characters
            c = 0     # flag to check if 8 bits are covered
            flag = 0 # Flag to check if the loop has reached the second ">" character
            # transposing it makes it read vertically
            new = self.img.transpose(Image.TRANSPOSE)
            listed = list(new.getdata())
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
                    character = int(a,2)
                    g.append(character)    # Here 2 is the base of the input
                    if character == 62:
                        flag += 1
                        if flag is 2:
                            break
                    c = 0
                    a = ""
            g = bytes(g)
            requiredString = ""
            try:
                requiredString = str(g, 'UTF-8')
            except:
                pass
            f = re.search (r'<message type="(.*)" size="(.*)" encrypted="(.*)">',requiredString)
            if f:
                messageType = f.group(1)
                output = tuple([True , messageType])
            else: # Vertical and Horizontal both fail
                output = tuple([False , None])
        return output



if __name__ =="__main__":
    s = NewSteganography(imagePath='files/bridge_dog_h.png' , direction='horizontal')
    s.checkIfMessageExists()
    # mm = s.extractMessageFromMedium()
    # mm.saveToTarget("Text.txt")
    pass