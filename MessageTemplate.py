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

    def addFieldLengthDependency(self, a, b):
        self.fieldLengthDependencyList.append(FieldLengthDependency(a,b))

    def removeFieldLengthDependency(self, a, b):
        for x in self.fieldLengthDependencyList:
            if x.sourceFieldName == a and x.targetFieldName == b:
                self.fieldLengthDependencyList.remove(x)

    def printFieldLengthDependencyList(self):
        for x in self.fieldLengthDependencyList:
            print(x.sourceFieldName + " " + x.sourceFieldName)
        print("\n")

    def addPacketLengthDependency(self, a, b):
        self.packetLDList.append(PacketLengthDependency(a,b))

    def removePacketLengthDependency(self, a, b):
        for x in self.packetLDList:
            if x.packetName == a and x.fieldName == b:
                self.packetLDList.remove(x)

    def printPacketLengthDependencyList(self):
        for x in self.packetLDList:
            print(x.packetName + " " + x.fieldName)
        print("\n")

    def addCheckSum(self, a, b):
        self.checksumList.append(CheckSum(a, b))

    def removeCheckSum(self, a, b):
        for x in self.checksumList:
            if x.packetName == a and x.fieldName == b:
                self.checksumList.remove(x)

    def printCheckSumList(self):
        for x in self.checksumList:
            print(x.packetName + " " + x.fieldName)
        print("\n")

    def addFieldEquivalence(self, a, b, c, d):
        self.fieldEquivalenceList.append(FieldEquivalence(a, b, c, d))

    def removeFieldEquivalence(self, a, b, c, d):
        for x in self.fieldEquivalenceList:
            if x.sourceMessageType == a and x.sourceFieldName == b and x.targetMessageType == c and x.targetFieldName == d:
                self.fieldEquivalenceList.remove(x)

    def printFieldEquivalenceList(self):
        for x in self.fieldEquivalenceList:
            print(x.sourceMessageType + " " + x.sourceFieldName + " " + x.targetMessageType + " " + x.targetFieldName)
        print("\n")

# exampleMsg = MessageTemplate("Message1","C:/Users/Sergio/Desktop", "C:/Users/Sergio/Desktop/Folder", "Scapy")
# exampleMsg.addFieldEquivalence("a", "b", "c", "d")
# exampleMsg.addFieldEquivalence("c", "d", "e", "f")
# exampleMsg.printFieldEquivalenceList()
# exampleMsg.removeFieldEquivalence("a", "b", "c", "d")
# exampleMsg.printFieldEquivalenceList()