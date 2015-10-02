#! /usr/local/bin/python3.4

__author__ = 'ee364e10'

class Experiment:

    experimentNumber = 0
    experimentDate = "January 1, 2015"
    virusName = "Virus Name"
    unitCount = 0
    unitCost = 0.00
    totalCost = unitCost * unitCount

    def __init__(self , experimentNo = 0 , experimentDate = "January 1, 2015" ,virusName = "Virus Name" ,
                 unitCount = 0 , unitCost = 0.00 ):
        self.experimentDate = experimentDate
        self.experimentNumber = experimentNo
        self.unitCount = unitCount
        self.unitCost = unitCost
        self.totalCost = self.unitCost * float(self.unitCount)
        self.virusName = virusName

    def __str__(self):
        return("{0:03d}, {1}, ${2:06.2f}: {3}".format(self.experimentNumber , self.experimentDate , self.totalCost , self.virusName))

class Technician:
    techName = "Technicians name"
    techId= "00000"
    experiments = {}

    def __init__(self , techName = "Name" , techID = "0000"):
        self.techName = techName
        self.techId = techID
        self.experiments = {}

    def addExperiment(self , experiment):
        #print("inhere")
        self.experiments[experiment.experimentNumber] = experiment

    def __str__(self):
        c = 0
        for i in self.experiments:
            c += 1
        return("{0}, {1}: {2:02d} Experiments".format(self.techId , self.techName , c))

    def generateTechActivity(self):
        out = ("{}, {}".format(self.techId , self.techName))
        q = sorted(self.experiments)
        for i in q:
            out += "\n"
            out += self.experiments[i].__str__()
        return out

    def loadExperimentsFromFile(self,filename):
        c = 0
        with open(filename,"r") as inputFile:
            for line in inputFile:
                c += 1
                if c > 2:
                    #print(line.split()[4].strip('$'))
                    exp = Experiment(int(line.split()[0]) , line.split()[1] ,line.split()[2], int(line.split()[3]), float(line.split()[4].strip('$')) )
                    self.addExperiment(exp)
                    #print(exp)


class Laboratory:
    labName = "labname"
    technicians = {}
    t = {}

    def __init__(self, labname = "labname"):
        self.labName = labname
        self.technicians = {}
        self.t = {}

    def addTechnician(self , technician):
        self.technicians[technician.techName] = technician
        self.t[technician.techId] = technician

    def __str__(self):
        c = 0
        for i in self.technicians:
            c+=1
        out = ("{0}: {1:02d} Technicians".format(self.labName , c))
        q = sorted(self.t)
        for j in q:
            out += "\n"
            out += self.t[j].__str__()

        return out
    def generateLabActivity(self):
        out = ""
        q = sorted(self.technicians)
        for i in q:
            T = self.technicians[i]
            out += T.generateTechActivity()
            out += "\n\n"
        return out



if __name__ == "__main__":
    e = Experiment(31,"04/01/2015","LLLLLLLLL" , 3 , 4.4)
    # print(e)
    t = Technician("Techi", "8888")
    # print(t)
    # t.addExperiment(e)
    # t.addExperiment(Experiment(32,"04/01/2015","LLLLLLLLL" , 3 , 4.4))
    # t.addExperiment(Experiment(33,"04/01/2015","LLLLLLLLL" , 3 , 4.4))
    # print(t)
    # print("-----------------------")
    # t.generateTechActivity()
    # print("-----------------------")
    t.loadExperimentsFromFile("report 55926-36619.txt")
    t1 = Technician("PPPchno", "4545454")
    t1.loadExperimentsFromFile("report 75471-28954.txt")
    # print("-----------------------")
    print(t.generateTechActivity())
    print("-----------------------")
    l = Laboratory("ggg")
    print(l)
    l.addTechnician(t)
    l.addTechnician(t1)
    print(l)
    print("-----------------------")
    print(l.generateLabActivity())