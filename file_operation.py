fle = open('workfile.txt', 'rb+')
#fle.write(b'0123456789abcdef\nabcd')
#print (f.seek(5))      # Go to the 6th byte in the file
#print (f.read(1))
#print (f.seek(-3, 2))  # Go to the 3rd byte before the end
#print (f.read(1))
#fle.readline()
for fl in fle:
    print (fl)
import re
a="parakasha"
m = re.search('(pr?)', a)
print (m)