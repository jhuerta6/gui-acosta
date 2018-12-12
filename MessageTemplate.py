from FieldLengthDependency import FieldLengthDependency
from PacketLengthDependency import PacketLengthDependency
from CheckSum import CheckSum
from FieldEquivalence import FieldEquivalence

class MessageTemplate:

    def __init__(self, messageTemplateName, destinationFolderName, destinationFolderPath, outputFormat):
        self.messageTemplateName = messageTemplateName
        self.destinationFolderName = destinationFolderName
        self.destinationFolderPath = destinationFolderPath
        self.outputFormat = outputFormat
        self.fieldLengthDependencyList = []
        self.packetLDList = []
        self.checksumList = []
        self.fieldEquivalenceList = []
        # self.fld = FieldLengthDependency("a","b")
        # self.pld = PacketLengthDependency("c","d")
        # self.check = CheckSum("e","f")
        # self.fe = FieldEquivalence("g","h","i","j")

    def addFieldLengthDependency(self, a, b):
        self.fieldLengthDependencyList.append(FieldLengthDependency(a,b))

    def removeFieldLengthDependency(self, a, b):
        for x in self.fieldLengthDependencyList:
            if x.sourceFieldName == a and x.targetFieldName == b:
                self.fieldLengthDependencyList.remove(x)

    def addPacketLengthDependency(self, a, b):
        self.packetLDList.append(PacketLengthDependency(a,b))

    def removePacketLengthDependency(self, a, b):
        for x in self.packetLDList:
            if x.packetName == a and x.fieldName == b:
                self.packetLDList.remove(x)

    def addCheckSum(self, a, b):
        self.checksumList.append(CheckSum(a, b))

    def removeCheckSum(self, a, b):
        for x in self.checksumList:
            if x.packetName == a and x.fieldName == b:
                self.checksumList.remove(x)

    def addFieldEquivalence(self, a, b, c, d):
        self.fieldEquivalenceList.append(a,b,c,d)

    def removeFieldEquivalence(self, a, b, c, d):
        for x in self.fieldEquivalenceList:
            if x.SourceMessageType == a and x.sourceFieldName == b and x.targetMessageType == c and x.targetFieldName == d:
                self.fieldEquivalenceList.remove(x)

exampleMsg = MessageTemplate("Message1","C:/Users/Sergio/Desktop", "C:/Users/Sergio/Desktop/Folder", "Scapy")
exampleMsg.addFieldLengthDependency("a", "b")
exampleMsg.addFieldLengthDependency("c", "d")
print(exampleMsg.fieldLengthDependencyList[0].sourceFieldName + " " + exampleMsg.fieldLengthDependencyList[0].targetFieldName)
exampleMsg.removeFieldLengthDependency("a", "b")
print(exampleMsg.fieldLengthDependencyList[0].sourceFieldName + " " + exampleMsg.fieldLengthDependencyList[0].targetFieldName)