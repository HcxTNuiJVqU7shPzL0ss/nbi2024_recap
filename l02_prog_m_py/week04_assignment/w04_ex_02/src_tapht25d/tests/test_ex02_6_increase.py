"""Module for tests, L02, W04, Ex06."""

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
from ..ex02_functions import (ex02_06_increase)
# pylint: enable=import-error


def test_ex02_06_increase__correct_return():
    """Used for unit test of function ex02_06_increase.

    Check for correct return value.
    """
    # Test with pos int
    use_as_start_int = 1
    expected_int = 2
    assert ex02_06_increase(use_as_start_int) == expected_int
    # Test with neg int
    use_as_neg_int = -42
    expected_neg_int = -41
    assert ex02_06_increase(use_as_neg_int) == expected_neg_int
    # Test with pos float
    use_as_start_float = 42.1
    expected_float = 43.1
    assert ex02_06_increase(use_as_start_float) == expected_float
    # Test with neg float
    use_as_neg_float = -42.42
    expected_neg_float = -41.42
    assert ex02_06_increase(use_as_neg_float) == expected_neg_float


def test_ex02_06_increase__not_valid():
    """Used for unit test of function ex02_06_increase.

    Check that sending in different argument than
    int or float to parameter for what to find returns None.
    """
    use_str_not_int_06 = '42'
    use_tuple_not_int_06 = (42, 42)
    use_list_not_int_06 = [42]
    check_list_of_wrong_06 = [use_str_not_int_06,
                              use_tuple_not_int_06,
                              use_list_not_int_06]
    for check_list_06 in check_list_of_wrong_06:
        assert ex02_06_increase(check_list_06) is None
