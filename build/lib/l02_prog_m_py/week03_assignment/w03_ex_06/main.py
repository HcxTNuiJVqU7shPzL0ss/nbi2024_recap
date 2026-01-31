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
                                            enter_string,
                                            enter_int_range)


def create_base_list():
    """Use to create the first empty list."""
    empty_list = []
    return empty_list


def print_list(list_to_print):
    """Use to print the list."""
    if not list_to_print:
        print('\nYour list is empty')
    else:
        print('\nYour list contains:')
        for i, list_item in enumerate(list_to_print):
            print(f'  {i}: {list_item}')


def add_to_list():
    """Use to add an item to the list."""
    ask_str = 'Please enter the new item: '
    print('')
    add_item = enter_string(ask_str)
    print(f'\nOK, added "{add_item}" to the list.')
    return add_item


def mark_as_done(list_to_edit):
    """Use to mark an item as done and remove it from the list."""
    if not list_to_edit:
        print('\nThe list is empty, nothing to mark as done!')
        press_continue()
        return None
    print_list(list_to_edit)
    print('')
    ask_to_edit = 'Please select which index to mark as done: '
    lowest_item = 0
    highest_item = len(list_to_edit) - 1

    done_index = enter_int_range(ask_to_edit, lowest_item,
                                 highest_item, True)

    done_item = list_to_edit.pop(done_index)
    print(f'\nOK, marked {done_item} as completed.')
    press_continue()
    return done_item


def add_back_done(done_list):
    """Use to move back an item from archive."""
    ask_to_edit = 'Please select which index to move back: '
    lowest_item = 0
    highest_item = len(done_list) - 1

    back_index = enter_int_range(ask_to_edit, lowest_item,
                                 highest_item, True)

    back_item = done_list.pop(back_index)
    print(f'\nOK, moved {back_item} back to chores.')
    press_continue()
    return back_item


def user_interaction(input_list):
    """Use to interact with the user."""
    menu_options = ['** The Optimal Chores List **',
                    '  1: See the contents of your list',
                    '  2: Add new bullets to your list',
                    '  3: Mark as done',
                    '  4: See archived items',
                    '  5. Undo done (add back)',
                    '  q: Quit (list disappear, end program)']
    available_options = ['1', '2', '3', '4', '5', 'q']
    select_option = 'Select an option from the menu: '
    done_list = []

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
            press_continue()
        elif selected_option == '2':
            new_item = add_to_list()
            input_list.append(new_item)
            press_continue()
        elif selected_option == '3':
            removed_item = mark_as_done(input_list)
            if removed_item is not None:
                done_list.append(removed_item)
        elif selected_option in ('4', '5'):
            if not done_list:
                print('\nThe archive list is empty.')
                press_continue()
                continue
            print_list(done_list)
            press_continue()
            if selected_option == '5':
                undo_done = add_back_done(done_list)
                input_list.append(undo_done)
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
