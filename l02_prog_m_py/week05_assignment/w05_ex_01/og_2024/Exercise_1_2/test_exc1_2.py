# pylint: skip-file
# noqa
from exc_1_2 import sum_list


def test_empty_list():
    # noqa
    expected = 0
    actual = sum_list([])
    assert actual == expected


def test_number_list():
    # noqa
    assert sum_list([5]) == 5
    assert sum_list([1,2]) == 3
    assert sum_list([15,5]) == 20
    assert sum_list([-1,1]) == 0
    assert sum_list([1.2,1.8]) == 3
    assert sum_list(['a']) == 0
