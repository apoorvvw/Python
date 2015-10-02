#!/usr/local/bin/python3.4

__author__ = 'ee364e10'

class Entry:
    key = 0
    value = "String"

    def __init__(self, k= 0 , v= ''):
        if type(k) is int:
            self.key = 0
            self.value = v
        else:
            print("Type error")
            raise TypeError

    def __str__(self):
        str = ""
        for i in dict:
            str += i + ": \""+dict[i]+"\"\n"
        return str

    def __hash__(self):
        t = (self.key , self.value)
        return hash(t)

class LookUp:
    typed = {}
    _entrySet = set([])
    _name = ""

    def __init__(self, name):
        self._name = name

    def __str__(self):
        str = ""
        str += "[\"{0}\": {1:02d} Entries]\n".format(self._name , len(self._entrySet))
        return str

    def addEntry(self , entry):
        if (entry in self._entrySet):
            print("Entry already exists in the set")
            raise ValueError
        else:
            self._entrySet.add(entry)

    def updateEntry(self , entry):
        if entry in self._entrySet:
            self._entrySet.update(entry)
        else:
            self.addEntry(entry)

    def removeEntry(self,entry):
        self._entrySet.remove(entry)

    def getEntry(self , key):
        try:
            return(self._entrySet[key])
        except:
            raise KeyError

    def addOrUpdateFromDictionary(self , someDict):
        for a in someDict:
            self.updateEntry(someDict[a])

    def getAsDictionary(self):
        dict = {}
        k = 0
        for a in self._entrySet:
            dict[k] = a
            k += 1
        return dict

    def getKeys(self):
        k = []
        for a in self._entrySet:
            k.append(a.keys)
        return(sorted(k))



    def getValues(self):
        k = []
        for a in self._entrySet:
            k.append(a.values)
        return(sorted(k))

    def getElementCount(self):
        return len(self._entrySet)