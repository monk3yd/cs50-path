def main():
    # Get text with rendered emojis
    raw_text = input()
    print(convert(raw_text))

def convert(text):
    """ Render string into emoji text"""
    return text.replace(":)", "🙂").replace(":(", "🙁")

main()