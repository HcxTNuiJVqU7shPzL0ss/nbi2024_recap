"""Module for 'Hello World'."""


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
                                            press_exit)


# Prompt user to input "Hello world"
while True:
    first_string = input('\nPlease type "Hello world": ')
    clean_string = first_string.replace('\"', '')
    try:
        if clean_string.lower() == 'hello world':
            break
        #else:
        print('\nTry again!')
        continue
    except ValueError:
        print('\nDid not work')
        continue


# Prompt user to input their name
while True:
    name = input('\nPlease enter your name: ')
    try:
        if len(name) <= 0:
            print('\nTry again!')
            continue
        #else:
        break
    except ValueError:
        print('\nDid not work')
        continue


if not first_string == 'Hello world':
    # Print user input
    print('\nYour input was: ' + first_string)
    # Print expected
    print('Expected was: Hello world')
    #press_continue()
    if '\"' in first_string:
        print('You should not use " in your input.\n')
        press_continue()
    else:
        print('Please mind the Capitalization.\n')
        press_continue()
else:
    # If all correct, print what was expected
    print('\nHello world')


# Print a welcome message
print('This program was made by', name, '\n')


press_exit()
