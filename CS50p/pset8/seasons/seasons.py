from datetime import date, datetime


def main():
    # prompt for date of birth
    # bday_str = input("Date of Birth: ")
    bday_str = "1999-01-01"

    # convert str date to dastetime date
    bday = datetime.strptime(bday_str, "%Y-%m-%d").date()

    # todays date
    # today = date.today()
    today_str = "2000-01-01"
    today = datetime.strptime(today_str, "%Y-%m-%d").date()

    # delta between today and bday
    delta = today - bday

    # convert delta into minutes
    delta_minutes = delta.total_seconds() / 60
    print(delta_minutes)

    # rounded to nearest integer

    ...
    # print age in minutes with words,


def convert_to_minutes():
    ...


if __name__ == "__main__":
    main()
