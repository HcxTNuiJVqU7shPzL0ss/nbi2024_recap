"""Module for extra function calls used in exercise 04, week 04.

Lesson 02, Week 04, Exercise 04.
TAP HT 25D.
Poker Hand.
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
from ex04_functions import deal_poker_hand, check_if_straight
# pylint: enable=import-error


def get_a_new_hand():
    """Use to get a hand to use for poker."""
    new_hand = deal_poker_hand()
    return new_hand


def run_game():
    """Use to run a poker game."""
    my_hand = get_a_new_hand()
    straight = check_if_straight(my_hand)
    if straight:
        print('You got a straight!')
    else:
        print('No straight')
