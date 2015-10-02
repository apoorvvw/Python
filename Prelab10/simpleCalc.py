#!/usr/local/bin/python3.4

__author__ = 'ee364e10'# Import PySide classes
from PySide.QtCore import *
from PySide.QtGui import *
import sys
import calculator
import re
#from calculator import *

class calculatorClass(QMainWindow, calculator.Ui_MainWindow):

    def __init__(self, parent=None):

        super(calculatorClass, self).__init__(parent)
        self.setupUi(self)
        self.s = ""
        self.result = 0.0
        self.decimal = 2
        self.checked = 0
        # Connect Buttons to their methods
        self.btn0.clicked.connect(lambda :self.displayText('0'))
        self.btn1.clicked.connect(lambda :self.displayText('1'))
        self.btn2.clicked.connect(lambda :self.displayText('2'))
        self.btn3.clicked.connect(lambda :self.displayText('3'))
        self.btn4.clicked.connect(lambda :self.displayText('4'))
        self.btn5.clicked.connect(lambda :self.displayText('5'))
        self.btn6.clicked.connect(lambda :self.displayText('6'))
        self.btn7.clicked.connect(lambda :self.displayText('7'))
        self.btn8.clicked.connect(lambda :self.displayText('8'))
        self.btn9.clicked.connect(lambda :self.displayText('9'))
        self.btnPlus.clicked.connect(lambda :self.displayText('+'))
        self.btnMinus.clicked.connect(lambda :self.displayText('-'))
        self.btnMul.clicked.connect(lambda :self.displayText('X'))
        self.btnDiv.clicked.connect(lambda :self.displayText('/'))
        self.btnDecimal.clicked.connect(lambda :self.displayText('.'))
        self.btnClear.clicked.connect(lambda :self.displayText('C'))

        # Connect = Button
        try:
            self.btnResult.clicked.connect(self.findResult)
        except ZeroDivisionError:
            self.lineEdit.setText("ZeroDivisionError")

        # Connect spinBox
        self.spinBox.valueChanged[str].connect(self.onChanged)

        # Connect checkBox
        self.checkBox.toggled.connect(self.checkToggle)

    def checkToggle(self , state):
        if self.checkBox.isChecked():
            self.checked = 1
        else:
            self.checked = 0
        # print("**********{}".format(self.checked))

    def onChanged(self, val):
        self.decimal = self.spinBox.value()
        # print("**********  {}".format(a))

    def displayText(self, str):
        # ff = self.spinBox.value(self)
        # print(ff)
        ff = self.decimal #number of decimals to be displayed\

        #Reset the textBox for C
        if str == 'C':
            self.s = ""

        # -1 is the return code when '=' button is pressed
        elif str == '-1':
            print(ff)
            strr = "{0:.{1}f}".format(self.result,ff)    # Customize the number of decimal places shown in the output
            strr = strr.strip()

            if len(strr) - 1 > 13:     # Client requirements
                self.lineEdit.setText("ERROR: Output too Big")
                return

            if self.checked is 1:
                try:
                    strr = "{0:,}".format(float(strr)) # this is the python syntax for adding ',' between a number
                except:
                    pass
            self.s = "{0}".format(strr)

        else:
            self.s += str

        # Output the string to the text Box
        self.lineEdit.setText(self.s)
        print(self.lineEdit.text())

    def findResult(self):

        f = re.findall(r'\d*\.?\d*',self.s) # find all numbers in the input string, and put them in a list
        while '' in f:
            f.remove('') # remove greedyness of the regex statement
        f.reverse() # this is needed since the list pop function pops from the back

        ff = re.findall(r'[X\-+/]',self.s) # Find all the operators in the given input
        ff.reverse()

        flag = 0 # used to consider if the statement starts with a negetive

        if ( len(f) - len(ff) != 1) and self.s[0] != '-' :  # check for valid input and account for the first negetive
            self.result = 0.0
            self.lineEdit.setText("WrongInput")
            return

        while len(f)>=2 and len(ff)>0:

            # Use the immidiate execution algorithm for simplicity
            try:
                a = float(f.pop())
                b = float(f.pop())
            except:
                self.lineEdit.setText("WrongInput")
                print("Inhere")
                return
            op = ff.pop()

            if self.s[0] == '-' and flag == 0:
                a = a * (-1)
                op = ff.pop()
                flag = 1

            # Perform the poped operation
            if op == 'X':
                self.result = a * b
            elif op == '-':
                self.result = a - b
            elif op == '+':
                self.result = a + b
            elif op == '/':
                try:
                    self.result = a / b
                except:
                    self.result = 0.0
                    self.lineEdit.setText("ZeroDivisionError")
                    return
            print(self.result)
            f.append(self.result)
        self.displayText('-1')

currentApp = QApplication(sys.argv)
currentForm = calculatorClass()

currentForm.show()
currentApp.exec_()