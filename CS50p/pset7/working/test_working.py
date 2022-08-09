import pytest
from working import convert


def test_no_colon():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_mix_colon():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"


def test_round_hours():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_half_hours():
    assert convert("5:30 PM to 9:00 AM") == "17:30 to 09:00"


def test_reverse_hours():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_value_errors():
    with pytest.raises(ValueError):
        assert convert("8:60 AM to 4:60 PM")
        assert convert("9AM to 5PM")
        assert convert("09:00 to 17:00")
        assert convert("9 AM - 5 PM")
        assert convert("10:7 AM to 5:1 PM")
