"""Module for tests, L02, W05, Ex01.4."""

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


from ..ex01_4_find_max import (find_max)


def test_find_max__empty_list():
    """Used for unit test of function find_max.

    Check empty list.
    """
    expected = None
    actual = find_max([])
    assert actual == expected


def test_find_max__number_list_max():
    """Used for unit test of function find_max.

    Check numbered list for max value.
    """
    assert find_max([5]) == 5
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([98.5, 1.5]) == 98.5
    assert find_max([-30, '32', 15]) == 15

    assert find_max([1, 2]) == 2
    assert find_max([15, 5]) == 15
    assert find_max([-1, 1, 'a']) == 1
    assert find_max([1.2, 1.8]) == 1.8

    assert find_max([5, 5, 5, 5, 9]) == 9
    assert find_max([105, 5, -5985, 500, 9]) == 500
    assert find_max([-999, 1.1]) == 1.1


def test_find_max__non_numbered_list():
    """Used for unit test of function find_max.

    Check list including only non numbers.
    """
    expected = 'incorrect'
    a = find_max([[], 'det', 'a'])
    b = find_max(['hello'])
    c = find_max([str(2), '234'])
    assert b == c
    assert a == expected
