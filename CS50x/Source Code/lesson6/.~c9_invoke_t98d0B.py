#include library

#get_string
answer = input("What's your name?\n")       #input is native to python

#print
print("hello, world")       #just print
print("hello, " + answer)   #cocatenate with + operator
print("hello,", answer)     #pass multiple arguments to print separated by ,
print(f"hello, {answer}")   #{variable} works like %s in C works
