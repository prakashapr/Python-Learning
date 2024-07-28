from statistics import mean
"""import logging
from lib import *

fl1 = "/Volumes/Data/Jaya/Learning/Python-Learning/files/workfile.txt"
fle = open(fl1, "r")
loglist = fle.readlines()
fle.close()
# fle.write(b'0123456789abcdef\nabcd')
# print (f.seek(5))      # Go to the 6th byte in the file
# print (f.read(1))
# print (f.seek(-3, 2))  # Go to the 3rd byte before the end
# print (f.read(1))
# fle.readline()
for fl2 in loglist:
    fl = fl2.rstrip("\n")
    # logging.info(fl)
    # if "prakasha" in fl:
    #     print ("Line %s contains prakasha" %fl.rstrip('\n'))
    if str(fl).find("prakasha"):
        logging.info("Line %s contains prakasha" % fl.rstrip("\n"))
# Example:
linestring = open(fl1, "r").read()

# Then you can print it:
logging.info(linestring)

# You can even make a list with it!
logging.info(linestring.split("\n"))
for ln in linestring.split("\n"):
    if ln.find("prakasha") >= 0:
        logging.info("prakasha is found in %s", ln)
logging.info("Jaya")
"""
# ####################### File operations ####################

# w - write
# a - append
# x - create file and write
# r - read
# t - text
# b - binary            >> to read binary of any file
# read - to read full txt in file
# readline - to read txt in line
"""
f = open("loop_sample.py")  # TO OPEN FILE

print(f.read())
"""

file_handle = open("../files/iperf.log", "rt")
# print(f.read())
file_content = file_handle.readlines()
thpt_numbers = []
for item in file_content:
    print(item)
    item=item.strip()
    if "Mbits/sec" in item:
        line_item = item.split(" ")
        thpt_numbers.append(int(line_item[-2]))

print(f'thpt_numbers = {thpt_numbers}')
tput_max = max(thpt_numbers)
print(f'Maximum number is :{tput_max}')
print(f'min number is :{min(thpt_numbers)}')
print(f'average number is :{mean(thpt_numbers)}')

    # print(item)




