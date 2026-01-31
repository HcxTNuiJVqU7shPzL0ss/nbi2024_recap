# pylint: skip-file
# noqa
from exc_1_4 import find_max


def test_empty_list():
    # noqa
    expected = None
    actual = find_max([])
    assert actual == expected

def test_int_list():
    # noqa
    assert find_max([5,5,5,5,9]) == 9
    assert find_max([105, 5, -5985, 500, 9]) == 500
    assert find_max([-999, 1.1]) == 1.1

def test_str_list():
    # noqa
    assert find_max(['z','g','e','r','99999']) == 'z'
