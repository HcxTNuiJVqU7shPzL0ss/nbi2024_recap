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
#                                             press_goback,
#                                             press_exit)

from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)

color = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


def set_one():
    """Use to force One pair for test."""
    one_hand = [('hearts', 2), ('clubs', 5), ('diamonds', 8),
                ('hearts', 6), ('diamonds', 6)]
    return one_hand


def set_two():
    """Use to force Two pairs for test."""
    two_hand = [('hearts', 5), ('clubs', 5), ('diamonds', 8),
                ('hearts', 6), ('diamonds', 6)]
    return two_hand


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


def return_card(in_list, force_flush):
    """Use to return a random card."""
    # color = ['hearts', 'diamonds', 'clubs', 'spades']
    # value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    while True:
        if force_flush:
            test_color = color[0] # Use to test "flush"
        else:
            test_color = random.choice(color)
        test_value = random.choice(value)
        card = (test_color, test_value)
        if card not in in_list:
            return card
        # print('Duplicate')
        # press_goback()
        continue


def build_hand(force_straight):
    """Use to build a poker hand."""
    hand = []
    cnt = 0
    do_flush = False
    # do_flush = True # Force Flush for test
    while cnt < 5:
        cnt += 1
        new_card = return_card(hand, do_flush)
        if force_straight:
            straight_check = (new_card[0], cnt + 1)  # 2 through 6
            hand.append(straight_check)
        else:
            hand.append(new_card)
    return hand


def check_four_three_full(hand):
    """Use to check if Four or Three of a kind."""
    values = [i[1] for i in hand]
    value_counts = defaultdict(int)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1, 4]:
        return 4 # Four if a kind
    if set(value_counts.values()) == {1, 3}:
        return 3 # Three of a kind
    if set(value_counts.values()) == {2, 3}:
        return 3 # Full House
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
    value_counts = defaultdict(int)
    for v in values:
        value_counts[v] += 1
    value_range = max(values) - min(values)
    if len(set(value_counts.values())) == 1 and (value_range == 4):
        return True
    return False


def check_pairs(hand_pairs):
    """Use to check of Two pairs or One pair, or not."""
    values = [i[1] for i in hand_pairs]
    value_counts = defaultdict(int)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]:
        return 2
    if 2 in value_counts.values():
        return 1
    return 0


def prettify_print_card(hand_in):
    """Use to make a pretty print out of the hand."""
    print('Your cards are:')
    # pylint: disable=duplicate-code
    for face, value_card in hand_in:
        print_value = {
        0: 'BUG',
        2: 'Two of',
        3: 'Three of',
        4: 'Four of',
        5: 'Five of',
        6: 'Six of',
        7: 'Seven of',
        8: 'Eight of',
        9: 'Nine of',
        10: 'Ten of',
        11: 'Jack of',
        12: 'Queen of',
        13: 'King of',
        14: 'Ace of',
        }.get(value_card)
        print(print_value, face)
    # pylint: enable=duplicate-code


def poker_hand(cards):
    """Use to check the poker hand."""
    prettify_print_card(cards)
    flush = check_flush(cards)
    straight = check_straight(cards)
    three_four = check_four_three_full(cards)
    pairs = check_pairs(cards)
    print('\nYour hand resulted in:')
    if flush and straight:
        print('You got a Straight Flush!')
    elif three_four == 4:
        print('You got Four of a kind!')
    elif three_four == 3 and pairs == 1:
        print('You got a Full House!')
    elif flush:
        print('You got a Flush!')
    elif straight:
        print('You got a straight!')
    elif three_four == 3:
        print('You got Three of a kind!')
    elif pairs == 2:
        print('You got Two pairs!')
    elif pairs == 1:
        print('You got one pair!')
    else:
        print('Sadly, you are unlucky.')
    press_exit()


def main():
    """Use as main function."""
    print('\nWeek 04, Exercise 04, Poker hand.'
          '\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    do_straight = False
    # do_straight = True # Force a Straight for test
    set_hand = build_hand(do_straight)

    print(f'\nHand is:\n{set_hand}\n')

    # set_hand = set_one()  # Force One pair for test

    # set_hand = set_two() # Force Two pairs for test

    # set_hand = set_three() # Force Three of a kind for test

    # set_hand = set_four()  # Force Four of a kind for test

    # Force Full House
    # mid_hand = set_one()  # Force One pair for test of full house
    # set_hand[3:] = mid_hand[3:]
    # mid_hand = set_three()  # Force Three of a kind for full house
    # set_hand[0:3] = mid_hand[0:3]

    poker_hand(set_hand)


if __name__ == "__main__":
    main()
