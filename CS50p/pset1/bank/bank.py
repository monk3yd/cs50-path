def main():
    greeting = input("Greeting: ").lower().strip()
    wins = calculate_greeting(greeting)
    print(f"${wins}")


def calculate_greeting(greeting):
    if greeting.startswith("hello"):
        return str(0)
    elif greeting.startswith("h"):
        return str(20)
    else:
        return str(100)


main()
