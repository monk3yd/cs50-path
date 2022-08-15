import re
import sys
import inflect

from datetime import date, datetime


def main():
    # prompt for date of birth
    bday_str = check_format(input("Date of Birth: "))
    # bday_str = "1999-01-01"
    if bday_str is False:
        sys.exit(1)

    # convert str date to datetime date
    bday = datetime.strptime(bday_str, "%Y-%m-%d").date()

    # todays date
    today = date.today()

    # delta between today and bday
    delta = today - bday

    # convert delta into minutes
    delta_minutes = int(delta.total_seconds() / 60)

    # convert age in minutes to words,
    minutes_words = convert_minutes_to_words(delta_minutes)
    print(f"{minutes_words} minutes")

    sys.exit(0)


def check_format(input):
    if matches := re.search(r"^\d{4}-\d{2}-\d{2}$", input):
        return input
    return False


def convert_minutes_to_words(minutes):
    inf = inflect.engine()
    delta_words = inf.number_to_words(minutes)
    text = delta_words.capitalize()
    return re.sub(r"\sand\s", " ", text)


if __name__ == "__main__":
    main()
