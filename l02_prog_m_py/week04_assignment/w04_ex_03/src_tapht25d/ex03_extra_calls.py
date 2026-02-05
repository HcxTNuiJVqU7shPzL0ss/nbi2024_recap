"""Module for extra function calls used in exercise 03, week 04.

Lesson 02, Week 04, Exercise 03.
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
from ex03_functions import (ex03_01_find_number, ex03_02_find_random)
# pylint: enable=import-error


from my_funct_dir.my_base_functions import (press_continue)


def ex03_version1_find_number():
    """Use to find the number for exercise 03 version 1."""
    print('This is version 1 from exercise 03.\n'
          'It will present which number that brings the sum '
          'total above 21.')
    press_continue()
    the_number_that_breaks = ex03_01_find_number()
    print(f'The number found to be:\n{the_number_that_breaks}')
    press_continue()


def ex03_version2_find_random():
    """Use to have random cards bring the total above 21.

    Returns
    Index 0: A list of the cards dealt
    Index 1: The sum total (above 21)
    Index 2: The number of cards delt
    """
    print('This is version 2 from exercise 03.\n'
          'After random cards have brought the sum total above 21, '
          'a few things will presented.')
    press_continue()
    returning_list = ex03_02_find_random()
    print(f'The sum total was: {returning_list[1]}\n'
          f'The number of cards were: {returning_list[2]}')
    print('The cards in order were:')
    for i in returning_list[0]:
        print(i)
    press_continue()


def run_all_functions_03():
    """Use to run all the functions.

    Rather than cluttering the main file with function calls,
    will run all functions from here.
    """
    # Version 1
    ex03_version1_find_number()

    # Version 2
    ex03_version2_find_random()
