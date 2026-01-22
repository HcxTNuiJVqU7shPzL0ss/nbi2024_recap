"""Module for 'Calculator'.

Lesson 02, Week 02, Exercise 05.
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


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit,
                                            enter_int,
                                            y_or_n)


def enter_integers(number_of_integers):
    """Use to prompt user for integers."""
    print(f'You will be asked to enter an '
          f'integer {number_of_integers} times.')
    press_continue()
    cnt = 0
    numbers = []
    while cnt < number_of_integers:
        ask = f'({cnt + 1}) Please enter an integer: '
        numbers.append(enter_int(ask))
        cnt += 1
    return numbers


def sum_up_numbers(list_of_int):
    """Use to sum up the integers.

    Integers come in a list.
    """
    sum_is = 0
    for value in list_of_int:
        sum_is += value
    print(f'\nPart 1.\n'
          f'The sum of your values is: {sum_is}')
    press_continue()


def find_largest(input_list):
    """Use to find the largest integer.

    Specifically find the value without using the built-in
    function max.
    """
    sort_list = input_list
    sort_list.sort()
    print(f'Part 2.\n'
          f'The largest input integer is: {sort_list[-1]}')
    press_continue()


def find_middle(integer_list):
    """Use to check which is the middle number.

    Only use if the number of entered integers is 3,
    and only if all 3 values differ.
    """
    sort_list = integer_list
    sort_list.sort()
    print(f'Part 4.\n'
          f'The middle value is {sort_list[1]}')


def find_duplicates(list_of_int, number_of_int):
    """Use to find any duplicates in the input.

    Input integers come in a list.
    """
    seen = set()
    duplicates = []
    for i in list_of_int:
        if i in seen:
            duplicates.append(i)
        else:
            seen.add(i)
    print('Part 3.')
    if not duplicates:
        print('There were no duplicate integers entered.')
        if number_of_int == 3:
            press_continue()
            find_middle(list_of_int)
    else:
        print(f'The following duplicate(s) were '
              f'found: {duplicates}')
        # Below handle specifics from exercise if "only" using
        # three integers
        if number_of_int == 3:
            if len(duplicates) == 2:
                print('All three integers were the same.')
                press_continue()
                print(f'Part 4.\n'
                      f'The middle value is {duplicates[0]}.')
            else:
                print('Two of the integers were the same.')
                press_continue()
                print('Part 4.\n'
                      'There is no middle value to display.')


def run_calculator():
    """Use to run the calculator."""
    number_of_integers = 3
    base_numbers = enter_integers(number_of_integers)
    sum_up_numbers(base_numbers)
    find_largest(base_numbers)
    find_duplicates(base_numbers, number_of_integers)


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    Basic calculator.
    """
    print('\nThis is exercise 5, "Calculator", from week 2.')
    press_continue()

    ask_continue = 'Do you want to run again (y)es or (no): '

    while True:
        run_calculator()
        print('')
        again = y_or_n(ask_continue)
        if again == 'n':
            break
        print('')

    print('\nThank you for calculating with us, come again!')
    press_exit()


if __name__ == "__main__":
    main()
