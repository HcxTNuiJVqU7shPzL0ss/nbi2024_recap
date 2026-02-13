"""Module for Lesson 02, Week 05, Exercise 02.

Parts 2.1 through 2.4, file for main.py.
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
from w05_ex02_functions import (c_to_f, count_words,
                                find_median,
                                is_sorted_ascending)
from celsius_to_fahrenheit import run_c_to_f_conversion
from count_words_in_string import run_space_check
from find_the_median import run_median_check
# pylint: enable=import-error


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


def main():
    """Use as main function."""
    print('\nWeek 05, Exercise 02, Function calls.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    # Version 1: Celsius to Fahrenheit
    check32 = c_to_f(0)
    print(check32)
    press_continue()

    # Version 2
    run_c_to_f_conversion()
    press_continue()


    # Version 1: Count words in string
    check_three = count_words('  1  2   3  ')
    print(check_three)
    press_continue()

    # Version 2
    run_space_check()
    press_continue()


    # Version 1: Check median
    check_median = find_median([-100.23, 2, 42.71, 100, -200])
    print(check_median)
    press_continue()

    # Version 2
    run_median_check()
    press_continue()


    # Version 1: Sort ascending
    check_sorted_y = is_sorted_ascending([1, 2, 42])
    print(check_sorted_y)
    press_continue()
    check_sorted_n = is_sorted_ascending([42, 3])
    print(check_sorted_n)

    press_exit()


if __name__ == "__main__":
    main()
