from cs50 import get_int

while True:
    h = get_int("height: ")
    if h > 0 and h < 9:
        break

for i in range(h):
    for j in range(h):
        if j < (h - 1) - i:
            print(" ", end="")
        else:
            print("#", end="")
    print()