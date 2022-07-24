import sys


def main():
    '''Input through argv path of file.
    Outputs num of lines of code (LOC) in that file'''

    # Expect exactly one command line argument
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    path = sys.argv[1]

    # Check for .py extension
    is_python = check_extension(path)
    if is_python is False:
        sys.exit("Not a Python file")

    num_of_lines = count_lines(path)
    print(num_of_lines)
    sys.exit(0)


def count_lines(path):
    # Try open python file
    try:
        loc_counter = 0
        with open(path) as file:
            for line in file:
                if len(line.strip()) == 0:  # exclude blank lines
                    continue

                if line.lstrip().startswith("#"):  # exclude comments
                    continue

                loc_counter += 1  # count line
        return loc_counter
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_extension(path):
    '''Input path of file. Outputs True if python file, else outputs False'''
    return path[-3:] == ".py"


if __name__ == "__main__":
    main()
