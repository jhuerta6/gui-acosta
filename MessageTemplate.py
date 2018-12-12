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

    # def changeDestFolderName(self, name):
    #     self.destinationFolderName = name
    #
    # def changeMessageTemplateName(self, name):
    #     self.messageTemplateName = name
    #
    # def changeDestFolderPath(self, path):
    #     self.destinationFolderPath = path
    #
    # def changeOutputFormet(self, format):
    #     self.outputFormat = format

    def addFieldLengthDependency(self, a, b):
        self.fieldLengthDependencyList.append(FieldLengthDependency(a,b))

    def addPacketLengthDependency(self, a, b):
        self.packetLDList.append(PacketLengthDependency(a,b))

    def addCheckSum(self, a, b):
        self.checksumList.append(CheckSum(a, b))

    def addFieldEquivalence(self, a, b, c, d):
        self.fieldEquivalenceList.append(a,b,c,d)

exampleMsg = MessageTemplate("Message1","C:/Users/Sergio/Desktop", "C:/Users/Sergio/Desktop/Folder", "Scapy")
exampleMsg.addFieldLengthDependency("a", "b")
exampleMsg.addPacketLengthDependency("c", "d")
print(exampleMsg.fieldLengthDependencyList[0].sourceFieldName)