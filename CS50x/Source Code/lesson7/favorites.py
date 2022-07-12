import csv

counts = {}         #same as: counts = dict()

with open("CS50 2019 - Lecture 7 - Favorite TV Shows (Responses) - Form Responses 1.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # print(row["title"])

        title = row["title"].upper()

        if title in counts:         # if i've seen the title before add one to counter value
            counts[title] += 1
        else:                       # else, if it's the first time we see the title name, set counter of that title to 1.
            counts[title] = 1
# print(counts)

def f(item):            # function that takes as input an item, and if that item has two values (key/value)
    return item[1]      # <- will return the second thing and return item[0] will return the first one

# you may erase this function if you change your sorted function like this:
# for title, count in sorted(counts.item(), key=lambda item: item[1], reverse=True):    # lambda just means give my an anonymouse function. item: is the input to the function. and item[1] is the return value
for title, count in sorted(counts.items(), key=f, reverse=True):     # iterate through dictionary's key, value pairs or in this case title, count pairs. # without .items() method you iterate only through keys.
    print(title, count, sep=" | ")      # sep argument allows sustitution of space default separator by other symbol