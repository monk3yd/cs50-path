from bank import value


def main():
    test_value_hello()
    test_value_h()
    test_value_other()
    test_no_value()
    test_value_num()


def test_value_hello():
    assert value("hello this is a mockup") == 0
    assert value("HELLO THIS IS A MOCKUP") == 0


def test_value_h():
    assert value("hahahaha") == 20
    assert value("H THIS IS A MOCKUP") == 20


def test_value_other():
    assert value("this must be a 100") == 100


def test_no_value():
    assert value("") == 100


def test_value_num():
    assert value("0") == 100


if __name__ == "__main__":
    main()
