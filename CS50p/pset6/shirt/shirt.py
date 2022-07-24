import sys

from PIL import Image


def main():
    # Expect 2 command-line arguments
    is_valid = check_arguments(sys.argv)
    if is_valid is False:
        sys.exit(is_valid)

    input = sys.argv[1]
    output = sys.argv[2]

    # Check formats (.jpg .jpeg .png)
    check_formats(input, output)


def check_formats(input, output):
    valid_formats = [".jpg", ".jpeg", ".png"]
    for format in valid_formats:
        if input.endswith(format):
            return True
    
    return False


def check_arguments(args):
    if len(args) < 3:
        return "Too few command-line arguments"

    if len(args) > 3:
        return "Too many command-line arguments"
    return True


if __name__ == "__main__":
    main()
