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


def find_2nd_max(list_in):
    """Find the second to max numbered value in incoming list.

    If empty list, there are no numbered items, or only one
    number, return None.
    If there is a tie for first place, this value will be
    returned.
    """
    found_max = float('-inf')
    found_2nd_max = float('-inf')
    cnt_nr = 0
    if not list_in: # List is empty
        return None, None
    if len(list_in) < 2: # Less than 2 values in list
        return None, None
    for item in list_in:
        if isinstance(item, (int, float)): # Only check int and float
            if cnt_nr == 0:
                found_max = item
            elif item > found_max:
                found_2nd_max = found_max
                found_max = item
            # Does not allow two "high" values only
            #elif item > found_2nd_max and item != found_max:
            elif item > found_2nd_max:
                found_2nd_max = item
            cnt_nr += 1
    if found_2nd_max == float('-inf') or cnt_nr < 2:
        return None, None
    return found_2nd_max, cnt_nr


def main():
    """Use as main function."""
    print('\nWeek 05, Exercise 01.5, Find 2nd max.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    list_to_search = [10, 'a', 2, 3, 4, 5, 17]

    result = find_2nd_max(list_to_search)
    print(f'The second to max found is: {result[0]}')
    print(f'There were {result[1]} numbers in the list.')

    press_exit()


if __name__ == "__main__":
    main()
