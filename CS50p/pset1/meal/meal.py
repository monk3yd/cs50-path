def main():
    time = input("What time is it? ")
    format_time = convert(time)
    if 7 <= format_time <= 8:
        print("breakfast time")

    if 12 <= format_time <= 13:
        print("lunch time")

    if 18 <= format_time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    if "p.m." in minutes:
        minutes = minutes.split(" ")[0]
        hours += 12

    if "a.m" in minutes:
        minutes = minutes.split(" ")[0]

    format_time = hours + float(minutes) / 60
    return format_time


if __name__ == "__main__":
    main()
