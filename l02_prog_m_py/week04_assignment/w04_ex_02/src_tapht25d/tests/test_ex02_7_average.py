"""Module for tests, L02, W04, Ex02, part 7."""

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


import math


# pylint: disable=import-error
from ..ex02_functions import (ex02_07_average)
# pylint: enable=import-error


def test_ex02_07_average__correct_return_int():
    """Used for unit test of function ex02_07_average.

    Check for correct return value.
    USing integers.
    """
    # Test with pos int for x and y
    use_as_start_int_x = 1
    use_as_start_int_y = 83
    expected_int = 42
    assert ex02_07_average(use_as_start_int_x,
                           use_as_start_int_y) == expected_int
    # Test with neg int for x and y
    use_as_neg_int_x = -42
    use_as_neg_int_y = -2
    expected_neg_int = -22
    assert ex02_07_average(use_as_neg_int_x,
                           use_as_neg_int_y) == expected_neg_int


def test_ex02_07_average__correct_return_float():
    """Used for unit test of function ex02_07_average.

    Check for correct return value, using float.
    Since the average that is returned may include rounding
    errors, this has also been handled.
    """
    # Test with pos float for x and y
    use_as_start_float_x = 41.1
    use_as_start_float_y = 0.9
    expected_float = 21
    assert ex02_07_average(use_as_start_float_x,
                           use_as_start_float_y) == expected_float
    # Test with neg float for x and y
    use_as_neg_float_x = -42.42
    use_as_neg_float_y = -0.58
    expected_neg_float = -21.5
    assert ex02_07_average(use_as_neg_float_x,
                           use_as_neg_float_y) == expected_neg_float
    # Test with an approximate value as result
    use_approx_x = 1.000000003
    use_approx_y = 1.00000000042
    expected_approx = 1
    get_absolute = (ex02_07_average(use_approx_x,
                           use_approx_y))
    check_if_close = math.isclose(get_absolute, expected_approx,
                                  rel_tol=1e-05)
    assert check_if_close is True


def test_ex02_07_average__not_valid():
    """Used for unit test of function ex02_07_average.

    Check that sending in different argument than
    int or float to any parameter for what to find returns None.
    """
    use_str_not_int_07 = '42'
    use_tuple_not_int_07 = (42, 42)
    use_list_not_int_07 = [42]
    check_list_of_wrong_07 = [use_str_not_int_07,
                              use_tuple_not_int_07,
                              use_list_not_int_07]
    correct_int = 42
    # Test with incorrect value for y
    for check_list_07 in check_list_of_wrong_07:
        assert ex02_07_average(correct_int, check_list_07) is None
    # Test with incorrect value for x
    for check_list_07 in check_list_of_wrong_07:
        assert ex02_07_average(check_list_07, correct_int) is None
    correct_float = 0.42
    # Test with incorrect value for y
    for check_list_07 in check_list_of_wrong_07:
        assert ex02_07_average(correct_float, check_list_07) is None
    # Test with incorrect value for x
    for check_list_07 in check_list_of_wrong_07:
        assert ex02_07_average(check_list_07, correct_float) is None
