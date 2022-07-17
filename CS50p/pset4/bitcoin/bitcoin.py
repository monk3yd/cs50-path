import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        num_of_bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit(1)

    usd_rate = response.json()["bpi"]["USD"]["rate_float"]

    bitcoin_price = num_of_bitcoin * usd_rate
    bitcoin_price_formatted = f"{bitcoin_price:,.4f}"

    print(f"${bitcoin_price_formatted}")
    sys.exit(0)


if __name__ == "__main__":
    main()
