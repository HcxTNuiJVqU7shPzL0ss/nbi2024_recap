"""Module for Lesson 02, Week 01, Exercise 03, Part 01b."""

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


from my_funct_dir.my_base_functions import (press_goback,
                                            press_continue,
                                            press_exit)


def int_input_01b(in_string):
    """Use to enter an integer."""
    while True:
        s_input = input('\n' + in_string)
        try:
            i_input = int(s_input)
            return i_input
        except ValueError:
            print('\nNot a valid integer, try again!')
            press_goback()
            continue


def main():
    """Use for main in part 01b."""
    print('\nExercise 3, part 1b.')
    press_continue()

    # First integer
    in_string1 = 'Enter the first integer: '
    i_input1 = int_input_01b(in_string1)

    # Second integer
    in_string2 = 'Enter the second integer: '
    i_input2 = int_input_01b(in_string2)

    # Add the two integers
    result_i = i_input1 + i_input2

    print('\nThe sum of your integers is: ', result_i, '.', sep = '')
    press_exit()


if __name__ == "__main__":
    main()
