"""Module for 'Balder'.

Lesson 02, Week 02, Exercise 02.
Done "off course".
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
                                            press_goback,
                                            press_exit)


# CONSTANTS, PEP8
MIN_LENGTH = 130
MAX_LENGTH = 272
WARNING_LENGTH_TALL = 210
TODDLER_WARNING = 88


def balder():
    """Use to run Balder function."""
    # Ask user to input length in cm.
    #s_length_cm = ''
    i_length_cm = 0
    while True:
        s_length_cm = input('\nHow tall are you (in cm): ')
        try:
            i_length_cm = int(s_length_cm)
            break
        except ValueError:
            print('\nPlease input a valid integer!')
            press_goback()
            continue


    # Check if user is allowed to ride Balder.
    if i_length_cm >= MIN_LENGTH:
        print('\nYou are allowed to ride!\n')
        press_continue()
        if i_length_cm > MAX_LENGTH:
            print('\nYou are taller than Robert Wadlow!\n'
                  'Call Guinness, we have a record!\n')
            press_continue()
        elif i_length_cm >= WARNING_LENGTH_TALL:
            print('\nYou are very tall, make sure you feel safe '
                  'riding!\n')
            press_continue()
    else:
        print('\nYou are not tall enough, you may not ride!\n')
        press_continue()
        if i_length_cm <= TODDLER_WARNING:
            print('\nYou are quite short, you should not ride!\n'
                  'Safety first.\n')
            press_continue()


    # Discuss
    print('\nQ: Why three values?')
    print('Check below, exact and above the single limit.\n')
    press_continue()

    print('\nQ: Why these three values?')
    print('Checks below, exact and above the specified limit.\n')
    press_continue()

    print('\nQ: Would it help to add the test value of 129 cm?')
    print('No, this would not add value.\n')


def main():
    """Use as main function.

    This version made for the recap of 2024.
    """
    print('\nLesson 02, Week 02, Exercise 02, Balder.')
    press_continue()

    balder()

    press_exit()


if __name__ == "__main__":
    main()
