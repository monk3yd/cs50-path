import re
import sys
import inflect

from datetime import date, datetime


def main():
    # prompt for date of birth
    bday_str = check_format(input("Date of Birth: "))
    # bday_str = "1999-01-01"

    # convert str date to datetime date
    bday = datetime.strptime(bday_str, "%Y-%m-%d").date()

    # todays date
    today = date.today()
    # today_str = "2000-01-01"
    # today = datetime.strptime(today_str, "%Y-%m-%d").date()

    # delta between today and bday
    delta = today - bday

    # convert delta into minutes
    delta_minutes = int(delta.total_seconds() / 60)

    # convert age in minutes to words,
    inf = inflect.engine()
    delta_words = inf.number_to_words(delta_minutes)
    text = delta_words.capitalize()
    answer = re.sub(r"\sand\s", " ", text)
    print(f"{answer} minutes")

    sys.exit(0)


def check_format(input):
    if matches := re.search(r"^\d{4}-\d{2}-\d{2}$", input):
        # print(matches)
        return input
    sys.exit(1)


if __name__ == "__main__":
    main()
