"""Module for Lesson 02, Week 05, Exercise 01.2, Fix "sum_list".

Update the code and fix it, including tests in separate file.
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
                                            press_exit)


def sum_list(list_in):
    """Sum up incoming numbered list.

    If empty list, return None.
    If any non numbered items, return 'incorrect' string.
    """
    tot = 0
    if not list_in: # List is empty
        return None
    for item in list_in:
        if isinstance(item, (int, float)):
            tot += item
        else:
            tot = 'incorrect'
            return tot
    return tot


def main():
    """Use as main function."""
    print('\nWeek 05, Exercise 01.2, Sum list.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    list_to_sum_up = [1, 2, 3, 4, 5]

    result = sum_list(list_to_sum_up)
    print(f'The result is: {result}')

    press_exit()


if __name__ == "__main__":
    main()
