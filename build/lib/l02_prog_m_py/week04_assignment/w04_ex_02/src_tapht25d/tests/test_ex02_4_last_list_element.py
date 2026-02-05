"""Module for tests, L02, W04, Ex02, part 4."""

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
from ..ex02_functions import ex02_04_last_element
# pylint: enable=import-error


def test_ex02_04_last_element__correct_print():
    """Used for unit test of function ex02_04_last_element.

    Check for correct printout.
    """
    use_as_list_04 = [1, 2, 3]
    last_element = 3
    assert ex02_04_last_element(use_as_list_04) == last_element


def test_ex02_04_last_element__not_list():
    """Used for unit test of function ex02_04_last_element.

    Check that sending in different argument than
    list (with contents) to parameter for what to find returns None.
    """
    use_int_not_list_04 = 42
    use_float_not_list_04 = 42.42
    use_str_not_list_04 = '42'
    use_tuple_not_list_04 = ('42', '42')
    check_list_of_wrong_04 = [use_int_not_list_04,
                              use_float_not_list_04,
                              use_str_not_list_04,
                              use_tuple_not_list_04]
    for check_list_04 in check_list_of_wrong_04:
        assert ex02_04_last_element(check_list_04) is None


def test_ex02_04_last_element__empty_list():
    """Used for unit test of function ex02_04_last_element.

    Check that sending in an empty list to parameter for what to
    find returns None.
    """
    empty_list = []
    expected = None
    assert ex02_04_last_element(empty_list) == expected
