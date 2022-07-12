# import libraries
from sys import argv
from csv import reader
# import re                           # imports regular expressions

# check for valid number of command arguments
if len(argv) != 3:
    print("invalid number of command-line arguments")
    exit(1)


people = []                         # list contains csv file row by row
# open csv file and
with open(argv[1], "r") as data:
    reader = reader(data)           # read .csv file contents into memory list
    for row in reader:              # for each row in csv file
        people.append(row)      # (row[0], int(row[1]), int(row[2]), int(row[3]))      # store all other rows in people list


# open dna sequence
with open(argv[2], "r") as seqf:
    dna = str(seqf.read())               # read .txt file contents into memory string
# print(dna)                          # prints string


# dictionary key/value pairs
STRS = {
    'AGATC': 0,
    'TTTTTTCT': 0,
    'AATG': 0,
    'TCTAG': 0,
    'GATA': 0,
    'TATC': 0,
    'GAAA': 0,
    'TCTG': 0
}

# for each position in dna sequence: compute how many times the STR repeats starting at that position.
# for each position keep checking succesive substrings until the STR repeats no longer

for STR in STRS:
    i = 0                   # iterator through dna sample
    tmp_counter = 0         # store consecutive str count for each str
    global_counter = 0      # stores highest consecutive repeat of each STR iteration
    while i < len(dna):
        if STR == dna[i:i+len(STR)]:            # if DNA node match with substring
            tmp_counter += 1                        # increase tmp counter
            if i+len(STR) < len(dna):               # check if iterator inside bounds
                i += len(STR)                           # if so, re-set iterator at new location
            continue                                # go back to the beginning of the inner loop
        else:                                   # if it doesn't match with substring (means break of consecuitve STR)
            if tmp_counter > global_counter:       # check if consecutive counter is bigger than global counter
                global_counter = tmp_counter            # if so, pass tmp value to global variable
                tmp_counter = 0                         # reset tmp counter
            else:                                   # if not,
                tmp_counter = 0                         # reset tmp counter
        i += 1
    STRS[STR] = global_counter              # put global_counter value into corresponding value in dict
# print('total STR count: ')
# print(STRS)
# print(people[2][1:])

llist = []
# compare STR counts against each row in the csv file
for STR, counter in STRS.items():
    if STR in people[0]:
        llist.append(str(counter))
# print(llist)

for x in range(len(people)):
    for y in range(len(people)):
        if llist == people[x][y:]:
            print(people[x][0])
            exit(0)
print('No match')