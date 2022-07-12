#include library
from cs50 import get_string

#get_string
answer = get_string("What's your name?\n")       #input is native to python

#print
print(f"hello, {answer}")   #{variable} works like %s in C works