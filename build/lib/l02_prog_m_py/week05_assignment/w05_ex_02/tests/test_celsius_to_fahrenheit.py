"""Module for tests, L02, W05, Ex02.

Part 2.1 function test.
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


from ..src.celsius_to_fahrenheit import celsius_to_fahrenheit


###


### Special Exception Type ###
# Note: Bool is troublesome, since isinstance will not
# catch it, it is a subclass of int
@pytest.mark.parametrize(
    'c_degree_input',
    [
        '273',
        [3.14],
        (23, 31),
        {'yes': 42},
        {14, 42, 41},
        range(42),
        b'bcdef',
        bytearray(b'bcdef'),
        None,
        True,
        False,
        lambda y: y,
        (i for i in range(3)),
        iter([1, 2, 3, 4]),
    ],
)

def test_celsius_to_fahrenheit__unsupported_types_raise_typeerror(c_degree_input):
    """Use for TypeError raise testing."""
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(c_degree_input)


###


### Special Exception Value: low ###
@pytest.mark.parametrize(
    'c_degree_input',
    [
        -273.16,
        -300,
        -420,
    ],
)

def test_celsius_to_fahrenheit__temp_too_low(c_degree_input):
    """Use for ValueError raise testing, temp too low."""
    with pytest.raises(ValueError):
        celsius_to_fahrenheit(c_degree_input)


###


### Special Exception Value: high ###
@pytest.mark.parametrize(
    'c_degree_input',
    [
        1.5e32,
        1.42 * 10**32,
    ],
)

def test_celsius_to_fahrenheit__temp_too_high(c_degree_input):
    """Use for ValueError raise testing, temp too high."""
    with pytest.raises(ValueError):
        celsius_to_fahrenheit(c_degree_input)


###


def test_celsius_to_fahrenheit__check_low_temps():
    """Used for unit test of function celsius_to_fahrenheit.

    Check conversion at absolute zero or higher, using
    negative values, or 0.
    """
    assert round(celsius_to_fahrenheit(-273.15), 2) == -459.67
    assert celsius_to_fahrenheit(-50) == -58
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(-30) == -22
    assert celsius_to_fahrenheit(-20) == -4
    assert celsius_to_fahrenheit(-15) == 5
    assert celsius_to_fahrenheit(-10) == 14
    assert celsius_to_fahrenheit(-5) == 23
    assert celsius_to_fahrenheit(0) == 32


def test_celsius_to_fahrenheit__check_high_temps():
    """Used for unit test of function celsius_to_fahrenheit.

    Check conversion at higher than 0.
    """
    assert celsius_to_fahrenheit(5) == 41
    assert celsius_to_fahrenheit(10) == 50
    assert celsius_to_fahrenheit(15) == 59
    assert celsius_to_fahrenheit(20) == 68
    assert celsius_to_fahrenheit(25) == 77
    assert celsius_to_fahrenheit(35) == 95
    assert celsius_to_fahrenheit(37) == 98.6
    assert celsius_to_fahrenheit(40) == 104
    assert celsius_to_fahrenheit(100) == 212
