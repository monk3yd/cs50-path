import sys

from PIL import Image, ImageOps


def main():
    # Expect 2 command-line arguments
    is_valid = check_arguments(sys.argv)
    if is_valid is False:
        sys.exit(is_valid)

    input = sys.argv[1]
    output = sys.argv[2]

    # Check formats (.jpg .jpeg .png)
    format_ok = check_formats(input, output)
    if isinstance(format_ok, str):
        sys.exit(format_ok)

    # Open input file
    try:
        shirt_image = Image.open("shirt.png")
        input_image = Image.open(input)
        image = ImageOps.fit(input_image, size=(600, 600))
        image.paste(shirt_image, (0, 0), mask=shirt_image)
        image.save(output)

    except FileNotFoundError:
        sys.exit("Input does not exist")

    sys.exit(0)


def check_formats(input, output):
    valid_formats = [".jpg", ".jpeg", ".png"]
    keep_going = True
    # Check for invalid output extension
    for format in valid_formats:
        if output.endswith(format):
            keep_going = True
            break
        keep_going = False

    if keep_going is False:
        return "Invalid output"

    # Check input and output different extensions
    for format in valid_formats:
        if input.endswith(format) and output.endswith(format):
            return True
    return "Input and output have different extensions"


def check_arguments(args):
    if len(args) < 3:
        return "Too few command-line arguments"

    if len(args) > 3:
        return "Too many command-line arguments"
    return True


if __name__ == "__main__":
    main()
