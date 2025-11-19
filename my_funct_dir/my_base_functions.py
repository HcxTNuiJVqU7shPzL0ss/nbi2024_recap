"""My user defined functions."""


#####################################################################
#
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
#
#####################################################################


# Use to prompt user to hit enter to continue
def press_continue():
    """Use to hit enter to continue."""
    input('Press Return (Enter) to continue.\n')


# Use to prompt user to hit enter to exit
def press_exit():
    """Use to hit enter to exit."""
    input('Press Return (Enter) to exit.\n')


# Use to prompt user to "go back" and try again
def press_goback():
    """Use to hit enter to go back."""
    input('Press Return (Enter) to go back.\n')


# Use to get user input as integer
# If range is used, checks this as well, else skips it
def enter_int(input_string, low, high, any_range):
    """Use to get integer input."""
    while True:
        if any_range:
            print('\nRange is between:', low, 'and', high)
        int_s = input(input_string)
        try:
            int_i = int(int_s)
            if any_range:
                if low <= int_i <= high:
                    return int_i
                #else:
                print('\nIncorrect range, try again.')
                press_goback()
                continue
            #else:
            return int_i
        except ValueError:
            print('\nPlease use an integer!')
            press_goback()
            continue


# Use to get a string input
def enter_string(input_string):
    """Use to prompt user for an input string."""
    while True:
        user_string = input(input_string)
        try:
            if len(user_string) > 0:
                return user_string
            #else:
            print('\nNot enough characters, try again!\n')
            press_goback()
        except ValueError:
            print('\nPlease try again\n')
            press_goback()
            continue
