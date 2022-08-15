from seasons import check_format, convert_minutes_to_words


def test_check_format():
    assert check_format("1999-01-01") == "1999-01-01"
    assert check_format("2000-01-01") == "2000-01-01"
    assert check_format("01-02-1993") is False


def test_convert_minutes_to_words():
    assert convert_minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
