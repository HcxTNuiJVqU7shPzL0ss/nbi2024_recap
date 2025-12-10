"""Module for Lesson 02, Week 03, Exercise 06.

List of things to do, mark as done, add back.
"""

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


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit,
                                            press_goback,
                                            enter_string,
                                            enter_int_range)


def print_list(in_list):
    """Use to print a list."""
    if len(in_list) == 0:
        print('Your list is empty!')
        press_continue()
    else:
        #for i in range(len(in_list)):
        for i, item in enumerate(in_list):
            # print('* ' + in_list[i])
            print('Index:', i, '= ' + item)
        press_continue()


def add_to_list():
    """Use to add an item to the active list."""
    ask_item = 'Enter an item you want to add to the list: '
    print('')
    add_item = enter_string(ask_item)
    print('\nOK, added "' + add_item + '" to the list.')
    press_continue()
    return add_item


def remove_from_list(in_list):
    """Use to remove an item from the active list."""
    print('\nYour current active list:')
    print_list(in_list)
    remove_string = ('Enter the index from the list you '
                     'want to remove: ')
    remove_index = enter_int_range(remove_string, 0,
                                   len(in_list) - 1, True)
    selected_item = in_list[remove_index]
    print('\nOK, removed "' + selected_item +
          '" from the list.')
    press_continue()
    return remove_index


def view_removed(in_list):
    """Use to view previously removed items."""
    print('\nYour current list of finished (removed) tasks:')
    print_list(in_list)


def add_back(in_list):
    """Use to add back from previously removed."""
    print('\nYour current "done" list:')
    print_list(in_list)
    add_string = ('Enter the index from the list you '
                     'want to add back: ')
    add_index = enter_int_range(add_string, 0,
                                   len(in_list) - 1, True)
    sel_add_item = in_list[add_index]
    print('\nOK, added "' + sel_add_item +
          '" back to the active list.')
    press_continue()
    return add_index


def list_menu():
    """Use to display the menu of the list."""
    menu_options = ['a. See the contents of your list',
                    'b. Add new item to your list',
                    'c. Mark as done (remove from list)',
                    'd. View removed items',
                    'e. Add back previously removed item',
                    'q. Quit']
    option_string = 'Please enter which option you want to use: '
    current_list = []
    done_list = []
    while True:
        # Code for ANSI underline start: \033[4m
        # Code for ANSI to "stop": \033[0m
        print('\033[4m** Your list of options **\033[0m')
        #for index in range(len(menu_options)):
        for index, option in enumerate(menu_options):
            #print(menu_options[index])
            print(option)
        print('')
        selected_option = enter_string(option_string)
        if selected_option == 'a':
            print('\nYour list:')
            print_list(current_list)
            continue
        if selected_option == 'b':
            current_list.append(add_to_list())
            continue
        if selected_option == 'c':
            if len(current_list) == 0:
                print('\nThe "Task" list is empty, '
                      'cannot help with this.')
                press_goback()
                continue
            #current_list.pop(remove_from_list(current_list)) # v2
            index_to_remove = remove_from_list(current_list)
            move_item = current_list[index_to_remove]
            current_list.pop(index_to_remove)
            done_list.append(move_item)
            continue
        if selected_option == 'd':
            view_removed(done_list)
            continue
        if selected_option == 'e':
            if len(done_list) == 0:
                print('\nThe "Done" list is empty, '
                      'cannot help with this.')
                press_goback()
                continue
            index_to_add = add_back(done_list)
            move_item = done_list[index_to_add]
            done_list.pop(index_to_add)
            current_list.append(move_item)
            continue
        if selected_option == 'q':
            print('\nThank you, bye!')
            break
        print('\nUnknown option, please try again!')
        press_continue()


def main():
    """Use as main function."""
    print('\nWeek 03, Exercise 06, To Do list.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    list_menu()

    press_exit()


if __name__ == "__main__":
    main()
