"""Module for Lesson 02, Week 05, Exercise 04.

Generate the multiplication table, for positive integers range
1 to 10, based on user input.
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
from w05_ex04_functions import multiplication_table, select_integers
# pylint: enable=import-error


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


def main():
    """Use as main function."""
    print('\nWeek 05, Exercise 04, Multiplication table.'
          '\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    # Hard coded check
    n = 1
    limit = 10
    result = multiplication_table(n, limit)
    print(f'Result: {result}')
    press_continue()

    # User controlled
    user_ints = select_integers()
    user_result = multiplication_table(user_ints[0],user_ints[1])
    print(f'Result: {user_result}')

    press_exit()


if __name__ == "__main__":
    main()
