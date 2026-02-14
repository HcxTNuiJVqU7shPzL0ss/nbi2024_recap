"""Module for tests, L02, W05, Ex1.2."""

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


import random

import pytest

from ..ex01_2_sum_list import (sum_list)


### Special Exception ###
@pytest.mark.parametrize(
    'list_in',
    [
        42,
        42.42,
        '10',
        (2, 3),
        {'no': 1},
        {42, 41},
        range(1),
        b'abcde',
        bytearray(b'abcde'),
        None,
        True,
        False,
        lambda x: x,
        (i for i in range(5)),
        iter([1, 2, 3]),
    ],
)

def test_sum_list__unsupported_types_raise_typeerror(list_in):
    """Use for raise testing when incorrect type."""
    with pytest.raises(TypeError):
        sum_list(list_in)


def test_sum_list__empty_list():
    """Used for unit test of function sum_list.

    Check empty list (returns None).
    """
    expected = None
    actual = sum_list([])
    assert actual == expected

    edit_list = [1, 2]
    edit_list.pop()
    edit_list.pop()
    assert sum_list(edit_list) == expected


def test_sum_list__number_list():
    """Used for unit test of function sum_list.

    Check numbered list.
    """
    assert sum_list([5]) == 5
    assert sum_list([1, 2, 3, 4, 5]) == 15
    assert sum_list([98.5, 1.5]) == 100
    assert sum_list([-30, 15]) == -15

    assert sum_list([1, 2]) == 3
    assert sum_list([15, 5]) == 20
    assert sum_list([-1, 1]) == 0
    assert sum_list([1.2, 1.8]) == 3

    use_list = list(range(-42, 150))
    tot_list = sum(use_list)
    assert sum_list(use_list) == tot_list

    values_no = 42
    value_list = random.sample(range(-999, 999), values_no)
    value_tot = sum(value_list)
    value_list.append('a')
    value_list.pop()
    assert sum_list(value_list) == value_tot


def test_sum_list__non_numbered_list():
    """Used for unit test of function sum_list.

    Check list including non numbers.
    """
    expected = 'incorrect'
    a = sum_list([1, 2, 3, 'a'])
    b = sum_list(['hello'])
    c = sum_list([True, False, None])
    assert b == c
    assert a == expected

    assert sum_list([True]) == expected

    values_no = 42
    value_list = random.sample(range(-999, 999), values_no)
    value_tot = sum(value_list)
    value_list.append('a')
    assert sum_list(value_list) != value_tot
    assert sum_list(value_list) == expected
