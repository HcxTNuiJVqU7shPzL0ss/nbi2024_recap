"""Functions for Lesson 02, Week 04, Exercise 02."""

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


from my_funct_dir.my_base_functions import (press_continue)


def my_function_2_1(in_name):
    """Use for exercise 02, part 01."""
    print('\nThis is exercise 01.\n')
    add_string = ' is a real hacker'
    print(in_name + add_string)
    print('\nEnd of part 01.')
    press_continue()


def eko_2a(in_string):
    """Use to echo incoming string."""
    print('\nThis is exercise 02a.\n')
    print(in_string + in_string)
    print('\nEnd of part 02a.')
    press_continue()


def eko_2b(in_string, count):
    """Use to echo incoming string count number of times."""
    print('\nThis is exercise 02b.\n')
    # int_cnt = count
    # int_string = in_string
    print(in_string * count)
    # int_cnt -= 1
    # while int_cnt > 0:
    #     int_string += in_string
    #     int_cnt -= 1
    # print(int_string)
    print('\nEnd of part 02b.')


def my_function_2_3():
    """Use for exercise 02, part 03."""
    # Loop 5 times, should print out: 32.
    print('\nThis is exercise 03.\n')

    end = 5
    y = 1
    for x in range(1, 100):
        y *= 2
        # avsluta loopen med en if-sats här
        if x == end:
            break
    print(y)

    print('\nEnd of part 03.')
    press_continue()


def last(in_list_04):
    """Use to return the last element of the list parameter."""
    print('\nThis is exercise 04.\n')
    return in_list_04[-1]


def cut_edges(in_list_05):
    """Use to return the list without the first and last element."""
    print('\nThis is exercise 05.\n')
    internal_list = in_list_05
    internal_list.remove(0)
    internal_list.pop(-1)
    return internal_list


def increase(x):
    """Use to increase x by 1 and return the result."""
    print('\nThis is exercise 06.\n')
    x += 1
    return x


def average(x, y):
    """Use to return the average value of the two parameters."""
    print('\nThis is exercise 07.\n')
    aver_value_07 = (x + y) / 2
    return aver_value_07
