#include library

#get_string
answer = input("What's your name?\n")       #input is native to python
answer = get_string("What's your name?\n")  #need to import cs50library or specific function

#print
print("hello, world")       #just print
print("hello, " + answer)   #cocatenate with + operator
print("hello,", answer)     #pass multiple arguments to print separated by ,
print(f"hello, {answer}")   #{variable} works like %s in C works

#declare variable
counter = 0                 #initialize to 0

#increment variable
counter = counter + 1       #increment variable counter by 1
counter += 1                #increment variable counter by 1

#conditions

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equals to y")
