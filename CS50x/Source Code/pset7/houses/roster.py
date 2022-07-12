import csv
from cs50 import SQL
from sys import argv

# check number of command-arguments
if len(argv) != 2:
    print("invalid number of command-line arguments")
    exit(1)

# open database
open("students.db", "r")
db = SQL("sqlite:///students.db")

rows = []
# query database for all students in house
rows = db.execute("SELECT first, middle, last, house, birth FROM students ORDER BY last, first")

for row in rows:
    if argv[1] == row['house']:
        if row['middle'] == None:
            print(row['first'], row['last'] + ',', "born", row['birth'])
        else:
            print(row['first'], row['middle'], row['last'] + ',', "born", row['birth'])
    else:
        continue

# print(row['first'], row['middle'], row['last'], row['birth'])