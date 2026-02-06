"""Module for functions used in exercise 04, week 04.

Lesson 02, Week 04, Exercise 04.
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


import random


def create_and_return_card(list_of_cards):
    """Use to create and return a card.

    Exercise 04.
    Creates a card of random suit and rank.
    Will check incoming list to ensure a specific card cannot
    be returned twice. This is impossible in a standard deck,
    but using random cards very much could happen.
    """
    # Ensure a list has been used as parameter argument
    if not (isinstance(list_of_cards, list)):
        return None
    list_of_suits = ['spades', 'clubs', 'hearts', 'diamonds']
    list_of_ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    while True:
        # Create a random value from each list
        created_suit = random.choice(list_of_suits)
        created_rank = random.choice(list_of_ranks)
        # Put suit and rank together as a card
        drawn_card = [created_suit, created_rank]
        # Check that the card has not been drawn and dealt before
        if drawn_card not in list_of_cards:
            return drawn_card
        # Duplicate card, try again until a unique one is found
        continue


def deal_poker_hand():
    """Use to build a poker hand of 5 cards.

    Exercise 04.
    Draw a card 5 times, until a hand of 5 cards has been dealt.
    """
    hand_with_cards = []
    for card in range(0,5):
        current_card = create_and_return_card(hand_with_cards)
        hand_with_cards.append(current_card)
    return hand_with_cards
