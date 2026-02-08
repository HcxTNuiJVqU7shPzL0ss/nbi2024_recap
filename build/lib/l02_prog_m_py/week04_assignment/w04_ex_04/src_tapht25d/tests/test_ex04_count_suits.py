"""Module for tests, L02, W04, Ex04.

Handle unit test of function: check_same_suit
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


# pylint: disable=import-error
from ..ex04_functions import check_same_suit
# pylint: enable=import-error


def test_check_same_suit__correct_five():
    """Use for unit test of function check_same_suit.

    Checks that the returned list of suits is correct, when
    having 5 of the same suits.
    """
    check_five_same = [['spades', 2], ['spades', 3], ['spades', 4],
                       ['spades', 5], ['spades', 6]]
    list_of_same = check_same_suit(check_five_same)
    assert isinstance(check_five_same, list)
    assert isinstance(list_of_same, list)
    assert len(list_of_same) == 4
    assert list_of_same.count(5) == 1
    assert list_of_same.count(0) == 3
    assert list_of_same[0] == 5
    for i, found in enumerate(list_of_same):
        if i == 0:
            assert found == 5
        else:
            assert found == 0


def test_check_same_suit__correct_four():
    """Use for unit test of function check_same_suit.

    Checks that the returned list of suits is correct, when
    having 4 of the same suits.
    """
    check_four_same = [['spades', 2], ['spades', 4], ['spades', 6],
                       ['spades', 8], ['clubs', 10]]
    list_of_same = check_same_suit(check_four_same)
    assert isinstance(check_four_same, list)
    assert isinstance(list_of_same, list)
    assert len(list_of_same) == 4
    assert list_of_same.count(4) == 1
    assert list_of_same.count(1) == 1
    assert list_of_same.count(0) == 2
    assert list_of_same[0] == 4
    assert list_of_same[1] == 1
    for i, found in enumerate(list_of_same):
        if i == 0:
            assert found == 4
        elif i == 1:
            assert found == 1
        else:
            assert found == 0


def test_check_same_suit__correct_three():
    """Use for unit test of function check_same_suit.

    Checks that the returned list of suits is correct, when
    having 3 of the same suits.
    """
    check_three_same = [['spades', 3], ['spades', 4], ['spades', 4],
                        ['clubs', 4], ['hearts', 2]]
    list_of_same = check_same_suit(check_three_same)
    assert isinstance(check_three_same, list)
    assert isinstance(list_of_same, list)
    assert len(list_of_same) == 4
    assert list_of_same.count(3) == 1
    assert list_of_same.count(1) == 2
    assert list_of_same.count(0) == 1
    assert list_of_same[0] == 3
    assert list_of_same[1] == 1
    assert list_of_same[2] == 1
    for i, found in enumerate(list_of_same):
        if i == 0:
            assert found == 3
        elif i == 1:
            assert found == 1
        elif i == 2:
            assert found == 1
        else:
            assert found == 0


def test_check_same_suit__correct_two():
    """Use for unit test of function check_same_suit.

    Checks that the returned list of suits is correct, when
    having 2 of the same suits.
    """
    check_two_same = [['spades', 3], ['spades', 4], ['clubs', 4],
                      ['hearts', 7], ['diamonds', 5]]
    list_of_same = check_same_suit(check_two_same)
    assert isinstance(check_two_same, list)
    assert isinstance(list_of_same, list)
    assert len(list_of_same) == 4
    assert list_of_same.count(2) == 1
    assert list_of_same.count(1) == 3
    assert list_of_same.count(0) == 0
    assert list_of_same[0] == 2
    assert list_of_same[1] == 1
    assert list_of_same[2] == 1
    for i, found in enumerate(list_of_same):
        if i == 0:
            assert found == 2
        elif i == 1:
            assert found == 1
        elif i == 2:
            assert found == 1
        elif i == 3:
            assert found == 1
        else:
            assert found == 0


def test_check_same_suit__correct_one():
    """Use for unit test of function check_same_suit.

    Checks that the returned list of ranks is correct, when
    having only 1 of the same suits (which normally can never
    happen, but it is possible to test it).
    """
    # Should be impossible to have only 1 of the same, though the
    # specific function does not know this
    # The 5th value is however not included in the function, so
    # becomes a bit special test handling.
    check_one_same = [['spades', 3], ['clubs', 4], ['hearts', 13],
                      ['diamonds', 11], ['dummy', 2]]
    list_of_same = check_same_suit(check_one_same)
    assert isinstance(check_one_same, list)
    assert isinstance(list_of_same, list)
    assert len(list_of_same) == 4
    assert list_of_same.count(1) == 4 # Can only be 4 in the function
    assert list_of_same[0] == 1
    assert list_of_same[1] == 1
    assert list_of_same[2] == 1
    assert list_of_same[3] == 1
    for i, found in enumerate(list_of_same):
        if i == 0:
            assert found == 1
        elif i == 1:
            assert found == 1
        elif i == 2:
            assert found == 1
        elif i == 3:
            assert found == 1
        elif i == 4:
            assert found == 1
        else:
            assert found == 0


def test_check_same_suit__not_list():
    """Used for unit test of function check_same_suit.

    Check that sending in different argument than
    list to parameter for what to find returns None.
    """
    use_int_not_list_suit = 3
    use_float_not_list_suit = 2.2
    use_str_not_list_suit = '4'
    use_tuple_not_list_suit = ('2', '4')
    check_list_of_wrong_suit = [use_int_not_list_suit,
                                use_float_not_list_suit,
                                use_str_not_list_suit,
                                use_tuple_not_list_suit]
    for check_list_suit in check_list_of_wrong_suit:
        assert check_same_suit(check_list_suit) is None
