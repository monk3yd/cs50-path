import sys


def main():
    while True:
        percentage = convert(input("Fraction: "))
        if percentage > 100 or percentage < 0:
            continue
        break

    response = gauge(percentage)
    print(response)
    sys.exit(0)


def convert(fraction):
    try:
        x = int(fraction.split("/")[0])
        y = int(fraction.split("/")[1])

    except (ValueError, ZeroDivisionError, TypeError) as error:
        raise error

    else:
        float_fraction = x / y
        rounded_fraction = round(float_fraction, 2)
        percentage = rounded_fraction * 100
        return int(percentage)


def gauge(percentage):
    if 100 >= percentage >= 99:
        fuel = "F"
        return f"{fuel}"
    elif 1 >= percentage >= 0:
        fuel = "E"
        return f"{fuel}"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
