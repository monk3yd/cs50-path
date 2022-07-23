import sys


def main():
    while True:
        string = input("Input: ")
        try:
            no_vowel_string = shorten(string)
        except TypeError:
            continue
        else:
            print(no_vowel_string)
            sys.exit(0)


def shorten(word: str) -> str:
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for vowel in vowels:
        if vowel in word:
            word = word.replace(vowel, "")
    return word


if __name__ == "__main__":
    main()
