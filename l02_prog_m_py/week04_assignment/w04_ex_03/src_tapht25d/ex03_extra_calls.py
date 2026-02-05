"""Module for extra function calls used in exercise 03, week 04.

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


# pylint: disable=import-error
from ex03_functions import (ex03_01_find_number,
                            ex03_02_find_random,
                            ex03_v3_pull_card,
                            ex03_v3_check_sum,
                            ex03_v3_check_winner)
# pylint: enable=import-error


from my_funct_dir.my_base_functions import (press_continue,
                                            y_or_n)


def ex03_version1_find_number():
    """Use to find the number for exercise 03 version 1."""
    print('This is version 1 from exercise 03.\n'
          'It will present which number that brings the sum '
          'total above 21.')
    press_continue()
    the_number_that_breaks = ex03_01_find_number()
    print(f'The number found to be:\n{the_number_that_breaks}')
    press_continue()


def ex03_version2_find_random():
    """Use to have random cards bring the total above 21.

    Returns
    Index 0: A list of the cards dealt
    Index 1: The sum total (above 21)
    Index 2: The number of cards delt
    """
    print('This is version 2 from exercise 03.\n'
          'After random cards have brought the sum total above 21, '
          'a few things will presented.')
    press_continue()
    returning_list = ex03_02_find_random()
    print(f'The sum total was: {returning_list[1]}\n'
          f'The number of cards were: {returning_list[2]}')
    print('The cards in order were:')
    for i in returning_list[0]:
        print(i)
    press_continue()


def ex03_version3_play_game():
    """Use to play the Game 21 vs computer.

    If user busts on card, computer automatically wins.
    If computer busts while user is safe, user automatically wins.
    If user stops while between 0 and 21, will check who won,
    or if a tie.
    """
    print('This is version 3 from exercise 03.\n'
          'You will be asked to draw cards, value 1 through 13, '
          'until you choose to stop or go bust.\n'
          'The computer will always draw if you do, else not.')
    press_continue()
    sum_user = 0
    sum_computer = 0
    bust = 22
    ask_user_str = 'Do you want to pull a card (y)es or (n)o: '
    while (sum_user < bust) and (sum_computer < bust):
        print(f'Your current total is: {sum_user}\n'
              f'Remember if you go above 21, you\'ll be bust!\n')
        go_or_stop = y_or_n(ask_user_str)
        if go_or_stop == 'y':
            user_card = ex03_v3_pull_card()
            print(f'\nYour card was of value: {user_card}')
            sum_user = ex03_v3_check_sum(sum_user, user_card)
            print(f'Your sum is now: {sum_user}')
            computer_card = ex03_v3_pull_card()
            sum_computer = ex03_v3_check_sum(sum_computer,
                                             computer_card)
        else:
            winner = ex03_v3_check_winner(sum_user, sum_computer)
            if winner == 'user':
                print('\nCongratulations, you won!')
            elif winner == 'computer':
                print('\nOh no! You lost!')
            else:
                print('\nWhat, a tie!?!')
            print(f'Your score: {sum_user}\n'
                  f'Computer score: {sum_computer}')
            break
    if sum_user > bust:
        print(f'\nYou went bust!\nThe score: {sum_user}')
    elif sum_computer > bust:
        print(f'\nYay, the computer went bust at {sum_computer}!\n'
              f'You had {sum_user}')


def run_all_functions_03():
    """Use to run all the functions.

    Rather than cluttering the main file with function calls,
    will run all functions from here.
    """
    # Version 1
    ex03_version1_find_number()

    # Version 2
    ex03_version2_find_random()

    # Version 3
    ex03_version3_play_game()
    while True:
        again_str = 'Do you want to play again (y)es or (n)o: '
        print('\n***   ***   ***\n')
        check_again = y_or_n(again_str)
        if check_again == 'y':
            print('')
            ex03_version3_play_game()
        else:
            print('\nHope you had fun, goodbye!')
            break
