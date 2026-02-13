"""Module for Lesson 02, Week 05, Exercise 02, part 3.

Part 2.3 function.
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


from my_funct_dir.my_base_functions import (press_continue,
                                            press_goback,
                                            enter_float,
                                            enter_int,
                                            y_or_n)


def find_median_in_list(list_of_numbers):
    """Use to find the median in a list of numbers.

    If input argument to parameter is not of type list,
    return TypeError.
    If not all elements in the list are int or float,
    return TypeError.
    An empty list returns ValueError.
    A list with only one number returns ValueError.
    A correct list input will result in a median
    is returned, according to (sorted):
    Even number of elements == average of the two middle numbers
    Odd number of elements == The middle number
    Note that sorting is done on the list prior
    to use.
    """
    # Store the function first parameter name from
    # count_words_in_string
    param_name_find_median = dir()[0]
    # Do NOT add any variable above the line that contains "dir"

    # Has to have list as type for parameter input argument
    if not isinstance(list_of_numbers, list):
        wrong_type = type(list_of_numbers)
        raise TypeError(f'\nNeed a list for parameter: '
                        f'{param_name_find_median}.\n'
                        f'What was entered is of type: '
                        f'{wrong_type}')

    # Does not allow a list with less than 2 values as input
    if len(list_of_numbers) < 2:
        raise ValueError('\nThe input list must not be empty, '
                         'nor contain just one value.\n'
                         'Please use a list as input containing at '
                         'least 2 numeric values.')

    # All elements in the list has to be of type int or float
    if not all(isinstance(element, (int, float)) for
               element in list_of_numbers):
        raise ValueError('\nThe input list must only contain '
                         '(at least 2) numeric values.')

    # Sort ascending: incoming list
    list_of_numbers.sort()

    # Find the length of the list
    list_len = len(list_of_numbers)

    # If: odd number of list elements
    if list_len % 2 != 0:
        median_index = list_len // 2
        return list_of_numbers[median_index]

    # If: even number of list elements
    mid_index_one = list_len // 2 - 1
    mid_index_two = list_len // 2
    median_value = (list_of_numbers[mid_index_one] +
                    list_of_numbers[mid_index_two]) / 2
    return median_value


def select_float_or_int():
    """Use to select if to input a float or integer."""
    float_int_ask = ('Do you wish to enter a (f)loat or '
                     'an (i)nt: ')
    accepted_values = ['f', 'float',
                       'i', 'int']
    use_float = 'f'
    use_int = 'i'
    while True:
        use_type = input(float_int_ask)
        use_type = use_type.replace('(', '').replace(')', '')
        if not use_type.casefold() in accepted_values:
            print('Please try again!')
            press_goback()
            continue
        if use_float in use_type:
            return use_float
        return use_int


def enter_value_for_list(selected_type):
    """Use to enter either a float or an int.

    Value entered is returned, to be used in a list.
    """
    if selected_type == 'f':
        use_type = 'a float'
    else:
        use_type = 'an int'
    ask_for_number_str = f'Please enter {use_type}: '
    if selected_type == 'f':
        number_to_use = enter_float(ask_for_number_str)
    else:
        number_to_use = enter_int(ask_for_number_str)
    return number_to_use


def build_numbered_list():
    """Use to build a list of numbers."""
    print('You will be asked to input numbers to store in a list.\n'
          'First, you will be asked, each time, if to input a '
          'float or an int, after this to input the selected type.\n'
          'The list is required to contain at least 2 values.')
    press_continue()
    cnt_num = 0
    ask_continue = 'Do you want to add more values (y)es or (n)o: '
    numbered_list = []
    while True:
        chosen_type = select_float_or_int()
        user_number = enter_value_for_list(chosen_type)
        numbered_list.append(user_number)
        cnt_num += 1
        print('')
        if cnt_num > 1:
            one_more = y_or_n(ask_continue)
            if one_more == 'y':
                print('')
                continue
            return numbered_list


def run_median_check():
    """Use to run the function for median check.

    Will first build a list to use from user input.
    Next will find the median and print it.
    """
    print('Welcome to median reporter!')
    press_continue()

    numbers_list = build_numbered_list()
    copy_of_list = numbers_list.copy()

    median_in_list = find_median_in_list(numbers_list)

    print(f'\nYou entered numbers to create the '
          f'list: {copy_of_list}.\n'
          f'The median of this list is: {median_in_list}.')
