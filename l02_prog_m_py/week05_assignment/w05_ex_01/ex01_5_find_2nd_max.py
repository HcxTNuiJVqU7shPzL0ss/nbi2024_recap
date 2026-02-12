"""Module for Lesson 02, Week 05, Exercise 1.5, Find second max.

Build a function that finds the second-largest number in a list.
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


def find_2nd_max(list_in_2nd):
    """Find the second to max numbered value in incoming list.

    If empty list, there are no numbered items, or only one
    number, return None.
    If there is a tie for first place, this value will be
    returned.
    """
    # Store the function first parameter name from find_2nd_max
    param_name_2nd_max = dir()[0]
    found_max = float('-inf')
    found_2nd_max = float('-inf')
    cnt_nr = 0
    if not isinstance(list_in_2nd, list):
        wrong_type = type(list_in_2nd)
        raise TypeError(f'Need a list for parameter: '
                        f'{param_name_2nd_max}.\n'
                        f'What was entered is of type: '
                        f'{wrong_type}')
    # List is empty, or less than 2 values in the list
    if not list_in_2nd or len(list_in_2nd) < 2:
        return None, None
    for item in list_in_2nd:
        # Check only int and float
        if (not isinstance(item, bool) and
                isinstance(item, (int, float))):
            if cnt_nr == 0:
                found_max = item
            elif item > found_max:
                found_2nd_max = found_max
                found_max = item
            elif item > found_2nd_max:
                found_2nd_max = item
            cnt_nr += 1
    # Have not found 2 numbers, or 2 numbers found, but are identical
    if found_2nd_max == float('-inf') or cnt_nr < 2:
        return None, None
    return found_2nd_max, cnt_nr


def run_2nd_max():
    """Use to run function find_2nd_max.

    Creates the input, handles the output.
    """
    second_max = 10
    list_to_search = [second_max, 'a', 2, 3, 4, 5, 17]

    print(f'Will search the list {list_to_search}.\n'
          f'The second largest number will be presented.\n'
          f'Should give: {second_max}.\n')

    result = find_2nd_max(list_to_search)

    print(f'The second to max found is: {result[0]}')
    print(f'There were {result[1]} numbers in the list.')


def main():
    """Use as main function."""
    print('\nWeek 05, Exercise 1.5, Find 2nd max.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    run_2nd_max()

    press_exit()


if __name__ == "__main__":
    main()
