import re


def main():
    # # test = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    # test = '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    # print(parse(test))
    print(parse(input("HTML: ")))


def parse(html: str):
    if matches := re.search(r'src="https?://(www\.)?youtube\.com/embed/(\w+)"', html):
        return f"https://youtu.be/{matches.group(2)}"
    return None


if __name__ == "__main__":
    main()
