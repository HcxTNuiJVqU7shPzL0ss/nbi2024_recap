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

import operator

from collections import defaultdict


def create_and_return_card(list_of_cards):
    """Use to create and return a card.

    Exercise 04.
    Creates a card of random suit and rank.
    Will check incoming list to ensure a specific card cannot
    be returned twice. This is impossible in a standard deck,
    but using random cards very much could happen.
    """
    # Ensure a list has been used as parameter argument
    if not isinstance(list_of_cards, list):
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


def check_same_rank(card_list):
    """Use to check if cards have the same rank.

    Returns a list containing how many times all possible
    ranks appear in a hand.
    """
    # Ensure a list has been used as parameter argument
    if not isinstance(card_list, list):
        return None
    # Create a separate list containing only the card ranks
    rank_list = []
    # Count each possible rank for how many there are
    counted_ranks = []
    for suit, rank in card_list:
        rank_list.append(rank)
    for possible_rank in range(2, 15):
        counted_ranks.append(operator.countOf
                             (rank_list, possible_rank))
    return counted_ranks


def check_same_suit(card_list):
    """Use to check if cards have the same suit.

    Returns a list containing how many times all possible
    suits appear in a hand.
    """
    # Ensure a list has been used as parameter argument
    if not isinstance(card_list, list):
        return None
    # Create a separate list containing only the card ranks
    suit_list = []
    # Count each possible suit for how many there are
    counted_ranks = []
    list_of_suits = ['spades', 'clubs', 'hearts', 'diamonds']
    for suit, rank in card_list:
        suit_list.append(suit)
    for possible_suit in list_of_suits:
        counted_ranks.append(operator.countOf
                             (suit_list, possible_suit))
    return counted_ranks


def check_if_straight(hand_maybe_straight):
    """Use to check if Straight or not.

    Takes the poker hand from the parameter.
    Returns True if the five cards form a Straight.
    Returns False for all other hands.
    """
    # Extract card ranks, only check rank [1], not suit [0]
    ranks = [r_i[1] for r_i in hand_maybe_straight]
    # Count occurrences: Build a frequency table of card ranks
    rank_count = defaultdict(int)
    for r in ranks:
        rank_count[r] += 1
    # Check the range if it can be a Straight (then has to be 4)
    rank_range = max(ranks) - min(ranks)
    # Check that every value occur exactly once, and that the
    # values has to be consecutive
    if len(set(rank_count.values())) == 1 and (rank_range == 4):
        return True # Yes, Straight!
    return False # No, not a Straight
