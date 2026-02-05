"""Module for tests, L02, W04, Ex03, version 2."""

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
from ..ex03_functions import ex03_02_find_random
# pylint: enable=import-error


def test_ex03_02_find_random__bust():
    """Use for unit test of function ex03_02_find_random.

    Difficult to test when using random numbers.
    This will test that the sum total was indeed over 21.
    List is returned, where index 1: The sum total (above 21)
    """
    bust_at_v2 = 22
    list_returned = ex03_02_find_random()
    assert list_returned[1] >= bust_at_v2


def test_ex03_02_find_random__no_of_cards():
    """Use for unit test of function ex03_02_find_random.

    Difficult to test when using random numbers.
    This will test that the number of cards dealt were less
    than 14.
    List is returned, where index 2: The number of cards delt
    """
    cards_max_v2 = 13
    list_returned = ex03_02_find_random()
    assert list_returned[2] < cards_max_v2 + 1


def test_ex03_02_find_random__cards_list():
    """Use for unit test of function ex03_02_find_random.

    Difficult to test when using random numbers.
    This will test that the cards dealt fulfill the spec.
    List is returned, where index 0: A list of the cards dealt
    """
    sum_min_v3 = 21
    cards_max_v3 = 13
    list_returned = ex03_02_find_random()
    cards_list = list_returned[0]
    sum_v3 = sum(cards_list)
    cards_v3 = len(cards_list)
    # Sum shall be greater than 21
    assert sum_v3 > sum_min_v3
    # Subtracting last card should bring sum to max 21
    assert (sum_v3 - cards_list[-1]) <= sum_min_v3
    # A maximum of 13 "cards" shall have been dealt
    assert cards_v3 <= cards_max_v3
    # Number of cards add upp
    assert cards_v3 == list_returned[2]
    # Sum adds up
    assert sum_v3 == list_returned[1]
