"""Module for Lesson 02, Week 03, Exercise 06.

List of things to do.
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
                                            enter_string)


def list_menu():
    """Use to display the menu of the list."""
    menu_options = ['a. See the contents of your list',
                    'b. Add new item to your list',
                    'c. Quit']
    option_string = 'Please enter which option you want to use: '
    while True:
        selected_option = enter_string(option_string)
        if selected_option == 'a':
            print(menu_options[0])
            break



def main():
    """Use as main function."""
    print('\nWeek 03, Exercise 06, To Do list.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    list_menu()


    press_exit()


if __name__ == "__main__":
    main()
