from cs50 import get_string

s = get_string("Do you agree?\n")

#if s == "Y" or s == "y":
if s.lower() in ["y", "yes"]:   #input YES or YeS is valid
    print("Agreed.")
elif s in ["N", "n", "No", "no"]:
    print("Not agreed.")