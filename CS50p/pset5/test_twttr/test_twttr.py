from twttr import shorten


def main():
    test_shorten_input_mayus()
    test_shorten_input_minus()
    test_shorten_input_caps()
    test_shorten_no_input()
    test_shorten_zero()
    test_shorten_positive_num()
    test_shorten_negative_num()
    test_shorten_punctuation()


def test_shorten_input_mayus():
    assert shorten("JUAN") == "JN"
    assert shorten("WEASLEY") == "WSLY"


def test_shorten_input_minus():
    assert shorten("juan") == "jn"
    assert shorten("weasley") == "wsly"

def test_shorten_input_caps():
    assert shorten("Juan") == "Jn"
    assert shorten("Weasley") == "Wsly"


def test_shorten_no_input():
    assert shorten("") == ""


def test_shorten_zero():
    assert shorten("000") == "000"


def test_shorten_positive_num():
    assert shorten("2") == "2"


def test_shorten_negative_num():
    assert shorten("-3") == "-3"


def test_shorten_punctuation():
    assert shorten("Juan.") == "Jn."
