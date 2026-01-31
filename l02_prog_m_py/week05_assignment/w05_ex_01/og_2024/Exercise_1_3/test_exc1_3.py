# pylint: skip-file
# noqa
from exc_1_3 import count_vowels


def test_no_vowels():
    # noqa
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0

def test_vowels():
    # noqa
    assert count_vowels("aArreE") == 4
    assert count_vowels("PPllOouui") == 5
