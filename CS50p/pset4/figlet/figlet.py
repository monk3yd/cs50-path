import sys
import random
from pyfiglet import Figlet, FigletFont


def main():
    # Get list of all available fonts
    fig_fonts = FigletFont.getFonts()

    valid = validate_cli_args(fonts=fig_fonts)
    if valid is False:
        sys.exit("Invalid usage")

    prompt = input("Input: ")

    if len(sys.argv) == 1:
        fig_random(prompt, fonts=fig_fonts)
        sys.exit(0)

    fig_cli(prompt)
    sys.exit(0)


def fig_cli(prompt):
    try:
        font = sys.argv[2]
        fig = Figlet(font=font)
        print(f"{fig.renderText(prompt)}")

    except IndexError:
        sys.exit("Need to pass font as command-line argument.")


def fig_random(prompt, fonts):
    random_font = random.choice(fonts)
    fig = Figlet(font=random_font)
    print(f"{fig.renderText(prompt)}")


def validate_cli_args(fonts):
    '''Check if the amount of cli arguments entered are valid or not.'''
    is_valid = False
    if len(sys.argv) == 1 or len(sys.argv) == 3:
        is_valid = True

    if is_valid is False:
        return is_valid

    ''' Check if cli name arguments are valid or not.'''
    try:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in fonts:
                # print(sys.argv[2])
                return True

        return False
    except IndexError:
        if len(sys.argv) == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    main()
