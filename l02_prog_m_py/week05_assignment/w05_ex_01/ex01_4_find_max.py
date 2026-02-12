"""Module for Lesson 02, Week 05, Exercise 1.4, Find max.

Build a function that finds the largest number in a list.
TAP HT 25D, though done in near time off course, then
refactored for this week.
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


def find_max(list_in_max):
    """Find the max numbered value in incoming list.

    If empty list, return None.
    If there are no numbered items, return 'incorrect' string.
    Will not use built-in "max" directly, looking at numbers only.
    """
    # Store the function first parameter name from find_max
    param_name_max = dir()[0]
    found_max = float('-inf')
    no_numbers = found_max
    if not isinstance(list_in_max, list):
        wrong_type = type(list_in_max)
        raise TypeError(f'Need a list for parameter: {param_name_max}.\n'
                        f'What was entered is of type: {wrong_type}')
    if not list_in_max: # List is empty
        return None
    for item in list_in_max:
        if (not isinstance(item, bool) and
                isinstance(item, (int, float))):
            found_max = max(found_max, item)
    if found_max == no_numbers:
        return 'incorrect'
    return found_max


def run_find_max():
    """Use to run function find_max.

    Creates the input, handles the output.
    """
    max_no = 10
    list_to_search = [max_no, 'a', 2, 3, 4, 5]

    print(f'Will search the list {list_to_search}.\n'
          f'The largest number will be presented.\n'
          f'Should give: {max_no}.\n')

    result = find_max(list_to_search)
    print(f'The max found is: {result}')


def main():
    """Use as main function."""
    print('\nWeek 05, Exercise 1.4, Sum list.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    run_find_max()

    press_exit()


if __name__ == "__main__":
    main()
