import sys
import emoji


def main():
    prompt = input("Input: ")
    print(emoji.emojize(prompt, language="alias"), end="")
    sys.exit(0)


if __name__ == "__main__":
    main()
