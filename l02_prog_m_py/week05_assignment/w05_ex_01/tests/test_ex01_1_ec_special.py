"""Module for tests, L02, W05, Ex01.1.

Use more special handling of the tests, other than
doing each one separate.
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


from ..ex01_1_equivalence_classes import (w05_ex01_1a, w05_ex01_1b,
                                          w05_ex01_1c, w05_ex01_1d,
                                          w05_ex01_1e, w05_ex01_1f,
                                          w05_ex01_1g)


# Three times below use a pytest decorator
# Tells pytest to run the same test function multiple times with
# different input values.
# Takes two things, a string naming one or more argument names,
# and a list of values to be passed into the test

# @pytest.mark ==
# A namespace that contains pytest’s built‑in markers.

# .parametrize ==
# A specific marker that expands a single test into many tests.

# 'value' (first argument, e.g., 'x' or 'y') ==
# The name of the parameter that will be injected into the test function.

# [ ... ] (second argument) ==
# The list of values pytest will feed into the test.


############################## 1a ###################################

### Special Exception ###
# Note: Bool is troublesome, since isinstance will not
# catch it, it is a subclass of int
@pytest.mark.parametrize(
    'x',
    [
        '10',
        [3.14],
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

def test_w05_ex01_1a__unsupported_types_raise_typeerror(x):
    """Use for different kind of raise testing."""
    with pytest.raises(TypeError):
        w05_ex01_1a(x, True)


### Special True ###
@pytest.mark.parametrize(
    'x',
    [
        100.001,
        101,
        4242,
        424242.42,
    ],
)

def test_w05_ex01_1a__supported_types_int_float_ok(x):
    """Use for different kind of True check."""
    assert w05_ex01_1a(x, True) is True


### Special False ###
@pytest.mark.parametrize(
    'x',
    [
        99.999,
        100,
        42.42,
        -101,
    ],
)

def test_w05_ex01_1a__supported_types_int_float_nok(x):
    """Use for different kind of False check."""
    assert w05_ex01_1a(x, True) is False

############################## 1b ###################################

### Special Exception ###
# Note: Bool is troublesome, since isinstance will not
# catch it, it is a subclass of int
@pytest.mark.parametrize(
    'y',
    [
        '10', # str - String (text)
        [3.14], # list - List containing a float
        (2, 3), # tuple - Tuple of integers
        {'no': 1}, # dict - Dictionary (mapping)
        {42, 41}, # set - Set (unordered, unique elements)
        range(1), # range - Range object (iterable)
        b'abcde', # bytes - Immutable byte sequence
        bytearray(b'abcde'), # bytearray - Mutable byte sequence
        None, # NoneType - The singleton None
        True, # bool - Boolean (subclass of int)
        False, # bool - Boolean (subclass of int)
        lambda x: x, # function - Function object
        (i for i in range(5)), # generator - Generator object
        iter([1, 2, 3]), # list_iterator - Iterator created from a list
    ],
)

def test_w05_ex01_1b__unsupported_types_raise_typeerror(y):
    """Use for different kind of raise testing."""
    with pytest.raises(TypeError):
        w05_ex01_1b(y, True)


### Special True ###
@pytest.mark.parametrize(
    'y',
    [
        42,
        42.0,
        42.000,
    ],
)

def test_w05_ex01_1b__supported_types_int_float_ok(y):
    """Use for different kind of True check."""
    assert w05_ex01_1b(y, True) is True


### Special False ###
@pytest.mark.parametrize(
    'y',
    [
        99.999,
        41.99,
        42.01,
        -101,
        -42,
        -42.0,
    ],
)

def test_w05_ex01_1b__supported_types_int_float_nok(y):
    """Use for different kind of False check."""
    assert w05_ex01_1b(y, True) is False

############################## 1c ###################################

### Special Exception ###
@pytest.mark.parametrize(
    'text',
    [
        10,
        3.14,
        True,
        False,
        None,
        lambda x: x,
        (i for i in range(5)),
        iter([1, 2, 3]),
    ],
)

def test_w05_ex01_1c__unsupported_types_raise_typeerror(text):
    """Use for different kind of raise testing."""
    with pytest.raises(TypeError):
        w05_ex01_1c(text, True)


### Special True ###
@pytest.mark.parametrize(
    'text',
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

def test_w05_ex01_1c__supported_types_len_at_least_five(text):
    """Use for different kind of True check."""
    assert w05_ex01_1c(text, True) is True


### Special False ###
@pytest.mark.parametrize(
    'text',
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

def test_w05_ex01_1c__supported_types_len_too_short(text):
    """Use for different kind of False check."""
    assert w05_ex01_1c(text, True) is False

############################## 1d ###################################

### Special Exception ###
@pytest.mark.parametrize(
    'z',
    [
        42,
        42.42,
        '10',
        [3.14],
        (2, 3),
        {'no': 1},
        {42, 41},
        range(1),
        b'abcde',
        bytearray(b'abcde'),
        None,
        lambda x: x,
        (i for i in range(5)),
        iter([1, 2, 3]),
    ],
)

def test_w05_ex01_1d__unsupported_types_raise_typeerror(z):
    """Use for different kind of raise testing."""
    with pytest.raises(TypeError):
        w05_ex01_1d(z, True)


### Special True ###
@pytest.mark.parametrize(
    'z',
    [
        True,
    ],
)

def test_w05_ex01_1d__supported_types_len_at_least_five(z):
    """Use for different kind of True check."""
    assert w05_ex01_1d(z, True) is True


### Special False ###
@pytest.mark.parametrize(
    'z',
    [
        False,
    ],
)

def test_w05_ex01_1d__supported_types_len_too_short(z):
    """Use for different kind of False check."""
    assert w05_ex01_1d(z, True) is False


### Additional silly stuff, printout, mocking, etc. ###

def test_w05_ex01_1d__normal_run_does_not_block(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "")
    assert w05_ex01_1d(True, False) is True

@pytest.mark.parametrize('z', [True, False])
def test_w05_ex01_1d__normal_run(monkeypatch, z):
    monkeypatch.setattr('builtins.input', lambda _: "")
    assert w05_ex01_1d(z, False) is z

def test_w05_ex01_1d__normal_run_prints(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "")
    w05_ex01_1d(True, False)
    captured = capsys.readouterr()
    assert "This is part" in captured.out

############################## 1e ###################################

############################## 1f ###################################

############################## 1g ###################################
