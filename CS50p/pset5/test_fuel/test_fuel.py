import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("4/4") == 100
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("0/4") == 0


def test_value_error():
    with pytest.raises(ValueError):
        convert("cat")
        convert("cat/4")
        convert("True")


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(40) == "40%"
    assert gauge(80) == "80%"

