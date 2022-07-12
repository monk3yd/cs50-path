def main():
    percentage = fraction_to_percentage("Fraction: ")
    print_answer(percentage)


def fraction_to_percentage(prompt):
    while True:
        fraction = input(prompt)
        try:
            x = int(fraction.split("/")[0])
            y = int(fraction.split("/")[1])
            float_fraction = x / y
            rounded_fraction = round(float_fraction, 2)
            percentage = int(rounded_fraction * 100)
            if percentage > 100:
                continue
            return percentage
        except (ValueError, ZeroDivisionError):
            pass


def print_answer(percentage):
    if 100 >= percentage >= 99:
        fuel = "F"
        print(f"{fuel}")
    elif 1 >= percentage >= 0:
        fuel = "E"
        print(f"{fuel}")
    else:
        print(f"{percentage}%")


main()
