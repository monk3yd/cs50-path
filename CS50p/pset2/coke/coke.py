def main():
    valid_coins = [25, 10, 5]
    coke_price_left = 50

    while coke_price_left > 0:
        print(f"Amount Due: {coke_price_left}")
        inserted_coin = int(input("Insert Coin: "))
        if inserted_coin not in valid_coins:
            # print("This machine accepts only 25, 10 and 5 cents coins.")
            continue
        coke_price_left -= inserted_coin
        # print(coke_price_left)

    print(f"Change Owed: {abs(coke_price_left)}")


if __name__ == "__main__":
    main()
