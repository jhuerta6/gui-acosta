from FieldLengthDependency import FieldLengthDependency
from PacketLengthDependency import PacketLengthDependency
from CheckSum import CheckSum
from FieldEquivalence import FieldEquivalence


class MessageTemplate:

    def __init__(self, MessageTemplateName, DestinationFolderName, DestinationFolderPath, OutputFormat):
        self.MessageTemplateName = MessageTemplateName
        self.DestinationFolderName = DestinationFolderName
        self.DestinationFolderPath = DestinationFolderPath
        self.OutputFormat = OutputFormat
        self.fld = FieldLengthDependency("a","b")
        self.pld = PacketLengthDependency("c","d")
        self.check = CheckSum("e","f")
        self.fe = FieldEquivalence("g","h","i","j")

exampleMsg = MessageTemplate("Message1","C:/Users/Sergio/Desktop", "C:/Users/Sergio/Desktop/Folder", "Scapy")
print (exampleMsg.fld.TargetFieldName)