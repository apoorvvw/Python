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
from PySide.QtGui import *
from NewSteganography import NewSteganography
import glob

# Import PySide classes
from PySide.QtCore import *
from PySide.QtGui import *
from SteganographyGUI import *

debug = 1

'''
Things to implement
1. Make it work for vertical
2. Extract the message and display it
3. That should be all. Then try all test cases.
'''

class SteganographyBrowser(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(SteganographyBrowser, self).__init__(parent)
        self.setupUi(self)

        # Open FOlder Selector
        directory = QFileDialog.getExistingDirectory(None , "Select Folder with images ")

        # make a list of all image files in the given folder
        if directory == "":
            exit()
        if debug:
            print(directory)
        self.directory = directory

        # Refresh the list of files and update the treeView
        self.updateTree(directory)

        self.fileTreeWidget.itemClicked.connect(self.fileNameSelected)
        self.btnWipeMedium.clicked.connect(self.wiperDontWipe)
        self.btnExtract.clicked.connect(self.extractor)

    def extractor(self):
        # Extract the xml to pass it into the saveToTarget function
        n = NewSteganography(imagePath = self.targetImage , direction = 'horizontal')
        m = n.extractMessageFromMedium()


        if m is None:       # If the messege is not found try to look for it in vertical
            n = NewSteganography(imagePath = self.targetImage , direction = 'vertical')
            m = n.extractMessageFromMedium()
        exctractedXml = m.getXmlString()

        self.grpMessage.setEnabled(True)

        if debug:
            print(exctractedXml)
            print(self.trueDic[self.imageName])

        if self.trueDic[self.imageName] == "Text":
            targetOutputPath = "output.txt"
            m.saveToTarget(targetPath = targetOutputPath)

            if m.encoding is True:
                pass

            self.txtMessage.clear()
            self.stackMessage.setCurrentIndex(1)
            with open(targetOutputPath) as inputFile:
                for line in inputFile:
                    self.txtMessage.insertPlainText(line)
        else:
            targetOutputPath = "output.png"
            m.saveToTarget(targetPath = targetOutputPath)

            if m.encoding is True:
                pass

            # Code to scale the image
            self.stackMessage.setCurrentIndex(0)
            scene = QGraphicsScene()
            pixmap = QPixmap(targetOutputPath)  #Open Image in pixmap
            pixmap = pixmap.scaled(275,255,Qt.KeepAspectRatio) #Scale the image
            scene.addPixmap(pixmap)
            self.viewMessage.setScene(scene) #Finally save it
            # Made them class variables to access later to remove them
            self.messageScene = scene
            self.messagePixmap = pixmap

        if debug:
            print(m.encoding)

        self.btnExtract.setDisabled(True)

    def wiperDontWipe(self):

        msgBox = QMessageBox()
        msgBox.setText("The document has been wiped.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QMessageBox.Ok  | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Ok)
        ret = msgBox.exec_()
        if ret == QMessageBox.Cancel:
            return

        n = NewSteganography(imagePath = self.targetImage , direction = 'horizontal')
        n.wipeMedium()
        self.btnExtract.setDisabled(True)
        self.btnWipeMedium.setDisabled(True)
        self.fileTreeWidget.clear()
        self.updateTree(self.directory)

        self.txtMessage.clear()
        scene = QGraphicsScene()
        pixmap = QPixmap().fill(color = Qt.white)
        scene.addPixmap(pixmap)
        self.viewMessage.setScene(scene)


    def fileNameSelected (self, item, column):
        if debug:
            print('fileNameSelected: ', item.text(column))

        self.txtMessage.clear()
        scene = QGraphicsScene()
        pixmap = QPixmap().fill(color = Qt.white)
        scene.addPixmap(pixmap)
        self.viewMessage.setScene(scene)

        self.imageName = item.text(column)
        if self.imageName in ['Text','ColorImage', 'GrayImage']:
            self.imageName = item.parent().text(column)
        self.targetImage = self.directory+"/"+self.imageName

        # Code to scale the image
        scene = QGraphicsScene()
        pixmap = QPixmap(self.directory+"/"+self.imageName)  #Open Image in pixmap
        pixmap = pixmap.scaled(275,255,Qt.KeepAspectRatio) #Scale the image
        scene.addPixmap(pixmap)
        self.viewMedium.setScene(scene) #Finally save it


        # Display the required items on the window
        self.grpMedium.setEnabled(True)
        self.btnExtract.setEnabled(True)
        self.btnWipeMedium.setEnabled(True)

        #Make seperate lists for images with and without messages
        if self.imageName in self.trueDic:
            if debug:
                print("True Dic")
            if self.trueDic[self.imageName] == "Text":
                self.stackMessage.setCurrentIndex(1)
            else:
                self.txtMessage.clear()
                self.stackMessage.setCurrentIndex(0)
        elif self.imageName in self.falseList:
            if debug:
                print("False List")
            self.btnWipeMedium.setDisabled(True)
            self.btnExtract.setDisabled(True)


    def updateTree(self , directory):
        imageFiles = glob.glob(directory+'/*.png')
        imageFiles += glob.glob(directory+'/*.gif')
        imageFiles += glob.glob(directory+'/*.bmp')
        imageFiles += glob.glob(directory+'/*.tif')
        imageFiles += glob.glob(directory+'/*.jpg')
              # Check if the image files have a message in them
        trueDic = {}
        trueList = []
        falseList = []
        for file in imageFiles:
            s = NewSteganography(imagePath=file ,direction='horizontal')

            returnValue = s.checkIfMessageExists()[0]
            fileList = file.split('/')
            fileName = fileList[len(fileList) - 1]

            if returnValue is True:
                trueList.append(fileName)
                trueDic[fileName] = s.checkIfMessageExists()[1]
            else:
                falseList.append(fileName)
            # print(file + '  ->  ' + str(returnValue))

        if debug&0:
            print(trueDic)

        # Disable the unnecessary groups
        self.grpMedium.setDisabled(True)
        self.grpMessage.setDisabled(True)

        # IMPLEMENTING/ POPULATING THE TREE WIDGET
        for file in falseList:
            item = QTreeWidgetItem([file])
            item.setForeground(0,QColor('blue'))

            self.fileTreeWidget.addTopLevelItem(item)

        for file in trueDic:
            parentItem = QTreeWidgetItem([file])
            parentItem.setForeground(0,QColor('red'))
            font = QFont()
            font.setBold(True)
            parentItem.setFont(0,font)
            self.fileTreeWidget.addTopLevelItem(parentItem)

            childItem = QTreeWidgetItem([trueDic[file]])
            childItem.setForeground(0,QColor('green'))
            parentItem.insertChild(0, childItem)
        self.trueDic = trueDic
        self.falseList = falseList
        self.fileTreeWidget.expandAll()
        self.fileTreeWidget.show()

currentApp = QApplication(sys.argv)
currentForm = SteganographyBrowser()

currentForm.show()
currentApp.exec_()

'''
Web Links:

1. Tree Widget example:
   http://stackoverflow.com/questions/25166305/how-to-auto-expand-qtreewidget-items

2. Change the font:
   http://stackoverflow.com/questions/20131761/add-an-item-to-qtreeview-with-a-specific-style

3. Scaling the image use documentation for qpixmap on sourceforge

4. Pop up for wipe:
   http://pyqt.sourceforge.net/Docs/PyQt4/qmessagebox.html

5.
'''