#in python ints can't overflow. floats do

from time import sleep

i = 1
while True:
    print(i)
    sleep(0.1)
    i *= 2