from pizza import check_arguments, check_extension


def test_check_arguments():
    assert check_arguments(["pizza.py", "regular.csv"]) is True
    assert check_arguments(["pizza.py"]) == "Too few command-line arguments"
    assert (
        check_arguments(["pizza.py", "regular.csv", "sicilian.csv"])
        == "Too many command-line arguments"
    )


def test_check_extension():
    assert check_extension("regular.csv") is True
    assert check_extension("regular") is False
