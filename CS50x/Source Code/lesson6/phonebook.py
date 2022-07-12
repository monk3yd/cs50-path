#keys are always strings : values may be anything you want

from sys import exit

people = {
    "EMMA": "617-555-0100",
    "RODRIGO": "615-555-0101",
    "BRIAN": "615-555-0102",
    "DAVID": "615-555-0103",
}

if "EMMA" in people:
    print(f"Found {people['EMMA']}")
    exit(0)
print("Not found")
exit(1)