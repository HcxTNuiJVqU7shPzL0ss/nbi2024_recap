"""Module for tests, L02, W05, Ex05."""

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


from ..src.w05_ex05_functions import balance_lists


def test_balance_lists__not_list():
    """Used for unit test of function balance_lists.

    Test when either input is not an actual list.
    Checks that None is returned.
    Handles ac_001, parts 1 through 4 (all).
    """
    expected = None
    check_list = ['check']

    # Check "list1" if not a list, while "list2" is a list
    a_int = balance_lists(1, check_list)
    b_float = balance_lists(1.14, check_list)
    c_str = balance_lists('142', check_list)
    d_tuple = balance_lists((1, 42), check_list)

    assert a_int == b_float
    assert c_str == d_tuple
    assert a_int == d_tuple

    # Check "list2" if not a list, while "list1" is a list
    a_int = balance_lists(check_list, 1)
    b_float = balance_lists(check_list, 1.14)
    c_str = balance_lists(check_list, '142')
    d_tuple = balance_lists(check_list, (1, 42))

    assert a_int == b_float
    assert c_str == d_tuple
    assert a_int == d_tuple

    assert b_float[0] == expected


def test_balance_lists__empty_list():
    """Used for unit test of function balance_lists.

    Test when either input is an empty list.
    Checks that two lists are returned.
    Handles ac_002.
    """
    empty_list = []
    non_empty_list = ['not empty']
    # Check first list == empty
    result_1 = balance_lists(empty_list, non_empty_list)
    assert isinstance(result_1[0], list)
    assert isinstance(result_1[1], list)
    # Check second list == empty
    result_2 = balance_lists(non_empty_list, empty_list)
    assert isinstance(result_2[0], list)
    assert isinstance(result_2[1], list)


def test_balance_lists__list_length():
    """Used for unit test of function balance_lists.

    Test that the two input lists works with different length.
    Handles ac_003.
    """
    list_len2 = ['1', '2']
    list_len6 = ['1', '2', '3', '4', '5', '6']
    # Check lists == same len
    result_1 = balance_lists(list_len2, list_len2)
    assert isinstance(result_1[0], list)
    assert isinstance(result_1[1], list)
    # Check first list == longer len than second list
    result_2 = balance_lists(list_len6, list_len2)
    assert isinstance(result_2[0], list)
    assert isinstance(result_2[1], list)
    # Check second list == longer len than first list
    result_3 = balance_lists(list_len2, list_len6)
    assert isinstance(result_3[0], list)
    assert isinstance(result_3[1], list)


def test_balance_lists__balance():
    """Used for unit test of function balance_lists.

    Test that when two input lists differ more than 1 in length,
    two balanced lists with max 1 in len difference is returned.
    Handles ac_004.
    """
    list_len2 = ['1', '2']
    list_len3 = ['1', '2', '3']
    list_len6 = ['1', '2', '3', '4', '5', '6']
    diff_len_too_long = 2
    # Check lists == same len
    result_1 = balance_lists(list_len2, list_len2)
    assert abs(len(result_1[0]) - len(result_1[1])) < diff_len_too_long
    # Check first list == longer len than second list
    result_2 = balance_lists(list_len6, list_len2)
    assert abs(len(result_2[0]) - len(result_2[1])) < diff_len_too_long
    # Check second list == longer len than first list
    result_3 = balance_lists(list_len2, list_len6)
    assert abs(len(result_3[0]) - len(result_3[1])) < diff_len_too_long
    # Check also with an odd len
    result_4 = balance_lists(list_len3, list_len6)
    assert abs(len(result_4[0]) - len(result_4[1])) < diff_len_too_long


def test_balance_lists__types_in_list():
    """Used for unit test of function balance_lists.

    Test that the elements in the list can be of different types.
    Handles ac_005.
    """
    list_1 = [1, 2.23, 'hej', (1, 's'), [1, 'r']]
    list_2 = ['p', 'e', 3.14]
    diff_len_too_long = 2
    result = balance_lists(list_1, list_2)
    assert abs(len(result[0]) - len(result[1])) < diff_len_too_long
