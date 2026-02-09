"""Module for tests, L02, W05, Ex01.1."""

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


from ..ex01_1_equivalence_classes import (w05_ex01_1a, w05_ex01_1b,
                                          w05_ex01_1c, w05_ex01_1d,
                                          w05_ex01_1e, w05_ex01_1f,
                                          w05_ex01_1g)

############################## 1a ###################################

def test_w05_ex01_1a__raise():
    """Use for unit test of function w05_ex01_1a.

    Check that using other than int or float raise an exception.
    """
    use_1a_str = '42'
    use_1a_list = [42]
    with pytest.raises(ValueError):
        w05_ex01_1a(use_1a_str, True)
    with pytest.raises(ValueError):
        w05_ex01_1a(use_1a_list, True)


def test_w05_ex01_1a__true():
    """Use for unit test of function w05_ex01_1a.

    Check True, with correct int or float used as parameter.
    """
    expected = True

    # Version 1
    actual = w05_ex01_1a(101, True)
    assert actual == expected
    actual = w05_ex01_1a(1010, True)
    assert actual == expected

    # Version 2
    assert w05_ex01_1a(101, True) is expected
    assert w05_ex01_1a(1010, True) is expected

    # Version 3
    a = w05_ex01_1a(101, True)
    b = w05_ex01_1a(1010, True)
    c = a and b
    assert c == expected

    # Also with float
    actual = w05_ex01_1a(100.0001, True)
    assert actual == expected


def test_w05_ex01_1a__false():
    """Used for unit test of function w05_ex01_1a.

    Check False, with correct int or float used as parameter.
    """
    expected = False

    # Version 1
    actual = w05_ex01_1a(100, True)
    assert actual == expected
    actual = w05_ex01_1a(-1, True)
    assert actual == expected

    # Version 2
    assert w05_ex01_1a(100, True) is expected
    assert w05_ex01_1a(-1, True) is expected

    # Version 3
    a = w05_ex01_1a(100, True)
    b = w05_ex01_1a(-1, True)
    c = a or b
    assert c == expected

    # Also with float
    actual = w05_ex01_1a(99.999, True)
    assert actual == expected

############################## 1b ###################################

def test_w05_ex01_1b__raise():
    """Use for unit test of function w05_ex01_1b.

    Check that using other than int or float raise an exception.
    """
    use_1b_str = '42'
    use_1b_list = [42]
    with pytest.raises(ValueError):
        w05_ex01_1b(use_1b_str, True)
    with pytest.raises(ValueError):
        w05_ex01_1b(use_1b_list, True)


def test_w05_ex01_1b__true():
    """Used for unit test of function w05_ex01_1b.

    Check True, with correct int or float used as parameter.
    """
    expected = True

    # Version 1
    actual = w05_ex01_1b(42, True)
    assert actual == expected
    actual = w05_ex01_1b(42.0, True)
    assert actual == expected

    # Version 2
    assert w05_ex01_1b(42, True) is expected
    assert w05_ex01_1b(42.0, True) is expected

    # Version 3
    a = w05_ex01_1b(42, True)
    b = w05_ex01_1b(42.0, True)
    c = a and b
    assert c == expected


def test_w05_ex01_1b__false():
    """Used for unit test of function w05_ex01_1b.

    Check False, with correct int or float used as parameter.
    """
    expected = False

    # Version 1
    actual = w05_ex01_1b(41, True)
    assert actual == expected
    actual = w05_ex01_1b(43, True)
    assert actual == expected
    actual = w05_ex01_1b(42.001, True)
    assert actual == expected

    # Version 2
    assert w05_ex01_1b(41, True) is expected
    assert w05_ex01_1b(43, True) is expected
    assert w05_ex01_1b(42.001, True) is expected

    # Version 3
    a = w05_ex01_1b(41, True)
    b = w05_ex01_1b(43, True)
    c = w05_ex01_1b(42.001, True)
    d = a or b or c
    assert d == expected

############################## 1c ###################################

def test_w05_ex01_1c__raise():
    """Use for unit test of function w05_ex01_1c.

    Check that using type which does not support len raise an
    exception.
    E.g., int, float, bool, etc.
    """
    use_1c_int = 42
    use_1c_float = 42.2
    use_1c_bool = True
    use_1c_complex = 1001+2j
    use_1c_none = None
    with pytest.raises(TypeError):
        w05_ex01_1c(use_1c_int, True)
    with pytest.raises(TypeError):
        w05_ex01_1c(use_1c_float, True)
    with pytest.raises(TypeError):
        w05_ex01_1c(use_1c_bool, True)
    with pytest.raises(TypeError):
        w05_ex01_1c(use_1c_complex, True)
    with pytest.raises(TypeError):
        w05_ex01_1c(use_1c_none, True)


def test_w05_ex01_1c__true():
    """Used for unit test of function w05_ex01_1c.

    Check True, with correct type (supporting len)
    used as parameter.
    """
    expected = True

    # String
    actual = w05_ex01_1c('12345', True)
    assert actual == expected
    actual = w05_ex01_1c('abcdef', True)
    assert actual == expected

    # List
    actual = w05_ex01_1c([1, 2, 3, 4, 5, 6, 7, 8, 42], True)
    assert actual == expected

    # Tuple
    actual = w05_ex01_1c((10, 20, 30, 40, 50), True)
    assert actual == expected

    # Dictionary
    actual = w05_ex01_1c({'a': 10, 'b': 20, 'c': 30,
                          'd': 40, 'e': 50}, True)
    assert actual == expected

    # Set
    actual = w05_ex01_1c({10, 20, 30, 40, 50}, True)
    assert actual == expected

    # Range
    actual = w05_ex01_1c(range(5), True)
    assert actual == expected


def test_w05_ex01_1c__false():
    """Used for unit test of function w05_ex01_1c.

    Check False, with correct type (supporting len)
    used as parameter.
    """
    expected = False

    actual = w05_ex01_1c(str(41), True)
    assert actual == expected
    actual = w05_ex01_1c('1234', True)
    assert actual == expected
    actual = w05_ex01_1c(['1', 2], True)
    assert actual == expected
    actual = w05_ex01_1c(('1', 2, 'a', 5), True)
    assert actual == expected
    actual = w05_ex01_1c({'b': 20, 'c': 30,
                          'd': 40, 'e': 50}, True)
    assert actual == expected
    actual = w05_ex01_1c({10, 20, 30, 40}, True)
    assert actual == expected
    actual = w05_ex01_1c(range(4), True)
    assert actual == expected

    # Also check empty / len 0
    actual = w05_ex01_1c(str(), True)
    assert actual == expected
    actual = w05_ex01_1c('', True)
    assert actual == expected
    actual = w05_ex01_1c([], True)
    assert actual == expected
    actual = w05_ex01_1c((), True)
    assert actual == expected
    actual = w05_ex01_1c({}, True)
    assert actual == expected
    actual = w05_ex01_1c({}, True)
    assert actual == expected
    actual = w05_ex01_1c(range(0), True)
    assert actual == expected


# Three times below use a pytest decorator
# Tells pytest to run the same test function multiple times with
# different input values.
# Takes two things, a string naming one or more argument names,
# and a list of values to be passed into the test

# @pytest.mark ==
# A namespace that contains pytest’s built‑in markers.

# .parametrize ==
# A specific marker that expands a single test into many tests.

# 'value' (first argument) ==
# The name of the parameter that will be injected into the test function.

# [ ... ] (second argument) ==
# The list of values pytest will feed into the test.


### Special Exception ###
@pytest.mark.parametrize(
    "value",
    [
        10,
        3.14,
        True,
        None,
        lambda x: x,
        (i for i in range(5)), # generator
        iter([1, 2, 3]), # iterator
    ],
)

def test_w05_ex01_1c__unsupported_types_raise_typeerror(value):
    """Use for different kind of raise testing."""
    with pytest.raises(TypeError):
        w05_ex01_1c(value, True)

### Special True ###
@pytest.mark.parametrize(
    "value",
    [
        'hello',
        [1, 2, 3, 4, 5],
        (1, 2, 3, 4, 5),
        {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
        {1, 2, 3, 4, 5},
        range(5),
        b'abcde',
        bytearray(b'abcde'),
    ],
)

def test_w05_ex01_1c__supported_types_len_at_least_five(value):
    """Use for different kind of True check."""
    assert w05_ex01_1c(value, True) is True

### Special False ###
@pytest.mark.parametrize(
    'value',
    [
        'hi',
        [1, 2],
        (1, 2, 3),
        {'a': 1},
        {1, 2, 3},
        range(3),
        b'abc',
    ],
)

def test_w05_ex01_1c__supported_types_len_too_short(value):
    """Use for different kind of False check."""
    assert w05_ex01_1c(value, True) is False

############################## 1d ###################################

def test_w05_ex01_1d__true():
    """Used for unit test of function w05_ex01_1d, check True."""
    expected = True
    actual = w05_ex01_1d(True, True)
    assert actual == expected


def test_w05_ex01_1d__false():
    """Used for unit test of function w05_ex01_1d, check False."""
    expected = False
    actual = w05_ex01_1d(41, True)
    assert actual == expected
    actual = w05_ex01_1d('1234', True)
    assert actual == expected
    actual = w05_ex01_1d(['1', 2], True)
    assert actual == expected
    actual = w05_ex01_1d(False, True)
    assert actual == expected

############################## 1e ###################################

def test_w05_ex01_1e__true():
    """Used for unit test of function w05_ex01_1e, check True."""

    a = w05_ex01_1e(9, True)
    b = w05_ex01_1e(15, True)
    c = a and b
    assert c is True


def test_w05_ex01_1e__false():
    """Used for unit test of function w05_ex01_1e, check False."""

    x = w05_ex01_1e(8, True)
    y = w05_ex01_1e(16, True)
    z = x or y
    assert z is False

############################## 1f ###################################

def test_w05_ex01_1f__true():
    """Used for unit test of function w05_ex01_1f, check True."""

    a = w05_ex01_1f(32, True)
    b = w05_ex01_1f(64, True)
    c = w05_ex01_1f(128, True)
    d = a and b and c
    assert d is True


def test_w05_ex01_1f__false():
    """Used for unit test of function w05_ex01_1f, check False."""

    m = w05_ex01_1f(8, True)
    n = w05_ex01_1f(42, True)
    o = w05_ex01_1f(100, True)
    p = w05_ex01_1f(129, True)
    z = m or n or o or p
    assert z is False

############################## 1g ###################################

def test_w05_ex01_1g__check_values():
    """Used for unit test of function w05_ex01_1g, check values."""

    expected_less5 = 'less_5'
    a = w05_ex01_1g(-100, True)
    assert a == expected_less5

    expected_less10_more5 = 'less10_more5'
    b = w05_ex01_1g(5, True)
    assert b == expected_less10_more5

    expected_less15_more10 = 'less15_more10'
    c = w05_ex01_1g(10, True)
    assert c == expected_less15_more10

    expected_more15 = 'more15'
    d = w05_ex01_1g(15, True)
    assert d == expected_more15
