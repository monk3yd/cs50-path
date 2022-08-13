import sys
import validators


def main():
    is_valid = validators.email((input("What's your email address? ")))
    if is_valid:
        print("Valid")
        sys.exit(0)
    print("Invalid")
    sys.exit(0)


if __name__ == "__main__":
    main()
