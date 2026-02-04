"""Module for tests, L02, W04, Ex02.2, part b."""

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


# pylint: disable=import-error
from ..ex02_functions import (ex02_02b_echo_multi)
# pylint: enable=import-error


def test_ex02_02b_echo_multi__correct_print():
    """Used for unit test of function ex02_02b_echo_multi.

    Check for correct printout.
    """
    multiplier = 4
    use_for_echo_multi = 'echo multi'
    expected_1 = use_for_echo_multi * multiplier
    expected_2 = 'echo multiecho multiecho multiecho multi'
    expected_list = [expected_1, expected_2]
    for expected in expected_list:
        assert ex02_02b_echo_multi(use_for_echo_multi,
                                   multiplier) == expected


def test_ex02_02b_echo_multi__not_string():
    """Used for unit test of function ex02_02b_echo_multi.

    Check that sending in different argument than
    str to parameter for what to echo returns None.
    """
    multiplier = 3
    use_int_not_str_02b = 42
    use_float_not_str_02b = 42.42
    use_list_not_str_02b = ['42']
    use_tuple_not_str_02b = ('42', '42')
    check_list_str_02b = [use_int_not_str_02b,
                          use_float_not_str_02b,
                          use_list_not_str_02b,
                          use_tuple_not_str_02b]
    for check_str_02b in check_list_str_02b:
        assert ex02_02b_echo_multi(check_str_02b,
                                   multiplier) is None


def test_ex02_02b_echo_multi__not_int():
    """Used for unit test of function ex02_02b_echo_multi.

    Check that sending in different argument than
    int to parameter for what to multiply with returns None.
    """
    echo_str = 'not working'
    use_str_not_int_02b = '42'
    use_float_not_int_02b = 42.42
    use_list_not_int_02b = [42]
    use_tuple_not_int_02b = (42, 42)
    check_list_int_02b = [use_str_not_int_02b,
                          use_float_not_int_02b,
                          use_list_not_int_02b,
                          use_tuple_not_int_02b]
    for check_int_02b in check_list_int_02b:
        assert ex02_02b_echo_multi(echo_str,
                                   check_int_02b) is None
