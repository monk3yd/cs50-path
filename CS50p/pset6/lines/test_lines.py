from lines import check_extension, count_lines


def test_check_extension():
    assert check_extension("hello.py") is True
    assert check_extension("hello") is False
    assert check_extension("") is False


def test_count_lines():
    assert count_lines("hello.py") == 5
