import sys
import random


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                continue
            break
        except ValueError:
            continue

    random_num = random.randint(1, level)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue

            if guess < random_num:
                print("Too small!")
                continue
            elif guess > random_num:
                print("Too large!")
                continue
            else:
                print("Just right!")
                sys.exit(0)
        except ValueError:
            continue


if __name__ == "__main__":
    main()
