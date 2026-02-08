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
from ex04_functions import deal_poker_hand, check_other_than_straight
# pylint: enable=import-error


def get_a_new_hand():
    """Use to get a hand to use for poker."""
    new_hand = deal_poker_hand()
    # Sort the cards by rank
    new_hand.sort(key=lambda card: card[1])
    return new_hand


def run_game():
    """Use to run a poker game."""
    my_hand = get_a_new_hand()
    possible_outcome = check_other_than_straight(my_hand)
    # Use a comprehension that extracts the second element of each
    # pair and counts how many are True (behaves as 1)
    # Only one should ever be true
    # The _ is used to signal to ignore the first element
    number_of_true = sum(1 for _, is_true in possible_outcome
                         if is_true)
    # Use the fact that only one element can have its second
    # element equal to True, pick that entry
    # Here, magic_hand will be the first element (the string)
    # corresponding to the True value
    magic_hand = next(hand for hand, is_true in possible_outcome
                      if is_true)
    if number_of_true > 1 or magic_hand == 'Should not happen':
        print('You have found a bug!')
    print_pretty_output(my_hand, magic_hand)


def print_pretty_output(poker_hand, result):
    """Use to make a pretty printout of the hand.

    Also, will print out the result of the hand.
    """
    print('Your hand contains:')
    for pretty, value_card in poker_hand:
        print_value = {
            0: 'This must be a bug',
            2: 'Two (2) of',
            3: 'Three (3) of',
            4: 'Four (4) of',
            5: 'Five (5) of',
            6: 'Six (6) of',
            7: 'Seven (7) of',
            8: 'Eight (8) of',
            9: 'Nine (9) of',
            10: 'Ten (10) of',
            11: 'Jack (11) of',
            12: 'Queen (12) of',
            13: 'King (13) of',
            14: 'Ace (14) of',
        }.get(value_card)
        print(print_value, pretty)
    print(f'\nHere is what you got: {result}')
