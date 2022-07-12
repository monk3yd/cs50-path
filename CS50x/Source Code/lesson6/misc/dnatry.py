# import libraries
from sys import argv
from csv import reader
import re                           # imports regular expressions
# import pprint                     # imports print formated list function

# check for valid number of command arguments
if len(argv) != 3:
    print("invalid number of command-line arguments")
    exit(1)

x = 0                               # use for import header into separate list

STRS = []                           # list contains header strings
people = []                         # list contains csv rows

# open csv file and dna sequence
with open(argv[1], "r") as data:
    reader = reader(data)           # read .csv file contents into memory list
    # next(reader)                  # skips header
    # print(db[0][1:])              # prints header without name column

    for row in reader:              # for each row in csv file
        if x < 1:                   # if first row
            STRS.append(row)            # store first row in STRS list
            x += 1
        else:
            people.append(row)      # (row[0], int(row[1]), int(row[2]), int(row[3]))      # store all other rows in people list

print('STRs: ')
for STR in STRS:
    print(STR[1:])                  # header without 'name' column. contains one STR per element

print('Here are the people in the list: ')
for line in people:
    print(line)                     # contains one person per element (line)

with open(argv[2], "r") as seqf:
    dna = seqf.read()               # read .txt file contents into memory string
print(dna)                          # prints string

# for each position in dna sequence: compute how many times the STR repeats starting at that position.
# for each position keep checking succesive substrings until the STR repeats no longer

    

#global_dna_counts = [str(A), str(B), str(C), str(D), str(E), str(F), str(G), str(H)]
#print(global_dna_counts)

# compare STR counts against each row in the csv file
#for line in db:
    #if line[1:] == global_dna_counts:
        #print(line[0])
        #exit()
#print("No match")