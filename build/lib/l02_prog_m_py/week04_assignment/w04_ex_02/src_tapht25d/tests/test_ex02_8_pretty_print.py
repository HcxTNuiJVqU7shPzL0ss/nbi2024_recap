"""Module for tests, L02, W04, Ex02, part 8."""

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
from ..ex02_functions import ex02_08_pretty_print
# pylint: enable=import-error


def test_ex02_08_pretty_print__correct_return():
    """Used for unit test of function ex02_08_pretty_print.

    Check for correct return result.
    """
    use_as_list_08 = ['a', 1, 3, 2]
    assert ex02_08_pretty_print(use_as_list_08) == use_as_list_08


def test_ex02_08_pretty_print__not_list():
    """Used for unit test of function ex02_08_pretty_print.

    Check that sending in different argument than
    list to parameter for what to find returns None.
    """
    use_int_not_list_08 = 42
    use_float_not_list_08 = 42.42
    use_str_not_list_08 = '42'
    use_tuple_not_list_08 = ('42', '42')
    check_list_of_wrong_08 = [use_int_not_list_08,
                              use_float_not_list_08,
                              use_str_not_list_08,
                              use_tuple_not_list_08]
    for check_list_08 in check_list_of_wrong_08:
        assert ex02_08_pretty_print(check_list_08) is None


def test_ex02_08_pretty_print__empty_list():
    """Used for unit test of function ex02_08_pretty_print.

    Check that sending in an empty list to parameter for what to
    find returns None.
    """
    empty_list = []
    expected = 'The list is empty'
    assert ex02_08_pretty_print(empty_list) == expected
