"""Module for Lesson 02, Week 04, Exercise 03.

The game 21.
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


from random import randint


from my_funct_dir.my_base_functions import (press_continue)


def ex03_v1():
    """Use to find the first number above 21 in the series."""
    print('This is exercise 3, The Game 21, first version.')
    press_continue()
    running_cnt = 1
    tot = 0
    while tot <= 21:
        tot += running_cnt
        print(f'Counter is: {running_cnt}')
        print(f'Total is: {tot}')
        running_cnt += 1
        press_continue()
    print('The first number above 21 is: ' + str(tot))
    press_continue()


def ex03_v2():
    """Use to find the first number above 21 using cards."""
    print('This is exercise 3, The Game 21, second version.')
    press_continue()
    tot = 0
    while tot <= 21:
        card = randint(1, 13)
        tot += card
        print(f'Card is: {card}')
        print(f'Total is: {tot}')
        press_continue()
    print('The first number above 21 is: ' + str(tot))
    press_continue()


def main():
    """Use as main function."""
    print('\nWeek 04, Exercise 03, The Game 21.'
          '\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    ex03_v1()

    ex03_v2()


if __name__ == "__main__":
    main()
