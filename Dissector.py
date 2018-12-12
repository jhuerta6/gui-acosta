import xml.etree.ElementTree as ET
from PCAP import PCAP


class Dissector:
    def Dissect(self, pcap, filename="test.pcap"):
        #pcap = PCAP() #used for testing
        #convert file name
        pdmlfile = pcap.convert(filename)
        tree = ET.parse(pdmlfile)
        root = tree.getroot()

        print(root)
        i = 0
        j = 0
        packetlist = []

        #maybe we can use this to build PDML view... Create other classes
        for packet in root:
            print packet.tag, packet.attrib
            for proto in packet:
                print proto.tag, proto.attrib
                for field in proto:
                    print field.tag, field.attrib
        for packet in root:
            packetlist.append(packet)

        print(packetlist)

        return root


#Used for testing Dissector class
    def getPDML():
        a = Dissector()
        pcap = PCAP()
        return a.Dissect(pcap)