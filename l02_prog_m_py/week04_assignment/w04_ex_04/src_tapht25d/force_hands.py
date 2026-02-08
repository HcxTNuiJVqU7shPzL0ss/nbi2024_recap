"""Module for functions used in exercise 04, week 04.

Lesson 02, Week 04, Exercise 04.
TAP HT 25D.
This one is used to force various hands for "manual" trials.
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
from ex04_extra_calls import run_game
# pylint: enable=import-error


from my_funct_dir.my_base_functions import (press_continue,
                                            ask_y_or_n)


def set_nothing():
    """Use to force a hand containing nothing, for test."""
    nothing_hand = [('hearts', 2), ('clubs', 5), ('diamonds', 8),
                ('hearts', 7), ('diamonds', 6)]
    return nothing_hand


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


def set_five():
    """Use to force Five of a kind for test.

    Should never happen in real life.
    """
    five_hand = [('hearts', 5), ('clubs', 5), ('diamonds', 5),
                ('spades', 5), ('diamonds', 5)]
    return five_hand


def set_straight():
    """Uee to force Straight for test."""
    straight_hand = [('hearts', 5), ('clubs', 6), ('diamonds', 7),
                 ('spades', 8), ('diamonds', 9)]
    return straight_hand


def set_straight_flush():
    """Uee to force Straight for test."""
    straight_flush_hand = [('hearts', 5), ('hearts', 6), ('hearts', 7),
                 ('hearts', 8), ('hearts', 9)]
    return straight_flush_hand


def set_flush():
    """Use to force Flush for test."""
    flush_hand = [('hearts', 2), ('hearts', 4), ('hearts', 6),
                 ('hearts', 8), ('hearts', 10)]
    return flush_hand


def set_full_house():
    """Use to force Full House for test."""
    full_house_hand = [('hearts', 5), ('clubs', 5), ('diamonds', 5),
                ('hearts', 6), ('diamonds', 6)]
    return full_house_hand


def run_forced_hands():
    """Use to force different hands for test."""
    print('Here we will force different poker hands.')
    press_continue()

    force = True

    print('\nThis will test when you got: A bug!\n')
    force_hand = set_five()
    run_game(force, force_hand)
    ask_y_or_n()
    # press_continue()

    print('\nThis will test when you got: Nothing\n')
    force_hand = set_nothing()
    run_game(force, force_hand)
    ask_y_or_n()
    # press_continue()

    print('\nThis will test when you got: One Pair\n')
    force_hand = set_one()
    run_game(force, force_hand)
    ask_y_or_n()
    # press_continue()

    print('\nThis will test when you got: Two Pair\n')
    force_hand = set_two()
    run_game(force, force_hand)
    ask_y_or_n()
    # press_continue()

    print('\nThis will test when you got: Three of a Kind\n')
    force_hand = set_three()
    run_game(force, force_hand)
    ask_y_or_n()
    # press_continue()

    print('\nThis will test when you got: Straight\n')
    force_hand = set_straight()
    run_game(force, force_hand)
    ask_y_or_n()
    # press_continue()

    print('\nThis will test when you got: Flush\n')
    force_hand = set_flush()
    run_game(force, force_hand)
    ask_y_or_n()
    # press_continue()

    print('\nThis will test when you got: Full House\n')
    force_hand = set_full_house()
    run_game(force, force_hand)
    ask_y_or_n()
    # press_continue()

    print('\nThis will test when you got: Four of a Kind\n')
    force_hand = set_four()
    run_game(force, force_hand)
    ask_y_or_n()
    # press_continue()

    print('\nThis will test when you got: Straight Flush\n')
    force_hand = set_straight_flush()
    run_game(force, force_hand)
    ask_y_or_n()
    # press_continue()

    print('\nThat was all of it, hope there were no bugs!')
