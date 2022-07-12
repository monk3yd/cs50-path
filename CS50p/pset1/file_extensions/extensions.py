def main():
    file = input("File name: ").lower().strip()
    mimetype = get_mimetype(file)
    print(mimetype)


def get_mimetype(file):
    extension = file.split(".")[-1]

    if extension == "jpg" or extension == "jpeg":
        return f"image/jpeg"
    elif extension == "pdf" or extension == "zip":
        return f"application/{extension}"
    elif extension == "gif" or extension == "png":
        return f"image/{extension}"
    elif extension == "txt":
        return f"text/plain"
    else:
        return "application/octet-stream"


main()
