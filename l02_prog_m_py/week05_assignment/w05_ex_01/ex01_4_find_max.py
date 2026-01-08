"""Module for Lesson 02, Week 05, Exercise 01.4, Find max.

Build a function that finds the largest number in a list.
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


def find_max(list_in):
    """Find the max numbered value in incoming list.

    If empty list, return None.
    If there are no numbered items, return 'incorrect' string.
    Will not use built-in "max", looking at numbers only.
    """
    found_max = float('-inf')
    if not list_in: # List is empty
        return None
    for item in list_in:
        if isinstance(item, (int, float)):
            #if item > found_max:
            found_max = max(found_max, item)
                #found_max = item
    if found_max == float('-inf'):
        return 'incorrect'
    return found_max


def main():
    """Use as main function."""
    print('\nWeek 05, Exercise 01.4, Sum list.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    list_to_search = [10, 'a', 2, 3, 4, 5]

    result = find_max(list_to_search)
    print(f'The max found is: {result}')

    press_exit()


if __name__ == "__main__":
    main()
