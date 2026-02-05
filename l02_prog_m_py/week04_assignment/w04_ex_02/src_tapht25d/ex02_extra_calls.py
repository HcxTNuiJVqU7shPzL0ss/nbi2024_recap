"""Module for extra function calls used in exercise 02, week 04.

Lesson 02, Week 04, Exercise 02.
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
from ex02_functions import (ex02_01_hacker, ex02_02a_echo_twice,
                            ex02_02b_echo_multi, ex02_03_end_loop,
                            ex02_04_last_element, ex02_05_cut_edges,
                            ex02_06_increase)
# pylint: enable=import-error


from my_funct_dir.my_base_functions import (press_continue,
                                            enter_string,
                                            enter_int_range,
                                            y_or_n, enter_int,
                                            enter_float)


def ex02_part01_add_name():
    """Use to add name for exercise 04 part 01."""
    print('This is part 01 from exercise 02.\n'
          'Your entered name will be added to a string that '
          'will print.')
    press_continue()
    ask_str = 'Please enter your name: '
    entered_name = enter_string(ask_str)
    final_string = ex02_01_hacker(entered_name)
    print(f'\n{final_string}')
    press_continue()


def ex02_part02a_add_echo_str():
    """Use to echo incoming string twice.

    To call function and handle printout for exercise 04 part 2a.
    """
    print('This is part 02 a, from exercise 02.\n'
          'Your entered string will be echoed twice, this '
          'will then print.')
    press_continue()
    ask_str_echo = 'Please enter what to echo: '
    echo_text = enter_string(ask_str_echo)
    echoed_for_print = ex02_02a_echo_twice(echo_text)
    print(f'\n{echoed_for_print}')
    press_continue()


def ex02_part02b_echo_str_multiplier():
    """Use to echo incoming string 'multiplier' times.

    To call function and handle printout for exercise 04 part 2b.
    """
    print('This is part 02 b, from exercise 02.\n'
          'Your entered string will be echoed the selected number '
          'of times, this will then print.')
    press_continue()
    ask_str_echo = 'Please enter what to echo: '
    ask_int_multiplier = 'Please enter how many times to echo: '
    low_int = 2
    high_int = 10
    use_range = True
    echo_text = enter_string(ask_str_echo)
    multiplier_int = enter_int_range(ask_int_multiplier, low_int,
                                     high_int, use_range)
    echoed_for_print = ex02_02b_echo_multi(echo_text, multiplier_int)
    print(f'\n{echoed_for_print}')
    press_continue()


def ex02_part3_print_after_loop():
    """Use to handle the printout of the return value.

    The loop ends after 5 times, returning 32.
    (1 = 2, 2 = 4, 3 = 8, 4 = 16, 5 = 32)
    """
    print('This is part 03, from exercise 02.\n'
          'The function will calculate 32, it will print here.')
    press_continue()
    print(ex02_03_end_loop())
    press_continue()


def add_elements_to_string(input_list):
    """Use to add elements to a list."""
    element_no = len(input_list)
    ask_if_continue = ('Do you want to add one more element to '
                       'the list, (y)es or (n)o: ')
    while True:
        add_element_str = (f'Please enter what to place at '
                           f'index {element_no}: ')
        add_this = enter_string(add_element_str)
        input_list.append(add_this)
        element_no += 1
        more = y_or_n(ask_if_continue)
        if more == 'y':
            continue
        break
    return input_list


def ex02_part4_return_last_element():
    """Use to return the last element in a list.

    Rather than creating a list, will use user input to create
    the list. After this, print the last entered element.
    """
    print('This is part 04, from exercise 02.\n'
          'Add entries to a list, when done, the last added element '
          'will be printed.')
    press_continue()
    list_for_last = []
    list_for_last = add_elements_to_string(list_for_last)
    the_last_one = ex02_04_last_element(list_for_last)
    print(f'\nThe last element added was:\n{the_last_one}')
    press_continue()


def ex02_part5_cut_edges_off():
    """Use to return a list with the first and last element removed.

    Rather than creating a list, will use user input to create
    the list. After this, print the list with specified elements
    as of assignment removed.
    """
    print('This is part 05, from exercise 02.\n'
          'Add entries to a list, when done, the first and the last '
          'added element will be removed, finally the remaining '
          'list will be printed.')
    press_continue()
    list_for_edges = []
    while True:
        list_for_edges = add_elements_to_string(list_for_edges)
        if len(list_for_edges) >= 3:
            break
        print('\nThe list needs to contain at least three (3) '
              'elements, please add more.\n')
        continue
    the_middle_ones = ex02_05_cut_edges(list_for_edges)
    print(f'\nThe middle element(s) added is/are:\n'
          f'{the_middle_ones}')
    press_continue()


def ex02_part6_increase_number():
    """Use to send an int or a float as parameter to function.

    Takes the return value, which should have increased the
    input by one (1), then prints it.
    """
    print('This is part 06, from exercise 02.\n'
          'You will be asked to select if to input an '
          'int (integer) or a float (decimal value).\n'
          'The entered value will have one (1) added to it, '
          'this will then be printed.')
    press_continue()
    select_str = 'Do you want to enter an (i)nt or a (f)loat: '
    while True:
        selected_type = input(select_str)
        int_check = ('i', '(i)', 'int', '(i)nt')
        float_check = ('f', '(f)', '(f)loat')
        try:
            if selected_type.lower() in int_check:
                selected_type = 'i'
                break
            if selected_type.lower() in float_check:
                selected_type = 'f'
                break
        except ValueError:
            print('\nPlease retry.\n')
            continue
    enter_value_str = 'Please enter your value: '
    if selected_type == 'i':
        value_to_use = enter_int(enter_value_str)
    elif selected_type == 'f':
        value_to_use = enter_float(enter_value_str)
    else:
        value_to_use = None
        print('Something has gone wrong!')
    increased_value = ex02_06_increase(value_to_use)
    print(f'\nYou entered the value {value_to_use}, when '
          f'it was increased by one became: {increased_value}')
    press_continue()
