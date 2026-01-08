"""Module for tests, L02, W05, Ex01.2."""

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


from ..ex01_2_sum_list import (sum_list)


def test_empty_list():
    """Used for unit test of function sum_list.

    Check empty list.
    """
    expected = None
    actual = sum_list([])
    assert actual == expected


def test_number_list():
    """Used for unit test of function sum_list.

    Check numbered list.
    """
    assert sum_list([5]) == 5 # 5
    assert sum_list([1, 2, 3, 4, 5]) # 15
    assert sum_list([98.5, 1.5]) # 100
    assert sum_list([-30, 15]) # -15


def test_non_numbered_list():
    """Used for unit test of function sum_list.

    Check list including non numbers.
    """
    expected = 'incorrect'
    a = sum_list([1, 2, 3, 'a'])
    b = sum_list(['hello'])
    c = sum_list([True, False, None])
    assert b == c
    assert a == expected
