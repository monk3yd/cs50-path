import re
# import sys


def main():
    # Original
    print(convert(input("Hours: ")))

    # Payloads
    # print(convert("9AM to 5PM"))


def convert(work_time: str):
    time = []
    pattern = r"([0-9:]+)\s(AM|PM)"
    if "to" not in work_time:
        raise ValueError
    if matches := re.findall(pattern, work_time):
        for match in matches:
            if match[1] == "AM":
                if ":" in match[0]:
                    hour, minutes = match[0].split(":")
                    if int(minutes) > 59:
                        raise ValueError

                    if hour == "12":
                        hour = "0"

                    if int(hour) >= 10:
                        am_time = f"{hour}:{minutes}"
                    else:
                        am_time = f"0{hour}:{minutes}"
                else:
                    minutes = "00"
                    hour = match[0]
                    if hour == "12":
                        hour = "0"

                    if int(hour) >= 10:
                        am_time = f"{hour}:{minutes}"
                    else:
                        am_time = f"0{hour}:{minutes}"

                # print(am_time)
                time.append(am_time)

            if match[1] == "PM":
                if ":" in match[0]:
                    hour, minutes = match[0].split(":")
                    if int(minutes) > 59:
                        raise ValueError

                    if int(hour) != 12:
                        hour = str(int(hour) + 12)
                    pm_time = f"{hour}:{minutes}"
                else:
                    hour = match[0]
                    if int(hour) != 12:
                        hour = str(int(hour) + 12)
                    pm_time = f"{hour}:00"

                # print(pm_time)
                time.append(pm_time)

    try:
        return f"{time[0]} to {time[1]}"
    except IndexError:
        raise ValueError


if __name__ == "__main__":
    main()
