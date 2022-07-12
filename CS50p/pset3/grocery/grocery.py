def main():
    groceries = {}
    while True:
        try:
            item = input().upper()
            if item not in groceries:
                groceries[item] = 1
            else:
                groceries[item] += 1
        except EOFError:
            break

    for key, value in sorted(groceries.items()):
        print(value, key)


if __name__ == '__main__':
    main()
