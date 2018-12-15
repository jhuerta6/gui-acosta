import subprocess

class PCAP:

    def __init__(self, dissector="tshark"): # for the moment, only this dissector
        self.dissector = dissector

    def convert(self, pcap):
        pdml= 'output_'+pcap+'.pdml'
        if(self.dissector == "tshark"):
        	cmd = self.dissector+' -r '+ pcap +' -T pdml > '+ pdml
        	subprocess.call(cmd, shell=True)
        	return pdml	
        else:
        	return 0
        
        

