import re


def main():
    print(parse(input("HTML: ")))


def parse(html: str):
    if matches := re.search(r'src="https?://(www\.)?youtube\.com/embed/(\w+)"', html):
        return f"https://youtu.be/{matches.group(2)}"
    return None


if __name__ == "__main__":
    main()
