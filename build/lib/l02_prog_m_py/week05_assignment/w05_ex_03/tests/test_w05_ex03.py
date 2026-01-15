"""Module for tests, L02, W05, Ex03."""

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


from ..src.w05_ex03_functions import auto_complete, global_list


def test_auto_complete__master_not_list():
    """Used for unit test of function auto_complete.

    Test when master_list is not an actual list.
    Checks that None is returned.
    Handles ac_006, parts 1 through 4 (all).
    """
    expected = None
    dummy_input = 'dummy'

    a_int = auto_complete(dummy_input, 1)
    b_float = auto_complete(dummy_input, 1.14)
    c_str = auto_complete(dummy_input, '142')
    d_tuple = auto_complete(dummy_input, (1, 42))

    assert a_int == b_float
    assert c_str == d_tuple
    assert a_int == d_tuple

    assert b_float[0] == expected


def test_auto_complete__master_list_with_non_str():
    """Used for unit test of function auto_complete.

    Check that master_list including non str returns None.
    For ac_007.
    """
    expected = None
    dummy_input = 'dummy'

    non_str_list = [5, 65]
    some_str_list = [5, 'Maria', 10, 's', 142]

    check_non = auto_complete(dummy_input, non_str_list)
    check_some = auto_complete(dummy_input, some_str_list)

    assert check_non == check_some
    assert check_some[0] == expected


def test_auto_complete__empty_master_list():
    """Used for unit test of function auto_complete.

    Check if empty master_list used, returns None.
    For ac_004.
    """
    expected = None
    dummy_input = 'dummy'

    a_empty_check = []
    a = auto_complete(dummy_input, a_empty_check)

    assert a[0] == expected


def test_auto_complete__input_not_str():
    """Used for unit test of function auto_complete.

    Test when input_str is not a string (of at least length 1).
    Checks that an empty result (list) is returned.
    Handles ac_001, parts 1 through 5 (all).
    """
    expected = []

    a_int = auto_complete(1, global_list)
    b_float = auto_complete(3.14, global_list)
    c_empty_str = auto_complete('', global_list)
    d_tuple = auto_complete((1, 42), global_list)
    e_list = auto_complete(['ab'], global_list)

    assert a_int == b_float
    assert c_empty_str == d_tuple
    assert a_int == d_tuple
    assert b_float == e_list

    assert b_float == expected


def test_auto_complete__input_not_found():
    """Used for unit test of function auto_complete.

    Test when input_str is not found in master_list.
    Returns empty list.
    Handles ac_003, part 1, also ac_002.
    """
    expected = []

    a_not_part_of_list = 'Oscar'
    b_not_part_of_list = 'orange'

    a_check = auto_complete(a_not_part_of_list, global_list)
    b_check = auto_complete(b_not_part_of_list, global_list)

    assert a_check == b_check
    assert a_check == expected


def test_auto_complete__input_found():
    """Used for unit test of function auto_complete.

    Test when input_str is found in master_list.
    Returns list of found item(s).
    Handles ac_003, part 2, also ac_002.
    """
    a_expected = ['Maria Bylund', 'Marie Hson-Larson']
    a_str_search = 'Mar'
    a_check = auto_complete(a_str_search, global_list)
    assert a_check == a_expected

    b_expected = ['banana']
    b_str_search = 'an'
    b_check = auto_complete(b_str_search, global_list)
    assert b_check == b_expected


def test_auto_complete__case_insensitive():
    """Used for unit test of function auto_complete.

    Ensure case does not matter.
    Handles ac_005.
    """
    a_expected = ['Maria Bylund', 'Marie Hson-Larson']
    a_str_search = 'mar'
    a_check = auto_complete(a_str_search, global_list)
    assert a_check == a_expected

    b_expected = ['banana']
    b_str_search = 'An'
    b_check = auto_complete(b_str_search, global_list)
    assert b_check == b_expected
