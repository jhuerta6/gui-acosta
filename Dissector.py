import xml.etree.ElementTree as ET

tree = ET.parse('cubic.pdml')
root = tree.getroot()

print(root)
i = 0
j = 0
packetlist = []

for packet in root:
    print packet.tag, packet.attrib
    for proto in packet:
        print proto.tag, proto.attrib
        for field in proto:
            print field.tag, field.attrib

for packet in root:
    packetlist.append(packet)

print(packetlist)