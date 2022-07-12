import re #regular expressions library
from cs50 import get_string

s = get_string("Do you agree?\n")

if re.search("^y(es)?$", s, re.IGNORECASE):
    print("Agreed.")
elif re.search("no?", s, re.IGNORECASE): #ummm, no input works
    print("Not agreed.")