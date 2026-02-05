"""Module for tests, L02, W04, Ex05."""

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
from ..ex02_functions import (ex02_05_cut_edges)
# pylint: enable=import-error


def test_ex02_05_cut_edges__correct_print():
    """Used for unit test of function ex02_05_cut_edges.

    Check for correct printout.
    """
    use_as_list_05 = [1, 2, 3]
    remaining_element = [2]
    assert ex02_05_cut_edges(use_as_list_05) == remaining_element


def test_ex02_05_cut_edges__not_list():
    """Used for unit test of function ex02_05_cut_edges.

    Check that sending in different argument than
    list (with contents) to parameter for what to find returns None.
    """
    use_int_not_list_05 = 42
    use_float_not_list_05 = 42.42
    use_str_not_list_05 = '42'
    use_tuple_not_list_05 = ('42', '42')
    check_list_of_wrong_05 = [use_int_not_list_05,
                              use_float_not_list_05,
                              use_str_not_list_05,
                              use_tuple_not_list_05]
    for check_list_05 in check_list_of_wrong_05:
        assert ex02_05_cut_edges(check_list_05) is None


def test_ex02_05_cut_edges__empty_list():
    """Used for unit test of function ex02_05_cut_edges.

    Check that sending in an empty list to parameter for what to
    find returns None.
    """
    empty_list = []
    expected = None
    assert ex02_05_cut_edges(empty_list) == expected


def test_ex02_05_cut_edges__short_list():
    """Used for unit test of function ex02_05_cut_edges.

    Check that sending in a list with less than three (3) arguments
    to parameter for what to find returns None.
    """
    short_list_1 = [1]
    short_list_2 = [1, 2]
    list_of_short = [short_list_1, short_list_2]
    expected = None
    for check_short_05 in list_of_short:
        assert ex02_05_cut_edges(check_short_05) == expected
