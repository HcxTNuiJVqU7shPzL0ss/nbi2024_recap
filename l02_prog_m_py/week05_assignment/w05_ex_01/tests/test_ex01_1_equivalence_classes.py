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


#from l02_prog_m_py.week05_assignment.w05_ex_01.ex01_1_equivalence_classes import w05_ex01_1a

from ..ex01_1_equivalence_classes import (w05_ex01_1a, w05_ex01_1b,
                                          w05_ex01_1c, w05_ex01_1d,
                                          w05_ex01_1e)


def test_w05_ex01_1a__true():
    """Used for unit test of function w05_ex01_1a, check True."""

    # Version 1
    expected = True
    actual = w05_ex01_1a(101, True)
    assert actual == expected
    actual = w05_ex01_1a(1010, True)
    assert actual == expected

    # Version 2
    assert w05_ex01_1a(101, True) == True
    assert w05_ex01_1a(1010, True) == True

    # Version 3
    a = w05_ex01_1a(101, True)
    b = w05_ex01_1a(1010, True)
    c = a and b
    assert c == expected


def test_w05_ex01_1a__false():
    """Used for unit test of function w05_ex01_1a, check False."""

    # Version 1
    expected = False
    actual = w05_ex01_1a(100, True)
    assert actual == expected
    actual = w05_ex01_1a(-1, True)
    assert actual == expected

    # Version 2
    assert w05_ex01_1a(100, True) == False
    assert w05_ex01_1a(-1, True) == False

    # Version 3
    a = w05_ex01_1a(100, True)
    b = w05_ex01_1a(-1, True)
    c = a or b
    assert c == expected


def test_w05_ex01_1b__true():
    """Used for unit test of function w05_ex01_1b, check True."""

    # Version 1
    expected = True
    actual = w05_ex01_1b(42, True)
    assert actual == expected
    actual = w05_ex01_1b(42.0, True)
    assert actual == expected

    # Version 2
    assert w05_ex01_1b(42, True) == True
    assert w05_ex01_1b(42.0, True) == True

    # Version 3
    a = w05_ex01_1b(42, True)
    b = w05_ex01_1b(42.0, True)
    c = a and b
    assert c == expected


def test_w05_ex01_1b__false():
    """Used for unit test of function w05_ex01_1b, check False."""

    # Version 1
    expected = False
    actual = w05_ex01_1b(41, True)
    assert actual == expected
    actual = w05_ex01_1b(43, True)
    assert actual == expected
    actual = w05_ex01_1b(42.001, True)
    assert actual == expected

    # Version 2
    assert w05_ex01_1b(41, True) == False
    assert w05_ex01_1b(43, True) == False
    assert w05_ex01_1b(42.001, True) == False

    # Version 3
    a = w05_ex01_1b(41, True)
    b = w05_ex01_1b(43, True)
    c = w05_ex01_1b(42.001, True)
    d = a or b or c
    assert d == expected


def test_w05_ex01_1c__true():
    """Used for unit test of function w05_ex01_1c, check True."""
    expected = True
    actual = w05_ex01_1c('12345', True)
    assert actual == expected
    actual = w05_ex01_1c('abcdef', True)
    assert actual == expected


def test_w05_ex01_1c__false():
    """Used for unit test of function w05_ex01_1c, check False."""
    expected = False
    actual = w05_ex01_1c(str(41), True)
    assert actual == expected
    actual = w05_ex01_1c('1234', True)
    assert actual == expected
    actual = w05_ex01_1c(['1', 2], True)
    assert actual == expected


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


def test_w05_ex01_1e__true():
    """Used for unit test of function w05_ex01_1e, check True."""

    a = w05_ex01_1e(9, True)
    b = w05_ex01_1e(15, True)
    c = a and b
    assert c == True


def test_w05_ex01_1e__false():
    """Used for unit test of function w05_ex01_1e, check False."""

    x = w05_ex01_1e(8, True)
    y = w05_ex01_1e(16, True)
    z = x or y
    assert z == False
