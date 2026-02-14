"""Module for tests, L02, W05, Ex02.

Handling unit test of function: is_sorted_ascending.
"""

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


from ..src.w05_ex02_functions import is_sorted_ascending


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
