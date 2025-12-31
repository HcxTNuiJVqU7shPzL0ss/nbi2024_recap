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

from collections import defaultdict

# from my_funct_dir.my_base_functions import (press_continue,
#                                             press_goback)

from my_funct_dir.my_base_functions import (press_continue)

color = ['hearts', 'diamonds', 'clubs', 'spades']
value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


def set_three():
    """Use to force Three of a kind for test."""
    three_hand = [('hearts', 5), ('clubs', 5), ('diamonds', 5),
                ('hearts', 7), ('diamonds', 6)]
    return three_hand


def set_four():
    """Use to force Four of a kind for test."""
    four_hand = [('hearts', 5), ('clubs', 5), ('diamonds', 5),
                ('spades', 5), ('diamonds', 6)]
    return four_hand


def return_card(in_list):
    """Use to return a random card."""
    # color = ['hearts', 'diamonds', 'clubs', 'spades']
    # value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    while True:
        test_color = random.choice(color)
        #test_color = color[0] # Use to test "flush"
        test_value = random.choice(value)
        card = (test_color, test_value)
        if card not in in_list:
            return card
        # print('Duplicate')
        # press_goback()
        continue


def build_hand():
    """Use to build a poker hand."""
    hand = []
    cnt = 0
    while cnt < 5:
        new_card = return_card(hand)
        hand.append(new_card)
        # print(cnt)
        # print(new_card)
        # print(hand)
        cnt += 1
        # straight_check = (new_card[0], cnt + 1) # 2 through 6
        # hand.append(straight_check)
        # press_continue()
    return hand


def check_four_or_three_of_a_kind(hand):
    values = [i[1] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1, 4]:
        return 4 # Four if a kind
    if set(value_counts.values()) == {1, 3}:
        return 3 # Three of a kind
    return 0


def check_flush(hand_flush):
    """Use to check if Flush or not."""
    suits = [i[0] for i in hand_flush]
    if len(set(suits)) == 1:
        return True
    return False


def check_straight(hand_straight):
    """Use to check if Straight or not."""
    values = [i[1] for i in hand_straight]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v] += 1
    value_range = max(values) - min(values)
    if len(set(value_counts.values())) == 1 and (value_range == 4):
        return True
    return False


def poker_hand(cards):
    """Use to check the poker hand."""
    flush = check_flush(cards)
    print(flush)
    straight = check_straight(cards)
    print(straight)
    three_four = check_four_or_three_of_a_kind(cards)
    print(three_four)


def main():
    """Use as main function."""
    print('\nWeek 04, Exercise 04, Poker hand.'
          '\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    set_hand = build_hand()

    print(f'\nHand is:\n{set_hand}')

    # set_hand = set_three() # Force Three of a kind for test
    # set_hand = set_four()  # Force Four of a kind for test
    poker_hand(set_hand)


if __name__ == "__main__":
    main()
