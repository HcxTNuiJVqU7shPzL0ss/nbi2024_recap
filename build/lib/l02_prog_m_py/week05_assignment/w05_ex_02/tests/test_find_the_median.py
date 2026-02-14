"""Module for tests, L02, W05, Ex03.

Part 2.3 function test of "find_median_in_list".
This one here can be considered extensive and very
overworked, used for learning things.
"""

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


from ..src.find_the_median import find_median_in_list


###


### Special Exception Type: Incorrect ###
@pytest.mark.parametrize(
    'list_of_numbers',
    [
        273,
        42.42,
        '[3.14]',
        (23, 31),
        {'yes': 42},
        {14, 42, 41},
        range(42),
        b'12345',
        bytearray(b'123456'),
        None,
        True,
        False,
        lambda y: y,
        (i for i in range(3)),
        iter([1, 2, 3, 4]),
    ],
)

def test_find_median_in_list__wrong_types_raise_typeerror(list_of_numbers):
    """Use for TypeError raise testing.

    Tests (most of) req_001, including ac_001.
    Bullet 5 handled elsewhere, raising instead ValueError.
    However, instead of returning False, will raise TypeError.
    """
    with pytest.raises(TypeError):
        find_median_in_list(list_of_numbers)


###


### Special Exception Value: Empty list ###
@pytest.mark.parametrize(
    'list_of_numbers',
    [
        [],
        [    ],
    ],
)

def test_find_median_in_list__empty_list(list_of_numbers):
    """Use for ValueError raise testing, empty list.

    Tests:
    req_002, including ac_002
    However, instead of returning None, will raise ValueError.
    """
    with pytest.raises(ValueError):
        find_median_in_list(list_of_numbers)


###


### Special Exception Value: List too short ###
@pytest.mark.parametrize(
    'list_of_numbers',
    [
        [1],
        [  3  ],
    ],
)

def test_find_median_in_list__short_list(list_of_numbers):
    """Use for ValueError raise testing, list too short.

    Tests:
    req_003, including ac_003
    However, instead of returning None, will raise ValueError.
    """
    with pytest.raises(ValueError):
        find_median_in_list(list_of_numbers)


###


### Special Exception Value: List includes non numerical ###
@pytest.mark.parametrize(
    'list_of_numbers',
    [
        [1, 2, 3, 'a'],
        [1.1, 2.2, 3.3, 'b'],
        [(1.1, 2.2), 3.3],
    ],
)

def test_find_median_in_list__wrong_list(list_of_numbers):
    """Use for ValueError raise testing, list with non number.

    Tests part of (bullet 5):
    req_001 / ac_001
    Will raise TypeError (not return: None)
    """
    with pytest.raises(TypeError):
        find_median_in_list(list_of_numbers)


###


### Does not need to be sorted ###
@pytest.mark.parametrize(
    'list_of_numbers',
    [
        [6, 1, 2, 3, 5],
        [3, 1, 42],
        [-42, 42, 3],
        [3, 3, 2, 2, 42, 42],
        [3, 3],
        [1, 3, 3, 42],
        [-100, -42, 3, 3, -3, 42, 100, 666],
        [-666, -42, 3, -3, 42, 100, 666],
    ],
)

def test_find_median_in_list__not_sorted(list_of_numbers):
    """Use to test that not sorted does not matter.

    A list of numbers does not need to be sorted,
    will still work correctly.
    Tests:
    req_004 / ac_004
    req_005 / ac_005
    req_006 / ac_006
    req_007 / ac_007
    """
    assert find_median_in_list(list_of_numbers) == 3
