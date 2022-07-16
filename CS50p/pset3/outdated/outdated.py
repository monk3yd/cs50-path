def main():
    while True:
        date = input("Date: ")  # Month/Day/Year
        formatted_date = detect_format(date)
        if formatted_date == "Not valid input format.":
            continue
        break


def detect_format(date):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    if "/" in date:
        try:
            month = int(date.split("/")[0])
            day = int(date.split("/")[1])

            check = check_possible_date(month, day)
            if check is False:
                return "Not valid input format."

            if 9 >= month >= 1:
                month = f"0{month}"

            if 9 >= day >= 1:
                day = f"0{day}"

            year = date.split("/")[2]

            # Output YYYY-MM-DD format
            date = f"{year}-{month}-{day}".replace(" ", "")
            print(date, end="")
        except ValueError:
            return "Not valid input format."

    elif date.split()[0] in months and "," in date.split()[1]:
        month_name = date.split()[0]
        month = months.index(month_name) + 1
        day = int(date.split()[1].replace(",", ""))

        check = check_possible_date(month, day)
        if check is False:
            return "Not valid input format."

        if 9 >= month >= 1:
            month = f"0{month}"

        if 9 >= day >= 1:
            day = f"0{day}"

        year = date.split()[2]

        # Output YYYY-MM-DD format
        date = f"{year}-{month}-{day}".replace(" ", "")
        print(date, end="")
    else:
        return "Not valid input format."


def check_possible_date(month: int, day: int):
    if month > 12 or day > 31:
        return False
    return True


if __name__ == "__main__":
    main()
