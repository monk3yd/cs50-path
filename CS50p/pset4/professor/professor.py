import sys
import random


def main():
    level = get_level()
    incorrect_counter = 0
    score = 0
    for _ in range(10):
        # Generate random numbers for question
        random_x = generate_integer(level)
        random_y = generate_integer(level)

        # Generate correct answer
        answer = random_x + random_y

        while True:
            # Get user input for answer
            answer_input = int(input(f"{random_x} + {random_y} = "))
            if answer != answer_input:  # Incorrect answer
                print("EEE")
                incorrect_counter += 1
                if incorrect_counter == 3:
                    print(f"{random_x} + {random_y} = {answer}")  # Display correct answer after 3 fails
                    break
                continue

            # Correct answer
            score += 1
            break

        incorrect_counter = 0

    print(f"Score: {score}")
    sys.exit(0)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 3 or level < 1:  # Level out or accepted range
                continue
        except ValueError:
            continue
        else:
            return level


def generate_integer(level):
    if level == 1:
        random_num = random.randint(0, 9)

    if level == 2:
        random_num = random.randint(10, 99)

    if level == 3:
        random_num = random.randint(100, 999)

    return random_num


if __name__ == "__main__":
    main()
