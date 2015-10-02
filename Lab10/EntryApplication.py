import sys
import re
from PySide.QtGui import *

from EntryForm import *

class EntryApplication(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(EntryApplication, self).__init__(parent)
        self.setupUi(self)

        self.btnLoad.clicked.connect(self.loadData)

        self.btnClear.clicked.connect(self.Clear)

        self.btnSave.clicked.connect(self.Save)

        self.txtFirstName.textChanged.connect(self.Enable)
        self.txtLastName.textChanged.connect(self.Enable)
        self.txtState.textChanged.connect(self.Enable)
        self.txtCity.textChanged.connect(self.Enable)
        self.txtAddress.textChanged.connect(self.Enable)
        self.txtEmail.textChanged.connect(self.Enable)
        self.txtZip.textChanged.connect(self.Enable)

    def Enable(self):
        self.btnSave.setEnabled(True)
        self.lblError.setText("")
        self.btnLoad.setDisabled(True)

    def Clear(self):
        self.txtLastName.setText("")
        self.txtFirstName.setText("")
        self.txtZip.setText("")
        self.txtEmail.setText("")
        self.txtAddress.setText("")
        self.txtCity.setText("")
        self.txtState.setText("")
        self.btnSave.setDisabled(True)
        self.lblError.setText("")
        self.btnLoad.setEnabled(True)

    def Save(self):
        # Has tExt
        if self.txtCity.text() == "" or self.txtState.text() == "" or self.txtFirstName.text() == "" or self.txtLastName.text() == "" or self.txtAddress.text() == "" or self.txtZip.text() == "" or self.txtEmail.text() == "":
            self.lblError.setText("ERROR: Fill all entries")
            return

        # State validation
        state = self.txtState.text()
        if state not in self.states:
            self.lblError.setText("ERROR: State must be in the US")
            return

        #Email validation
        if not re.search(r'\w+@\w+\.\w+',self.txtEmail.text()):
            self.lblError.setText("ERROR: Incorrect Email")
            return

        #ZIP code validation
        if len(self.txtZip.text()) != 5:
            self.lblError.setText("ERROR: Incorrect ZIP code, must be 5 digits")
            return

        FileObject = open('target.xml',"w")
        FileObject.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        FileObject.write("<user>\n")
        FileObject.write("\t<FirstName>"+self.txtFirstName.text()+"</FirstName>\n")
        FileObject.write("\t<LastName>"+self.txtLastName.text()+"</LastName>\n")
        FileObject.write("\t<Address>"+self.txtAddress.text()+"</Address>\n")
        FileObject.write("\t<City>"+self.txtCity.text()+"</City>\n")
        FileObject.write("\t<State>"+self.txtState.text()+"</State>\n")
        FileObject.write("\t<ZIP>"+self.txtZip.text()+"</ZIP>\n")
        FileObject.write("\t<Email>"+self.txtEmail.text()+"</Email>\n")
        FileObject.write("</user>\n")


    def loadFromXmlFile(self, filePath):
        """
        Handling the loading of the data from the given file name. This method should only be  invoked by the
        'loadData' method.
        """
        with open(filePath,"r") as inputFile:
            for line in inputFile:
                firstName = re.search(r'<FirstName>(\w*)</FirstName>',line)
                lastName = re.search(r'<LastName>(.*)</LastName>',line)
                address = re.search(r'<Address>(.*)</Address>',line)
                zip = re.search(r'<ZIP>(\d*)</ZIP>',line)
                city = re.search(r'<City>(.*)</City>',line)
                state = re.search(r'<State>(\w*)</State>',line)
                email = re.search(r'<Email>(.*)</Email>',line)
                try:
                    self.txtFirstName.setText(firstName.group(1))
                except:
                    pass
                try:
                    self.txtLastName.setText(lastName.group(1))
                except:
                    pass
                try:
                    self.txtZip.setText(zip.group(1))
                except:
                    pass
                try:
                    self.txtEmail.setText(email.group(1))
                except:
                    pass
                try:
                    self.txtAddress.setText(address.group(1))
                except:
                    pass
                try:
                    self.txtCity.setText(city.group(1))
                except:
                    pass
                try:
                    self.txtState.setText(state.group(1))
                except:
                    pass

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD, OR THE TEST WILL NOT PASS! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadFromXmlFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = EntryApplication()

    currentForm.show()
    currentApp.exec_()
