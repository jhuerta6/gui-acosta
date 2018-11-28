import os

def convert(a):
    os.system("tshark -T pdml -r "+filename+" -V | tee "+a[0]+".pdml")


filename = input("Input PCAP file")
a = filename.split(.)
convert(pdml)


