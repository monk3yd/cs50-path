def main():
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    string = input("Input: ")

    # final_string = [string.replace(vowel, "") for vowel in vowels if vowel in string]
    for vowel in vowels:
        if vowel in string:
            string = string.replace(vowel, "")

    print(string)


if __name__ == "__main__":
    main()
