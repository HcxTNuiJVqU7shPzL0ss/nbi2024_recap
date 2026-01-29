"""Module for 'Receipt Calculator'.

Lesson 02, Week 03, Exercise 03.
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


import sys


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit, press_goback,
                                            enter_int_range)


def enter_values():
    """Use for exercise 3, OG.

    Enter a number of values, exit by entering "quit" or
    "avsluta".
    """
    print('Welcome to Receipt Buddy!\n'
          'Terminate by entering: quit')
    press_continue()

    terminate = ['a', 'avsluta', 'd', 'done', 'e', 'exit',
                 's', 'stop', 'q', 'quit']
    list_of_values = []

    while True:
        in_string = input('Enter a value, or "quit" to exit: ')
        # Use maketrans to map characters to their replacement
        if_need_to_replace = str.maketrans({'\"': '',
                                            '\'': '', '(': '',
                                            ')': ''})
        # Use translate to replace any characters needed
        cleaned_input = in_string.translate(if_need_to_replace)

        if cleaned_input in terminate:
            print('\nThank you, on to the next part...')
            return list_of_values

        try:
            float_in = float(in_string)
            if float_in >= 0:
                list_of_values.append(float_in)
            else:
                print('\nPlease enter a value of 0 or greater.')
                press_goback()
            continue
        except ValueError:
            print('\nPlease use a value as numbers, or "quit".')
            press_goback()
            continue


def enter_people():
    """Use for exercise 3, version 2.

    Enter the number of people, used to divide the bill.
    """
    least_amount = 1
    max_amount = 99
    use_range = True
    ask_people = ('Please enter how many of you there are in '
                  'your party, that should take part in splitting '
                  'the bill: ')
    number_of_people = enter_int_range(ask_people, least_amount,
                                       max_amount, use_range)
    return number_of_people


def enter_tips():
    """Use for exercise 3, version 3.

    Enter how much tips to add to the bill.
    No entry adds standard of 10%.
    """
    # Default value
    tip_to_add = 10
    print('')
    while True:
        tip_as_str = input('How much tip in % do you wish to add: ')
        if not tip_as_str:
            print('\nNothing entered, standard of 10% added.')
            press_continue()
            return tip_to_add
        try:
            tip_to_add = float(tip_as_str)
            if tip_to_add < 0:
                print('Need to be 0 or higher.')
                press_goback()
                continue
            return tip_to_add
        except ValueError:
            print('Let\'s try again')
            press_goback()
            continue


def calculate_and_print(value_list, people, tip):
    """Use to calculate and print the result of it all."""
    the_sum = sum(value_list)
    if the_sum == 0:
        print('\nUnfortunately, no values were entered in the '
              'beginning, nothing to calculate.')
        sys.exit()

    with_tip = the_sum * (1 + (tip/100))
    per_person = with_tip / people

    print(f'\nYou had an initial sum of {the_sum}.\n'
          f'You wished to pay {tip}% in tips.\n'
          f'There are {people} that should split the bill, '
          f'which with tip is at {with_tip}.\n'
          f'\nEach person shall pay {per_person:.2f}.')
    print('\nWelcome back!')


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    """
    print('\nThis is exercise 3, "Receipt Calculator", from week 3.')
    press_continue()

    list_of_numbers = enter_values()
    party_size = enter_people()
    add_tip = enter_tips()
    calculate_and_print(list_of_numbers, party_size, add_tip)

    press_exit()


if __name__ == "__main__":
    main()
