# import library
from sys import argv
import csv
import re

# check for valid number of command arguments
if len(argv) != 3:
    print("invalid number of command-line arguments")
    exit(1)

# declare STR substrings variables
a = "AGATC"
b = "AATG"
c = "TATC"

# number of STR's

K = 3

#declare counters
aa = 0
bb = 0
cc = 0

# open csv file and dna sequence,
with open(argv[2], "r") as seqfile:
    s = seqfile.read()      # read contents into memory list

    # aa = s.count(a)?
    # bb = s.count(b)?
    # cc = s.count(c)?

# for each position in the sequence, keep checking succesive substrings until the str repeats no longer
    for i in range(len(s)):
        if s[i:i + 5] ==  a:
            aa += 1
        elif s[i:i + 4] == b:
            bb += 1
        elif s[i:i + 4] == c:
            cc += 1

strcou = [str(aa), str(bb), str(cc)]
# strcou = [aa, bb, cc]
# print(strcou)

# compare STR counts against each row in the csv file
with open(argv[1], "r") as dbfile:
    reader = csv.reader(dbfile)

    next(reader)

    #csvlist = list(reader)
    for line in reader:
        if line[1:] == strcou:
            print(line[0])
            exit()
        #print(line[1:])
    print("No match")