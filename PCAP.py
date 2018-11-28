import os

def convert(a):
    os.system("tshark -T pdml -r "+a+" -V | tee "+a[0]+".pdml")


a = input("Input PCAP file")
pdml = a.split(.)
conver(pdml)


