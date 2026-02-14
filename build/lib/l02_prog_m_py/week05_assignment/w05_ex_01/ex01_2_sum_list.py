"""Module for Lesson 02, Week 05, Exercise 1.2, Fix "sum_list".

Update the code and fix it, including tests in separate file.
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


def sum_list(list_in_sum):
    """Sum up incoming numbered list.

    If parameter is of a type other than list, return TypeError.
    If empty list, return None.
    If any non numbered items, return 'incorrect' string.
    """
    # Store the function first parameter name from sum_list
    param_name_sum = dir()[0]
    tot = 0
    if not isinstance(list_in_sum, list): # Wrong type
        wrong_type = type(list_in_sum)
        raise TypeError(f'Need a list for parameter: {param_name_sum}.\n'
                        f'What was entered is of type: {wrong_type}')
    if not list_in_sum: # List is empty
        return None
    for item in list_in_sum:
        if (not isinstance(item, bool) and
                isinstance(item, (int, float))):
            tot += item
        else:
            tot = 'incorrect'
            break
            # return tot
    return tot


def run_sum_list():
    """Use to run function sum_list.

    Creates the input, handles the output.
    """
    expected_sum = 15
    list_to_sum_up = [1, 2, 3, 4, 5]

    print(f'Will search the list {list_to_sum_up}.\n'
          f'The sum will be presented.\n'
          f'Should give: {expected_sum}.\n')

    result = sum_list(list_to_sum_up)
    print(f'The sum is: {result}')


def main():
    """Use as main function."""
    print('\nWeek 05, Exercise 1.2, Sum list.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    run_sum_list()

    press_exit()


if __name__ == "__main__":
    main()
