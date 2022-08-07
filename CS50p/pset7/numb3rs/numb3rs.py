import re


def main():
    # test_ip = "127.0.0.1"
    # print(validate(test_ip))
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip: str) -> bool:
    """Check if IP address is valid."""
    if matches := re.search(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        for i in range(1, 5):
            if int(matches.group(i)) > 255 or int(matches.group(i)) < 0:
                return False
        return True
    return False


if __name__ == "__main__":
    main()
