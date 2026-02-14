"""Module for Lesson 02, Week 05, Exercise 02, part 4.

Part 2.4 function.
See file w05_ex02_functions for "just following the exercise"
version of "easier not as complete" version.
This one here can be considered extensive and very
overworked, used for learning things.
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
from find_the_median import build_numbered_list
# pylint: enable=import-error


from my_funct_dir.my_base_functions import press_continue


def check_is_sorted_ascending(numbers_list):
    """Use a list of numbers, check if sorted ascending.

    If input argument to parameter is not of type list,
    return TypeError.
    If not all elements in the list are int or float,
    return TypeError.
    An empty list returns ValueError.
    A correct list input will check if sorted ascending:
    True: if sorted ascending.
    False: if not sorted ascending.
    """
    # Store the function first parameter name from
    # count_words_in_string
    param_name_check_ascending = dir()[0]
    # Do NOT add any variable above the line that contains "dir"

    # Has to have list as type for parameter input argument
    if not isinstance(numbers_list, list):
        wrong_type = type(numbers_list)
        raise TypeError(f'\nNeed a list for parameter: '
                        f'{param_name_check_ascending}.\n'
                        f'What was entered is of type: '
                        f'{wrong_type}')

    # Does not allow an empty list as input
    if not numbers_list:
        raise ValueError('\nThe input list must not be empty.\n'
                         'Please use a list as input containing at '
                         'least 1 numeric value.')

    # All elements in the list has to be of type int or float
    if not all(isinstance(element, (int, float)) for
               element in numbers_list):
        raise ValueError('\nThe input list must only contain '
                         'numeric values.')

    # Sort ascending: copy of incoming list
    copy_of_list = numbers_list.copy()
    copy_of_list.sort()

    # Check if input list is sorted ascending or not
    if copy_of_list == numbers_list:
        return True
    return False


def run_sorted_ascending():
    """Use to run the function sorted ascending.

    Will first build a list to use from user input.
    Next will check if sorted ascending (True) or not (False).
    """
    print('Welcome to sorted ascending!')
    press_continue()

    minimum_values_asc = 1
    print_info_asc = (f'The list is required to contain at '
                      f'least {minimum_values_asc} value.\n'
                      f'Next will check if you have entered '
                      f'the numbers as sorted ascending, or not.')

    list_of_numbers = build_numbered_list(print_info_asc, minimum_values_asc)
    copy_of_list = list_of_numbers.copy()

    is_ascending = check_is_sorted_ascending(list_of_numbers)

    if is_ascending:
        asc_print = 'Yes, it was'
    else:
        asc_print = 'No, it wasn\'t'

    print(f'\nYou entered numbers to create the '
          f'list: {copy_of_list}.\n'
          f'{asc_print} sorted ascending.')
