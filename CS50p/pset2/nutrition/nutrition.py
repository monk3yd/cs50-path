def main():
    FOOD_CHART = [
        {"name": "apple", "calories": 130},
        {"name": "avocado", "calories": 50},
        {"name": "banana", "calories": 110},
        {"name": "cantaloupe", "calories": 50},
        {"name": "grapefruit", "calories": 60},
        {"name": "grapes", "calories": 90},
        {"name": "honeydew melon", "calories": 50},
        {"name": "kiwifruit", "calories": 90},
        {"name": "lemon", "calories": 15},
        {"name": "lime", "calories": 20},
        {"name": "nectarine", "calories": 60},
        {"name": "orange", "calories": 80},
        {"name": "peach", "calories": 60},
        {"name": "pear", "calories": 100},
        {"name": "pineapple", "calories": 50},
        {"name": "plums", "calories": 70},
        {"name": "strawberries", "calories": 50},
        {"name": "sweet cherries", "calories": 100},
        {"name": "tangerine", "calories": 50},
        {"name": "watermelon", "calories": 80},
    ]

    item = input("Item: ").lower()
    kcal = search_calories(item, FOOD_CHART)
    if kcal is None:
        return 1
    print(f"Calories: {kcal}")


def search_calories(item, fruit_chart):
    for fruit in fruit_chart:
        if fruit["name"] == item:
            return fruit["calories"]


if __name__ == "__main__":
    main()
