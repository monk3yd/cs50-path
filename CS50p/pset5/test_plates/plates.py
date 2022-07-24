def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(string):
    # Check for max of 6 chars (leters + nums) and min of 2 chars.
    if not 2 <= len(string) <= 6:
        return False

    # Check for start with 2 letters
    invalid_start_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    first_letter = string[0]
    second_letter = string[1]
    if first_letter in invalid_start_chars or second_letter in invalid_start_chars:
        return False

    try:
        # Make list of indexes of numbers in given string
        num_indexes = [string.index(char) for char in invalid_start_chars if char in string]
        num_indexes.sort(key=int)

        # First num cant be 0
        if string[num_indexes[0]] == "0":
            return False

        # Check numbers must be at the end
        if string[num_indexes[-1]] != string[-1]:
            return False

        checker = num_indexes[0]
        for index in num_indexes:
            if checker != index:
                return False
            checker += 1

    except IndexError:
        pass

    # No periods, spaces or puntuation allowed
    invalid_punctuation = [".", " ", "!", "?"]
    for punctuation in invalid_punctuation:
        if punctuation in string:
            return False
    return True


if __name__ == "__main__":
    main()
