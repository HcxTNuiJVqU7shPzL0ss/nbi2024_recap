"""Module for Lesson 02, Week 03, Exercise 02, Part 02: Sum.

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


import sys


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


def w03_ex02_part02(s_error, sum_list):
    """Use to solve part 02.

    Calculate the sum of the elements in the list.
    """
    print('Part 02.\nFunction: ',
          w03_ex02_part02.__name__, sep = '')
    press_continue()
    answer = 0
    int_list = []
    # pylint: disable=consider-using-enumerate
    for i in range(len(sum_list)):
        answer += sum_list[i]
        int_list.append(sum_list[i])
    # pylint: enable=consider-using-enumerate
    print('The sum of the numbers in the list is:\n'
          + str(answer))
    overtime_sum = sum(int_list)
    # pylint: disable=duplicate-code
    try:
        if answer == overtime_sum:
            print('You did it for 02!')
        else:
            print(s_error)
            sys.exit()
    except ValueError:
        print(s_error)
        sys.exit()
    # pylint: enable=duplicate-code


def main():
    """Use as main function.

    This version made for the recap of 2024.
    """
    print('\nWeek 03, Exercise 02.02, Sum.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    s_ohno = 'Oh no, check your code!'

    use_list = [1, -2, 3, -2, 4, -3]
    # Part 02, sum list
    w03_ex02_part02(s_ohno, use_list)

    press_exit()


if __name__ == "__main__":
    main()
