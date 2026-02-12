"""Module for tests, L02, W05, Ex1.5."""

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


import pytest


from ..ex01_5_find_2nd_max import (find_2nd_max)


def test_find_2nd_max__empty_list():
    """Used for unit test of function find_2nd_max.

    Check empty list.
    """
    expected = None
    actual = find_2nd_max([])
    assert actual[0] == expected


def test_find_2nd_max__one_element_list():
    """Used for unit test of function find_2nd_max.

    Check list with only one element.
    """
    expected = None
    actual = find_2nd_max([100])
    assert actual[0] == expected


def test_find_2nd_max__two_element_list_one_number():
    """Used for unit test of function find_2nd_max.

    Check list with two element, but they are identical.
    """
    identical_no = 100
    actual = find_2nd_max([identical_no, identical_no])
    assert actual[0] == identical_no


def test_find_2nd_max__share_first():
    """Used for unit test of function find_2nd_max.

    Check list with shared first place.
    """
    shared_first = 100
    lower_no = 99
    actual = find_2nd_max([lower_no, shared_first,
                           lower_no, shared_first])
    assert actual[0] == shared_first


def test_find_2nd_max__number_list_max():
    """Used for unit test of function find_2nd_max.

    Check numbered list for second to max value.
    """
    assert find_2nd_max([1, 2, 3, 4, 5, -17, 'er'])[0] == 4
    assert find_2nd_max([98.5, 1.5, 0, 'hi', 0.3])[0] == 1.5
    assert find_2nd_max([-30, '32', 15, -99])[0] == -30
    assert find_2nd_max([1, 2, 0.5])[0] == 1
    assert find_2nd_max([15, 5, 4, 2, 1])[0] == 5
    assert find_2nd_max([-1, 1, 'a', -34])[0] == -1
    assert find_2nd_max([1.2, 1.8, 0.8])[0] == 1.2
    assert find_2nd_max([5, 5, 5, 5, 9])[0] == 5
    assert find_2nd_max([105, 5, -5985, 500, 9])[0] == 105
    assert find_2nd_max([-999, 1.1])[0] == -999
    assert find_2nd_max([999, 999])[0] == 999
    assert find_2nd_max([999, 999, 5])[0] == 999

    assert find_2nd_max([4, 1, 2, 3])[0] == 3
    assert find_2nd_max([345, 3, 79])[0] == 79
    assert find_2nd_max([100, 4, 4, -12])[0] == 4
    assert find_2nd_max([-12, -13, -14])[0] == -13


def test_find_2nd_max__non_numbered_list():
    """Used for unit test of function find_2nd_max.

    Check list including only non numbers.
    """
    expected = None
    a = find_2nd_max([[], 'det', 'a'])
    b = find_2nd_max(['hello'])
    c = find_2nd_max([str(2), '234'])
    assert b[0] == c[0]
    assert a[0] == expected


### Special Exception ###
@pytest.mark.parametrize(
    'list_in_2nd',
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

def test_2nd_find_max__unsupported_types_raise_typeerror(list_in_2nd):
    """Use for raise testing when incorrect type."""
    with pytest.raises(TypeError):
        find_2nd_max(list_in_2nd)
