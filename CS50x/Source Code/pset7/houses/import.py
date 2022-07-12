import csv
from cs50 import SQL
from sys import argv

# check number of command-arguments
if len(argv) != 2:
    print("invalid number of command-line arguments")
    exit(1)

# Create database by opening and closing an empty file first
open("students.db", "w").close()
db = SQL("sqlite:///students.db")

# Create table called 'students', and specify the columns we want and data type of each.
db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC)")

# open csv file
with open(argv[1], "r") as file:
    reader = csv.DictReader(file)

    names = []
    # for each row,
    for row in reader:
        # parse name
        names = row['name'].split()
        
        check = len(names)
        
        if check == 2:
            first = names[0]
            middle = None
            last = names[1]
        else:
            first = names[0]
            middle = names[1]
            last = names[2]
        
        # insert each student into students table of students.db
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", first, middle, last, row["house"], row["birth"])