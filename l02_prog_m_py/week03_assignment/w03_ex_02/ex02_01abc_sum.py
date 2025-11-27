"""Module for Lesson 02, Week 03, Exercise 02.

Part 1: a, b, c, Sum.
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


import sys


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


def w03_ex02_part1a(s_error, check_this):
    """Use to solve part 1a.

    Calculate the sum of the integers 1 through 10.
    """
    print('Part 1a.\nFunction: ',
          w03_ex02_part1a.__name__, sep = '')
    press_continue()
    answer = 0
    int_list = []
    for i in range(11):
        answer += i
        int_list.append(i)
    print('The sum of the numbers 1 through 10 is:\n'
          + str(answer))
    # Answer shall be 55
    overtime_sum = sum(int_list)
    try:
        if answer == check_this and answer == overtime_sum:
            print('You did it for 1a!')
            press_continue()
        else:
            print(s_error)
            sys.exit()
    except ValueError:
        print(s_error)
        sys.exit()


def w03_ex02_part1b(s_error, check_this):
    """Use to solve part 1b.

    Calculate the sum of the integers 1 through 100.
    Use a for loop.
    """
    print('Part 1b.\nFunction: ',
          w03_ex02_part1b.__name__, sep = '')
    press_continue()
    answer = 0
    int_list = []
    for i in range(101):
        answer += i
        int_list.append(i)
    print('The sum of the numbers 1 through 100 is:\n'
          + str(answer))
    # Answer shall be 5050
    overtime_sum = sum(int_list)
    try:
        if answer == check_this and answer == overtime_sum:
            print('You did it for 1b!')
            press_continue()
        else:
            print(s_error)
            sys.exit()
    except ValueError:
        print(s_error)
        sys.exit()


def w03_ex02_part1c(s_error, check_this):
    """Use to solve part 1c.

    Calculate the sum of the integers 1 through 100.
    Use a while loop (rewrite 1b).
    """
    print('Part 1c.\nFunction: ',
          w03_ex02_part1c.__name__, sep = '')
    press_continue()
    answer = 0
    int_list = []
    i = 1
    while i < 101:
        answer += i
        int_list.append(i)
        i += 1
    print('The sum of the numbers 1 through 100 is:\n'
          + str(answer))
    # Answer shall be 5050
    overtime_sum = sum(int_list)
    try:
        if answer == check_this and answer == overtime_sum:
            print('You did it for 1c!')
        else:
            print(s_error)
            sys.exit()
    except ValueError:
        print(s_error)
        sys.exit()


def main():
    """Use as main function."""
    print('\nWeek 03, Exercise 02, Sum.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    s_ohno = 'Oh no, check your code!'

    check_this_1a = 55
    # Part 1a, for, 1 - 10
    w03_ex02_part1a(s_ohno, check_this_1a)

    check_this_1bc = 5050
    # Part 1b, for, 1 - 100
    w03_ex02_part1b(s_ohno, check_this_1bc)

    # Part 1 c, while, 1 - 100
    w03_ex02_part1c(s_ohno, check_this_1bc)

    press_exit()


if __name__ == "__main__":
    main()
