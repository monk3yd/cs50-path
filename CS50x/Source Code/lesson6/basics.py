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
    print("x is less than y")       #execode
elif x > y:
    print("x is greater than y")    #execode
else:
    print("x is equals to y")       #execode

#loops
#infinite loop
while True
    print("hello, world")           #execode

#lopp with a variable
i = 3
while i > 0:
    print("cough")
    i -+ 1

#for loop
for i in [0, 1, 2]: #this is called a list, they're like arrays in C but with more features
    print("cough")

for i in range(3);  #succintly we can use range(). outputs values sequence 0, 1, 2
    print("cough")

#data types
bool, True or False
float, real numbers
int, integers
str, strings

#more powerful data types
range, sequence of numbers
list, sequence of mutable values, that we can change or add or remove
tuple, sequence of immutable values, that we can’t change
dict, collection of key/value pairs, like a hash table
set, collection of unique values