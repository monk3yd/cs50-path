import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "3"


def test_deposit():
    jar = Jar()
    jar.deposit(7)
    assert jar.size == 7

    with pytest.raises(ValueError):
        jar.deposit(7)


def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(4)
    assert jar.size == 3

    with pytest.raises(ValueError):
        assert jar.withdraw(7)
