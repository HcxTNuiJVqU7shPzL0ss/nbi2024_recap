"""Module for functions used in exercise 03, week 04.

Lesson 02, Week 04, Exercise 03.
TAP HT 25D.
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


from random import randint as rand_card


def ex03_01_find_number():
    """Use to find which number brings total above 21.

    Exercise 03, version 1.
    Adding numbers in the series 1 + 2 + 3, and so on.
    Returns the number which brings the sum above 21.
    """
    starting_number_1 = 1
    largest_allowed_1 = 21
    current_number_1 = starting_number_1
    sum_so_far_1 = 0
    while True:
        for numb_1 in range(2, 100):
            if sum_so_far_1 > largest_allowed_1:
                number_busting_1 = current_number_1 - 1
                return number_busting_1
            sum_so_far_1 += current_number_1
            current_number_1 = numb_1


def ex03_02_find_random():
    """Use to find which random number that brings bust.

    Exercise 03, version 2.
    Generating random integers between 1 and 13, symbolizing
    playing cards in the Game 21.
    When the sum gets above 21, will return:
    Index 0: A list of the cards dealt
    Index 1: The sum total (above 21)
    Index 2: The number of cards delt
    """
    largest_allowed_2 = 21 # Magic number, bust if above
    sum_so_far_2 = 0 # Total running sum, ending in bust
    cnt_of_cards_2 = 0 # Number of cards to bring bust
    cards_2 = [] # List of all the cards dealt for bust
    while sum_so_far_2 <= largest_allowed_2:
        # card_2 = rand_card(1,13)
        card_2 = ex03_v3_pull_card()
        cnt_of_cards_2 += 1
        cards_2.append(card_2)
        # sum_so_far_2 += card_2
        sum_so_far_2 = ex03_v3_check_sum(sum_so_far_2, card_2)
    return [cards_2, sum_so_far_2, cnt_of_cards_2]


def ex03_v3_pull_card():
    """Use to pull a random card between 1 and 13.

    Exercise 03, version 3.
    Generating random integers between 1 and 13, symbolizing
    playing cards in the Game 21.
    """
    card_3 = rand_card(1, 13)
    return card_3


def ex03_v3_check_sum(sum_before, card_value):
    """Use to take a sum and add a new card.

    Exercise 03, version 3.
    Takes a sum before pulling a card, then adding the pulled
    card value, then returning the new sum.
    """
    if (sum_before < 0) or (sum_before > 21):
        return None
    if (card_value < 1) or (card_value > 13):
        return None
    new_sum = sum_before + card_value
    return new_sum


def ex03_v3_check_winner(user_score, computer_score):
    """Use to take check the winner of user and computer.

    Exercise 03, version 3.
    Takes the score of the user and the computer, checks who
    won, or if a tie, returns the result.
    """
    if (user_score < 0) or (computer_score < 0):
        return None
    if (user_score > 21) or (computer_score > 21):
        return None
    if user_score == computer_score:
        return 'tie'
    if user_score > computer_score:
        return 'user'
    return 'computer'
