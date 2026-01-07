"""Module for tests, L02, W05, Ex01."""


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
                                          w05_ex01_1c)


def test_w05_ex01_1a__true():
    """Used for unit test of function w05_ex01_1a, check True."""
    expected = True
    actual = w05_ex01_1a(101, True)
    assert actual == expected
    actual = w05_ex01_1a(1010, True)
    assert actual == expected


def test_w05_ex01_1a__false():
    """Used for unit test of function w05_ex01_1a, check False."""
    expected = False
    actual = w05_ex01_1a(100, True)
    assert actual == expected
    actual = w05_ex01_1a(-1, True)
    assert actual == expected


def test_w05_ex01_1b__true():
    """Used for unit test of function w05_ex01_1b, check True."""
    expected = True
    actual = w05_ex01_1b(42, True)
    assert actual == expected
    actual = w05_ex01_1b(42.0, True)
    assert actual == expected


def test_w05_ex01_1b__false():
    """Used for unit test of function w05_ex01_1b, check False."""
    expected = False
    actual = w05_ex01_1b(41, True)
    assert actual == expected
    actual = w05_ex01_1b(43, True)
    assert actual == expected
    actual = w05_ex01_1b(42.001, True)
    assert actual == expected


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
