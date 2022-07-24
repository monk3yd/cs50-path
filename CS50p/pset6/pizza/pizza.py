import sys
import csv

from tabulate import tabulate


def main():
    # Expect only 1 command-line argument
    is_valid = check_arguments(sys.argv)
    if isinstance(is_valid, str):
        sys.exit(is_valid)

    path = sys.argv[1]

    # Expect csv file
    is_csv = check_extension(path)
    if not is_csv:
        sys.exit("Not a CSV file")

    table = generate_table(path)
    if table is False:
        sys.exit("File does not exist")
    print(table)
    sys.exit(0)


def generate_table(path):
    try:
        pizzas = []
        with open(path) as file:
            reader = csv.DictReader(file)
            for pizza in reader:
                pizzas.append(pizza)

        table = tabulate(pizzas, headers="keys", tablefmt="grid")
        return table
    except FileNotFoundError:
        return False


def check_arguments(argv):
    if len(argv) < 2:
        return "Too few command-line arguments"

    if len(argv) > 2:
        return "Too many command-line arguments"
    return True


def check_extension(path):
    return path[-4:] == ".csv"


if __name__ == "__main__":
    main()
