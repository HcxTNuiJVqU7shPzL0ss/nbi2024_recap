"""Module for tests, L02, W04, Ex04.

Handle unit test of function: check_same_rank
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
from ..ex04_functions import check_same_rank
# pylint: enable=import-error


def test_check_same_rank__correct_five():
    """Use for unit test of function check_same_rank.

    Checks that the returned list of ranks is correct, when
    having 5 of the same rank (impossible normally, though
    can be tested for this function).
    """
    # Should be impossible to have 5 of the same, though the
    # specific function does not know this
    check_five_same = [['a', 2], ['b', 2], ['c', 2], ['d', 2],
                       ['e', 2]]
    list_of_same = check_same_rank(check_five_same)
    assert isinstance(check_five_same, list)
    assert isinstance(list_of_same, list)
    assert len(list_of_same) == 13
    assert list_of_same.count(5) == 1
    assert list_of_same.count(0) == 12
    assert list_of_same[0] == 5
    for i, occurrence in enumerate(list_of_same):
        if i + 2 == 2:
            assert occurrence == 5
        else:
            assert occurrence == 0


def test_check_same_rank__correct_four():
    """Use for unit test of function check_same_rank.

    Checks that the returned list of ranks is correct, when
    having 4 of the same rank.
    """
    check_four_same = [['a', 3], ['b', 3], ['c', 3], ['d', 3],
                       ['e', 2]]
    list_of_same = check_same_rank(check_four_same)
    assert isinstance(check_four_same, list)
    assert isinstance(list_of_same, list)
    assert len(list_of_same) == 13
    assert list_of_same.count(4) == 1
    assert list_of_same.count(1) == 1
    assert list_of_same.count(0) == 11
    assert list_of_same[0] == 1
    assert list_of_same[1] == 4
    for i, occurrence in enumerate(list_of_same):
        if i == 0:
            assert occurrence == 1
        elif i == 1:
            assert occurrence == 4
        else:
            assert occurrence == 0


def test_check_same_rank__correct_three():
    """Use for unit test of function check_same_rank.

    Checks that the returned list of ranks is correct, when
    having 3 of the same rank.
    """
    check_three_same = [['a', 3], ['b', 4], ['c', 4], ['d', 4],
                       ['e', 2]]
    list_of_same = check_same_rank(check_three_same)
    assert isinstance(check_three_same, list)
    assert isinstance(list_of_same, list)
    assert len(list_of_same) == 13
    assert list_of_same.count(3) == 1
    assert list_of_same.count(1) == 2
    assert list_of_same.count(0) == 10
    assert list_of_same[0] == 1
    assert list_of_same[1] == 1
    assert list_of_same[2] == 3
    for i, occurrence in enumerate(list_of_same):
        if i == 0:
            assert occurrence == 1
        elif i == 1:
            assert occurrence == 1
        elif i == 2:
            assert occurrence == 3
        else:
            assert occurrence == 0


def test_check_same_rank__correct_two():
    """Use for unit test of function check_same_rank.

    Checks that the returned list of ranks is correct, when
    having 2 of the same rank.
    """
    check_two_same = [['a', 3], ['b', 4], ['c', 4], ['d', 7],
                        ['e', 5]]
    list_of_same = check_same_rank(check_two_same)
    assert isinstance(check_two_same, list)
    assert isinstance(list_of_same, list)
    assert len(list_of_same) == 13
    assert list_of_same.count(2) == 1
    assert list_of_same.count(1) == 3
    assert list_of_same.count(0) == 9
    assert list_of_same[1] == 1
    assert list_of_same[2] == 2
    assert list_of_same[3] == 1
    assert list_of_same[5] == 1
    for i, occurrence in enumerate(list_of_same):
        if i == 1:
            assert occurrence == 1
        elif i == 2:
            assert occurrence == 2
        elif i == 3:
            assert occurrence == 1
        elif i == 5:
            assert occurrence == 1
        else:
            assert occurrence == 0


def test_check_same_rank__correct_one():
    """Use for unit test of function check_same_rank.

    Checks that the returned list of ranks is correct, when
    having only 1 of the same rank.
    """
    check_one_same = [['a', 3], ['b', 4], ['c', 13], ['d', 11],
                        ['e', 2]]
    list_of_same = check_same_rank(check_one_same)
    assert isinstance(check_one_same, list)
    assert isinstance(list_of_same, list)
    assert len(list_of_same) == 13
    assert list_of_same.count(1) == 5
    assert list_of_same.count(0) == 8
    assert list_of_same[0] == 1
    assert list_of_same[1] == 1
    assert list_of_same[2] == 1
    assert list_of_same[9] == 1
    assert list_of_same[11] == 1
    for i, occurrence in enumerate(list_of_same):
        if i == 0:
            assert occurrence == 1
        elif i == 1:
            assert occurrence == 1
        elif i == 2:
            assert occurrence == 1
        elif i == 9:
            assert occurrence == 1
        elif i == 11:
            assert occurrence == 1
        else:
            assert occurrence == 0


def test_check_same_rank__not_list():
    """Used for unit test of function check_same_rank.

    Check that sending in different argument than
    list to parameter for what to find returns None.
    """
    use_int_not_list_rank = 3
    use_float_not_list_rank = 2.2
    use_str_not_list_rank = '4'
    use_tuple_not_list_rank = ('2', '4')
    check_list_of_wrong_rank = [use_int_not_list_rank,
                                use_float_not_list_rank,
                                use_str_not_list_rank,
                                use_tuple_not_list_rank]
    for check_list_rank in check_list_of_wrong_rank:
        assert check_same_rank(check_list_rank) is None
