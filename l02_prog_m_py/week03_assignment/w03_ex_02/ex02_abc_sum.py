"""Module for Lesson 02, Week 03, Exercise 02, a, b, c, Sum."""

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


import sys


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


def w03_ex02_part1a():
    """Use to solve part 1a.

    Calculate the sum of the integers 1 through 10.
    """
    print('Part 1a.')
    press_continue()
    answer = 0
    for i in range(11):
        answer += i
    print('The sum of the numbers 1 through 10 is: ' + str(answer))
    # Answer shall be 55
    check_this = 55
    ohno = 'Oh no, check your code!'
    try:
        if answer is check_this:
            print('You did it for 1a!')
            press_continue()
        else:
            print(ohno)
            sys.exit()
    except ValueError:
        print(ohno)
        sys.exit()


def main():
    """Use as main function."""
    print('\nWeek 03, Exercise 02, Sum.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    w03_ex02_part1a()

    press_exit()


if __name__ == "__main__":
    main()
