import csv #package or library
from cs50 import get_string

#file = open("phonebook1.csv", "a")

name = get_string("Name: ")
number = get_string("Number: ")

with open("phonebook.csv", "a") as file:
    writer = csv.writer(file) #pass open file to this library that helps me read a csv file (rows and columns)
    writer.writerow((name, number)) #tuple seems to explain double () more later!

#file.close()