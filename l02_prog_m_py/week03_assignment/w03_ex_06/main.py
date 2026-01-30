"""Module for 'List of Chores'.

Lesson 02, Week 03, Exercise 06.
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
                                            enter_string)


def create_base_list():
    """Use to create the first empty list."""
    empty_list = []
    return empty_list


def print_list(list_to_print):
    """Use to print the list."""
    if not list_to_print:
        print('\nYour list is empty')
        press_continue()
    else:
        print('\nYour list contains:')
        for list_item in list_to_print:
            print(list_item)
        press_continue()


def add_to_list():
    """Use to add an item to the list."""
    ask_str = 'Please enter the new item: '
    print('')
    add_item = enter_string(ask_str)
    add_item = '  + ' + add_item
    return add_item


def user_interaction(input_list):
    """Use to interact with the user."""
    menu_options = ['** The Optimal Chores List **',
                    '  1: See the contents of your list',
                    '  2: Add new bullets to your list',
                    '  3: Mark as done',
                    '  4. Undo done (add back)',
                    '  q: Quit (list disappear, end program)']
    available_options = ['1', '2', '3', 'q']
    select_option = 'Select an option from the menu: '

    while True:
        print('')
        for option in menu_options:
            print(option)

        print('')
        selected_option = input(select_option)

        if selected_option.casefold() not in available_options:
            print('\nThat option is not available, please try again.')
            continue

        if selected_option == '1':
            print_list(input_list)
        elif selected_option == '2':
            new_item = add_to_list()
            input_list.append(new_item)
        elif selected_option == 'q':
            print('\nOK, exiting, goodbye!')
            break


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    """
    print('\nThis is exercise 6, "List of Chores", '
          'from week 3.')

    press_continue()

    list_of_chores = create_base_list()
    user_interaction(list_of_chores)

    press_exit()


if __name__ == "__main__":
    main()
