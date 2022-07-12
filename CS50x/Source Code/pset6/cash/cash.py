# library
from cs50 import get_float

# prompt for change owed
while True:
    dollars = get_float("Change owed: ")
    if dollars >= 0:
        break
    
# variables
cents = round(dollars * 100)
coins = 0

# count coins
while cents > 0:
    if cents >= 25:
        cents -= 25
        coins += 1
        
    elif cents < 25 and cents >= 10:
        cents -= 10
        coins += 1
        
    elif cents < 10 and cents >= 5:
        cents -= 5
        coins += 1
        
    elif cents < 5 and cents >= 1:
        cents -= 1
        coins += 1
# print
print(f"{coins}")