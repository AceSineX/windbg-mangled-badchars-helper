#!/usr/bin/python
import socket
import sys
import binascii
from struct import *

path = "/path/to/file"
begin_badchar = sys.argv[1]

if(len(sys.argv) == 3):
    path = sys.argv[2]

blob = open(path, 'r')

line = blob.readline()
badchars = ""

# Parse blob and put the bytes in proper order
while(line):
    split = line.split(" ")
    b1 = split[2]
    b1 = "".join(reversed([b1[i:i+2] for i in range(0, len(b1), 2)]))
    b2 = split[3]
    b2 = "".join(reversed([b2[i:i+2] for i in range(0, len(b2), 2)]))
    b3 = split[4]
    b3 = "".join(reversed([b3[i:i+2] for i in range(0, len(b3), 2)]))
    b4 = split[5]
    b4 = "".join(reversed([b4[i:i+2] for i in range(0, len(b4), 2)]))
    badchars += b1 + b2 + b3 + b4
    line = blob.readline()


location_start = badchars.find(begin_badchar)
acc = location_start

# Check for correct offset, otherwise will get wrong output
if(location_start % 2 != 0):
    print("Wrong byte offset")
    print("exiting..")
    exit()

mangle_flag = 0

while(acc+5 < len(badchars)):
    if(int(badchars[acc:acc+2], base=16) + 1 != int(badchars[acc+2:acc+4], base=16) ):
        print("Mangled at: " + str(acc))
        mangle_flag = 1
    acc += 2

if(mangle_flag == 0):
    print("\n[+]No Mangles\n")
print("Ace says bye :)")
