import logging
from lib import *

fl1 = "/Volumes/Data/Prakasha/Learning/Python-Learning/files/iperf.log"
fle = open(fl1, "r")
lines = fle.readlines()
fle.close()
tput = []
tpt = -1
for line in lines:
    if line.find(" sec") >= 0 & line.find(" MBytes") >= 0 & line.find("Mbits/sec"):
        if line.find('  0.0- 1.0 sec') >= 0:
            if tpt != -1:
                tput.append(tpt)
                tpt = -1
        if ((line.find('  0.0- 1.0 sec') < 0) & (line.find('  0.0-') >= 0)):
            tpt = int(line.split('Mbits/sec')[0].split(' ')[-2])
if tpt != -1:
    tput.append(tpt)
for i in range(0,len(tput)):
        logging.info("Throughput for iteration %d => %d" %(i+1,tput[i]))
