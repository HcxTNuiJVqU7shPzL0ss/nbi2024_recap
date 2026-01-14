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

    Ensure master_list is an actual list.
    Handles ac_006, parts 1 through 4.
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
