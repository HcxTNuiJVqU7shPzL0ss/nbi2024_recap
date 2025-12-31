"""Module for Lesson 02, Week 04, Exercise 04.

Poker hand.
"""

#####################################################################
# Copyright 2025 gnoff
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


import random


from my_funct_dir.my_base_functions import (press_continue)


def return_card(in_list):
    """Use to return a random card."""
    color = ['hearts', 'diamonds', 'clubs', 'spades']
    value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    while True:
        test_color = random.choice(color)
        test_value = random.choice(value)
        card = (test_color, test_value)
        if card not in in_list:
            return card
        continue


def main():
    """Use as main function."""
    print('\nWeek 04, Exercise 04, Poker hand.'
          '\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    hand = []

    new_card = return_card(hand)

    hand.append(new_card)

    print(new_card)
    print(hand)


if __name__ == "__main__":
    main()
