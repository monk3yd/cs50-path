from plates import is_valid


def main():
    test_start()
    test_nums()
    test_length()
    test_first_num()
    test_punctuation()


def test_start():
    assert is_valid("AZBB32") is True
    assert is_valid("4ZBB32") is False


def test_nums():
    assert is_valid("AAA222") is True
    assert is_valid("AAA22T") is False
    assert is_valid("AAA2RT") is False


def test_length():
    assert is_valid("A") is False
    assert is_valid("AAA22456") is False


def test_first_num():
    assert is_valid("AB02") is False


def test_punctuation():
    assert is_valid("BB20.") is False
    assert is_valid("BB.20") is False


if __name__ == "__main__":
    main()
