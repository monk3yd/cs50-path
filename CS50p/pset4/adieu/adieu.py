import sys
import keyboard


def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            pass

        if keyboard.is_pressed("control + d"):
            break

    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
        sys.exit(0)

    if len(names) == 2:
        last_name = f"and {names[-1]}"
        print(f"Adieu, adieu, to {names[0]} {last_name}")
        sys.exit(0)

    names_str = " "
    for name in names[:-1]:
        names_str += " " + name + ","
    last_name = f"and {names[-1]}"
    print(f"Adieu, adieu, to {names_str.strip()} {last_name}")

    sys.exit(0)


if __name__ == "__main__":
    main()
