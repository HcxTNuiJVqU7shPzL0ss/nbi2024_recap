# pylint: skip-file
# noqa
from exc_1_5 import find_2nd_max


def test_empty_list():
    # noqa
    expected = None
    actual = find_2nd_max([])
    assert actual == expected

def test_one_element():
    # noqa
    assert find_2nd_max([12]) == None

def test_int_list():
    # noqa
    assert find_2nd_max([4, 1, 2, 3]) == 3
    assert find_2nd_max([345, 3, 79]) == 79
    assert find_2nd_max([100, 4, 4, -12]) == 4
    assert find_2nd_max([-12, -13, -14]) == -13
