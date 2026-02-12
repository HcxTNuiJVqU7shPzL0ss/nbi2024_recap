"""Module for tests, L02, W05, Ex02."""

#####################################################################
# Copyright 2026 gnoff
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#####################################################################


from ..src.w05_ex02_functions import (c_to_f,
                                      find_median,
                                      is_sorted_ascending)


####


def test_c_to_f__too_cold():
    """Used for unit test of function c_to_f.

    Check if below absolute zero, result shall be None.
    """

    expected = None
    actual = c_to_f(-300)
    assert actual == expected
    actual = c_to_f(-273.16)
    assert actual == expected


def test_c_to_f__check_temps():
    """Used for unit test of function c_to_f.

    Check if at absolute zero or higher.
    """

    assert round(c_to_f(-273.15), 2) == -459.67
    assert c_to_f(0) == 32
    assert c_to_f(-40) == -40
    assert c_to_f(1000) == 1832


####


def test_find_median__not_list():
    """Used for unit test of function find_median.

    Check that non list used as input returns False.
    For ac_001, parts 1 through 4.
    """

    expected = False

    a_int = find_median(42)
    b_float = find_median(3.14)
    c_str = find_median('42')
    d_tuple = find_median((1, 2))

    assert a_int == b_float
    assert c_str == d_tuple
    assert a_int == d_tuple

    assert b_float == expected


def test_find_median__list_with_non_numeral():
    """Used for unit test of function find_median.

    Check that list including non numerals used as input returns
    False.
    For ac_001, part 5.
    """

    expected = False

    non_numeral_list = ['a', 'b']
    some_numeral_list = [1, 2, 3, 'a', 42]

    check_non = find_median(non_numeral_list)
    check_some = find_median(some_numeral_list)

    assert check_non == check_some

    assert check_some == expected


def test_find_median__empty_list():
    """Used for unit test of function find_median.

    Check if empty list used as input returns None.
    For ac_002.
    """
    expected = None

    a_empty_check = []
    a = find_median(a_empty_check)

    assert a == expected


def test_find_median__short_list():
    """Used for unit test of function find_median.

    Check if too short list used as input returns None.
    For ac_003.
    """
    expected = None

    a_short_check = [42]
    a = find_median(a_short_check)

    assert a == expected


def test_find_median__even_list():
    """Used for unit test of function find_median.

    Check list with even number of elements (more than two).
    Return the median as the two middle values added,
    then div by 2.
    For ac_004 and ac_005.
    """
    # 2 values --> (1 + 41) / 2
    assert find_median([41, 1]) == 21
    # 4 values --> (25 + 25) / 2
    assert find_median([100, 25, 25, 10]) == 25
    # 8 values --> (25 + 75) / 2
    assert find_median([900, 800, 700, 75, 1, 2, 3, 25]) == 50


def test_find_median__odd_list():
    """Used for unit test of function find_median.

    Check list with odd number of elements (more than two).
    Return the median as the middle index value.
    For ac_004 and ac_006.
    """
    # 3 values
    assert find_median([3, 41, 1]) == 3
    # 5 values
    assert find_median([100, 75, 25, 10, 50]) == 50
    # 7 values
    assert find_median([800, 700, 75, 1, 2, 3, 25]) == 25


def test_find_median__different_types():
    """Used for unit test of function find_median.

    Check list including different support types, e.g.,
    int, float, positive numbers, negative numbers.
    For ac_007.
    """
    assert find_median([42, 3.14, -100]) == 3.14


####


def test_is_sorted_ascending__not_list():
    """Used for unit test of function is_sorted_ascending.

    Check that non list used as input returns None.
    For ac_001, parts 1 through 4.
    """

    expected = None

    a_int = is_sorted_ascending(1)
    b_float = is_sorted_ascending(1.14)
    c_str = is_sorted_ascending('142')
    d_tuple = is_sorted_ascending((1, 42))

    assert a_int == b_float
    assert c_str == d_tuple
    assert a_int == d_tuple

    assert b_float == expected


def test_is_sorted_ascending__list_with_non_numeral():
    """Used for unit test of function is_sorted_ascending.

    Check that list including non numerals used as input returns
    None.
    For ac_001, part 5.
    """

    expected = None

    non_numeral_list = ['x', 'y']
    some_numeral_list = [5, 6, 10, 's', 142]

    check_non = is_sorted_ascending(non_numeral_list)
    check_some = is_sorted_ascending(some_numeral_list)

    assert check_non == check_some

    assert check_some == expected


def test_is_sorted_ascending__empty_list():
    """Used for unit test of function is_sorted_ascending.

    Check if empty list used as input returns None.
    For ac_002.
    """
    expected = None

    a_empty_check = []
    a = is_sorted_ascending(a_empty_check)

    assert a == expected


def test_is_sorted_ascending__sorted_list():
    """Used for unit test of function is_sorted_ascending.

    Check if numbered list sorted ascending returns True.
    For ac_004, part 1.
    """
    expected = True
    a_list = [1, 42, 100]
    a = is_sorted_ascending(a_list)
    assert a == expected


def test_is_sorted_ascending__unsorted_list():
    """Used for unit test of function is_sorted_ascending.

    Check if numbered list not sorted ascending returns
    False.
    For ac_004, part 2.
    """
    expected = False
    b_list = [110, 42, 100]
    b = is_sorted_ascending(b_list)
    assert b == expected


def test_is_sorted_ascending__different_types():
    """Used for unit test of function is_sorted_ascending.

    Check list including different supported types, e.g.,
    int, float, positive numbers, negative numbers.
    For ac_003.
    """
    assert is_sorted_ascending([42, 3.14, -100]) is False
    assert is_sorted_ascending([-42, 3.14, 100]) is True


####
