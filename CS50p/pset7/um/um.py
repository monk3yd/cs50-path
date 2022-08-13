import re
import sys


def main():
    print(count(input("Text: ")))
    sys.exit(0)


def count(text):
    pattern = r"^(Um|um)|\s+(um)[. ,]"
    if matches := re.findall(pattern, text):
        # print(matches)
        return len(matches)
    return sys.exit(1)


if __name__ == "__main__":
    main()
