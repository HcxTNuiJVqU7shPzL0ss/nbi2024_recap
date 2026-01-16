"""Module for 'Hello World', version 2.

Lesson 02, Week 01, Exercise 01.
Done "off course".
More advanced, playing around, learning things.
"""

#####################################################################
# Copyright 2025-2026 gnoff
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
                                            press_exit, press_goback)


def hello_world():
    """Prompt user to input "Hello world".

    This version made for the recap of 2024.
    """
    while True:
        first_string = input('Please type "Hello world": ')
        clean_string = first_string.replace('\"', '')
        try:
            if clean_string.lower() == 'hello world':
                break
            print('\nTry again!')
            press_goback()
            continue
        except ValueError:
            print('\nDid not work')
            press_goback()
            continue
    return first_string


def user_name_input():
    """Prompt user to input their name.

    This version made for the recap of 2024.
    """
    while True:
        name = input('\nPlease enter your name: ')
        try:
            if len(name) <= 0:
                print('\nTry again!')
                press_goback()
                continue
            break
        except ValueError:
            print('\nDid not work')
            press_goback()
            continue
    return name


def check_hello(first_string):
    """Use to check input string for Hello world.

    This version made for the recap of 2024.
    """
    if not first_string == 'Hello world':
        # Print user input
        print('\nYour input was: ' + first_string)
        # Print expected
        print('Expected was: Hello world')
        if '\"' in first_string:
            print('You should not use " in your input.')
            press_continue()
        else:
            # Does not handle the case if both using " and
            # incorrect capitalization on "Hello".
            print('Please mind the Capitalization.')
            press_continue()
    else:
        # If all correct, print what was expected.
        print('\nHello world')


def main():
    """Use as module for Main.

    This version made for the recap of 2024.
    """
    print('\nLesson 02, Week 01, Exercise 01 (version 2).')
    press_continue()

    first_string = hello_world()
    check_hello(first_string)
    name = user_name_input()

    # Print a welcome message
    print(f'\nThis program was made by {name}.')

    press_exit()


if __name__ == "__main__":
    main()
