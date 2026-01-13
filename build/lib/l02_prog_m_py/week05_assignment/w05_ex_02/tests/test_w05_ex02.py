"""Module for tests, L02, W05, Ex02."""

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


from ..src.w05_ex02_functions import c_to_f, count_words, find_median


def test_c_to_f__too_cold():
    """Used for unit test of function c_to_f.

    Check if below absolute zero, result shall be None.
    """

    expected = None
    actual = c_to_f(-300)
    assert actual == expected
    actual = c_to_f(-273.16)
    assert actual == expected


def test_c_to_f__check_temps():
    """Used for unit test of function c_to_f.

    Check if at absolute zero or higher.
    """

    assert round(c_to_f(-273.15), 2) == -459.67
    assert c_to_f(0) == 32
    assert c_to_f(-40) == -40
    assert c_to_f(1000) == 1832


def test_count_words__non_string():
    """Used for unit test of function count_words.

    Check if non strings used as input returns False.
    For ac_001.
    """
    expected = False

    a_int_check = 2
    b_float_check = 2.42
    c_list_check = ['one', 'two', 'with space']

    a = count_words(a_int_check)
    b = count_words(b_float_check)
    c = count_words(c_list_check)

    assert a == b
    assert b == c
    assert a == expected


def test_count_words__empty_string():
    """Used for unit test of function count_words.

    Check if empty string used as input returns None.
    For ac_002.
    """
    expected = None

    a_empty_check = ''
    a = count_words(a_empty_check)

    assert a == expected


def test_count_words__string_one_word():
    """Used for unit test of function count_words.

    Check if a single word string used as input returns 1.
    For ac_003, part 1.
    """
    expected = 1

    a_one_word_check = 'one'
    a = count_words(a_one_word_check)

    assert a == expected


def test_count_words__string_several_words():
    """Used for unit test of function count_words.

    Check if a several word string, separated by spaces, used as
    input returns the correct number of words.
    For ac_003, part 2.
    """
    expected = 4

    a_four_word_check = 'one two three four'
    a = count_words(a_four_word_check)

    assert a == expected


def test_count_words__words_with_consecutive_spaces():
    """Used for unit test of function count_words.

    Check if a several word string, separated by spaces, but with
    consecutive spaces, used as input returns the correct number
    of words, i.e. consecutive spaces only counted once.
    For ac_003, part 3.
    """
    expected = 6

    a_consecutive_spaces_check = 'one two  three   four    five     six'
    a = count_words(a_consecutive_spaces_check)

    assert a == expected


def test_count_words__words_with_leading_space():
    """Used for unit test of function count_words.

    Check that a string, with leading space(s), used as input
    returns the correct number of words, i.e. any leading space(s)
    not counted.
    For ac_004, part 1.
    """

    # Checks one leading space
    expected_lead1 = 4
    a_leading_space_check = ' one two  three   four'
    a = count_words(a_leading_space_check)
    assert a == expected_lead1

    # Checks two leading spaces
    expected_lead2 = 3
    b_leading_space_check = '  one two  three'
    b = count_words(b_leading_space_check)
    assert b == expected_lead2


def test_count_words__only_leading_space():
    """Used for unit test of function count_words.

    Check that a string, with only leading space(s), though no
    words, used as input returns None.
    For ac_004, part 2.
    """

    # Checks one leading space
    expected_lead1 = None
    a_leading_space_check = ' '
    a = count_words(a_leading_space_check)
    assert a == expected_lead1

    # Checks two leading spaces
    expected_lead2 = None
    b_leading_space_check = '  '
    b = count_words(b_leading_space_check)
    assert b == expected_lead2


def test_count_words__words_with_trailing_space():
    """Used for unit test of function count_words.

    Check that a string, with trailing space(s), used as input
    returns the correct number of words, i.e. any trailing space(s)
    not counted.
    For ac_005.
    """

    # Checks one trailing space
    expected_trail1 = 4
    a_trailing_space_check =' one two  three   four '
    a = count_words(a_trailing_space_check)
    assert a == expected_trail1

    # Checks two trailing spaces
    expected_trail2 = 3
    b_trailing_space_check = 'one two  three  '
    b = count_words(b_trailing_space_check)
    assert b == expected_trail2


def test_find_median__not_list():
    """Used for unit test of function find_median.

    Check that non list used as input returns False.
    For ac_001, parts 1 through 4.
    """

    expected = False

    a_int = find_median(42)
    b_float = find_median(3.14)
    c_str = find_median('42')
    d_tuple = find_median((1, 2))

    assert a_int == b_float
    assert c_str == d_tuple
    assert a_int == d_tuple

    assert b_float == expected


def test_find_median__list_with_non_numeral():
    """Used for unit test of function find_median.

    Check that list including non numerals used as input returns
    False.
    For ac_001, part 5.
    """

    expected = False

    non_numeral_list = ['a', 'b']
    some_numeral_list = [1, 2, 3, 'a', 42]

    check_non = find_median(non_numeral_list)
    check_some = find_median(some_numeral_list)

    assert check_non == check_some

    assert check_some == expected


def test_find_median__empty_list():
    """Used for unit test of function find_median.

    Check if empty list used as input returns None.
    For ac_002.
    """
    expected = None

    a_empty_check = []
    a = find_median(a_empty_check)

    assert a == expected


def test_find_median__short_list():
    """Used for unit test of function find_median.

    Check if too short list used as input returns None.
    For ac_003.
    """
    expected = None

    a_short_check = [42]
    a = find_median(a_short_check)

    assert a == expected


def test_find_median__even_list():
    """Used for unit test of function find_median.

    Check list with even number of elements (more than two).
    Return the median as the two middle values added,
    then div by 2.
    For ac_004 and ac_005.
    """
    # 2 values --> (1 + 41) / 2
    assert find_median([41, 1]) == 21
    # 4 values --> (25 + 25) / 2
    assert find_median([100, 25, 25, 10]) == 25
    # 8 values --> (25 + 75) / 2
    assert find_median([900, 800, 700, 75, 1, 2, 3, 25]) == 50


def test_find_median__odd_list():
    """Used for unit test of function find_median.

    Check list with odd number of elements (more than two).
    Return the median as the middle index value.
    For ac_004 and ac_006.
    """
    # 3 values
    assert find_median([3, 41, 1]) == 3
    # 5 values
    assert find_median([100, 75, 25, 10, 50]) == 50
    # 7 values
    assert find_median([800, 700, 75, 1, 2, 3, 25]) == 25


def test_find_median__different_types():
    """Used for unit test of function find_median.

    Check list including different support types, e.g.,
    int, float, positive numbers, negative numbers.
    For ac_007.
    """
    assert find_median([42, 3.14, -100]) == 3.14
