# pylint: skip-file
# noqa
from exc_2_funcs import *


# Unit test for some Celsius to Fahrenheit values
def test_c_2_f():
    # noqa
    assert c_t_f(0) == 32
    assert c_t_f(-17) == 1.4
    assert c_t_f(5) == 41
    assert c_t_f(48.5) == 119.3
    assert c_t_f(-40) == -40


# Unit test for a too low (Celsius) value
def test_c_too_cold():
    # noqa
    expected = None
    actual = c_t_f(-273.16)
    assert actual == expected


# Unit test to count words in an empty string
def test_empty_string():
    # noqa
    expected = None
    actual = count_words("")
    assert actual == expected


# Unit test to count words in a string
def test_cnt_words():
    # noqa
    assert count_words("one") == 1
    assert count_words("one two") == 2
    assert count_words("one two three four") == 4
