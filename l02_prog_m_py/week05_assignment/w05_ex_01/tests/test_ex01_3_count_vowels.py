"""Module for tests, L02, W05, Ex01.3."""

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


from ..ex01_3_count_vowels import (count_vowels)


def test_count_vowels__empty_word():
    """Used for unit test of function count_vowels.

    Check empty word.
    """
    expected = None
    actual = count_vowels('')
    assert actual == expected


def test_count_vowels__no_vowels():
    """Used for unit test of function count_vowels.

    Check when no vowels are used.
    """
    # No, one test case is not enough
    assert count_vowels('qwrt') == 0
    assert count_vowels('Tt') == 0
    assert count_vowels('123 123') == 0
    assert count_vowels(' ') == 0
    assert count_vowels('åäö') == 0


def test_count_vowels__with_vowels():
    """Used for unit test of function count_vowels.

    Check word(s) that has vowels.
    """
    assert count_vowels('ales') == 2
    assert count_vowels('WWWRRRRRFFFFFFFFadddddwww') == 1
    assert count_vowels('AEIOUY') == 6

    assert count_vowels("aArreE") == 4
    assert count_vowels("PPllOouui") == 5


def test_count_vowels__non_string():
    """Used for unit test of function count_vowels.

    Check incorrect strings.
    """
    expected = 'incorrect'
    a = count_vowels([1, 2, 3, 'a'])
    b = count_vowels(['hello'])
    c = count_vowels([True, False, None])
    assert b == c
    assert a == expected
