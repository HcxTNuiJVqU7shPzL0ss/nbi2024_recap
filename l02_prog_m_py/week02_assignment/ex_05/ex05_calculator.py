"""Module for Lesson 02, Week 02, Exercise 05, Calculator."""


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


import sys

from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit, enter_int)


print('\nWeek 02, Exercise 05, Calculator.\n')
press_continue()


# CONSTANT PEP8
CRASH_INFO = '\nSomething crashed, check your code!'


def ask_for_some_ints():
    """Use to request user to input integers."""
    # Version 1 (ask for "three" integers).
    loop_count = 3
    loop_nos = []
    base_string = 'Please input integer number '
    print('\nYou will be asked to input an integer', loop_count, 'times.\n')
    press_continue()
    i = 0
    while i < loop_count:
        send_string = base_string + str(i+1) + ': '
        loop_nos.append(enter_int(send_string, 0, 0, False))
        i += 1
        #print('i:', i)
        #print('loop_nos:', loop_nos)
    return loop_nos


def sum_ints(int_list_sum):
    """Use to add the integers from a list and report the sum."""
    # Version 1 (sum up the integers).
    total_sum = 0
    for value in int_list_sum:
        total_sum += value
    # Sanity check with built-in sum()
    check_sum = sum(int_list_sum)
    if total_sum == check_sum:
        return total_sum
    #else:
    print(CRASH_INFO)
    sys.exit()


def largest_int(int_list_largest):
    """Use to find the largest integer."""
    # Variant 2 (find the largest integer).
    # Smallest possible: -9223372036854775808
    largest = -sys.maxsize - 1
    for value in int_list_largest:
        # pylint: disable=consider-using-max-builtin
        # Part of assignment, have to use it!
        if value > largest:
            largest = value
        # pylint: enable=consider-using-max-builtin
    # Sanity check with built-in max()
    sanity_large = max(int_list_largest)
    if largest == sanity_large:
        return largest
    print(CRASH_INFO)
    sys.exit()


def run_calculator():
    """Run the program."""
    numbers_list = ask_for_some_ints()
    #print(numbers_list)
    your_sum = sum_ints(numbers_list)
    big_int = largest_int(numbers_list)

    print('\nYour integers were:', numbers_list)
    press_continue()
    print('\nYour sum of input integers is:', your_sum)
    press_continue()
    print('\nThe largest integer entered was:', big_int)


run_calculator()

print('')
press_exit()
