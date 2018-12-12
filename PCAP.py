import os

class PCAP():
    def convert(self, filename):
        a = filename.split(".")
        out = a[0]+".pdml"
        os.system("tshark -T pdml -r "+filename+" -V | tee "+out)
        return out

#filename = input("Input PCAP file")
#file = PCAP()
#b = file.convert("test.pcap")
#print(b)

