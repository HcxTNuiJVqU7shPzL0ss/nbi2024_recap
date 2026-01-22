"""Module for 'Balder'.

Lesson 02, Week 02, Exercise 02.
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
                                            y_or_n,
                                            enter_float)


def enter_length_cm():
    """Use to get user input regarding their length in cm.

    Value is to be used to check if person is tall enough
    to ride Balder.
    No checks if too tall at this time, "just" follow the
    instructions from the exercise.
    """
    ask_length = 'Please enter your length in cm (as a number): '
    length_cm = enter_float(ask_length)
    return length_cm


def check_length():
    """Use to check if user meets Balder height restriction.

    At or above 130 cm is allowed to ride.
    Below 130 cm is not allowed to ride.
    """
    balder_min_limit = 130
    allowed_str = '\nYou are allowed to ride!\n'
    not_allowed_str = '\nSadly, you are not tall enough to ride.\n'
    rider_length_cm = enter_length_cm()
    if rider_length_cm >= balder_min_limit:
        print(allowed_str)
    else:
        print(not_allowed_str)


def check_the_line():
    """Use to run checks of the length of pople in line.

    Always checks one person, next ask if to check another.
    """
    ask_guard = 'Do you want to check one more (y)es or (n)o: '
    while True:
        check_length()
        check_another = y_or_n(ask_guard)
        if check_another == 'n':
            print('\nTake a break, the line is empty!')
            break
        print('')


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    Check if you are tall enough to be allowed to ride Balder.
    Enter length in cm, print if you are allowed to ride
    or not.
    Test with 121, 130 and 155 (130 and above is allowed).
    Discuss:
    1) Why three values?
    2) Shy these values?
    Would it be good to add 129 to the test suite?
    """
    print('\nThis is exercise 2, "Balder", from week 2.')
    print('\nPlease check the height restriction prior to standing '
          'in line to ride Balder!')
    press_continue()

    check_the_line()

    press_exit()


if __name__ == "__main__":
    main()
