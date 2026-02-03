"""Module for 'Discuss'.

Lesson 02, Week 04, Exercise 01.
TAP HT 25D.
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


# Will not import ex01_01b or ex01_01e functions, since never called
from ex01_functions import (ex01_01a, ex01_01c, ex01_01d, ex01_01f_oof, ex01_01f_oog, ex01_01g_is_number_og, ex01_01g_is_number_new)

from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


def run_ex01_part1a():
    """Use to run part 1a of exercise 01."""
    # Calls the function with 'hej' string
    # However, 't_1a' parameter is not used in the function,
    # instead it will always print: test
    string_1a = 'hej'
    ex01_01a(string_1a)


def run_ex01_part1b():
    """Use to run part 1b of exercise 01."""
    # Never calls the function.
    # Will always print:
    # 3 5
    print(3, 5)


def run_ex01_part1c():
    """Use to run part 1c of exercise 01."""
    # Will get the return value of 15, which is then printed as:
    # 15
    print(ex01_01c(3, 5))


def run_ex01_part1d():
    """Use to run part 1d of exercise 01."""
    x_1d = 2
    y_1d = 3
    # Using x, will get 10, and y will get 15, added to 25
    # Will next return 5 * 25 = 125
    a_1d = ex01_01d(ex01_01d(x_1d) + ex01_01d(y_1d))
    # Will print 125
    print(a_1d)


def run_ex01_part1e():
    """Use to run part 1d of exercise 01."""
    # Never calls the function
    # Assign value of 5 (int)
    a_1e = 5
    # Adding 2 (int) to previous value, now at 7
    a_1e += 2
    # Print the latest value, now: 7
    print(a_1e)


def run_ex01_part1f():
    """Use to run part 1f of exercise 01."""
    # Here a_1f will pass in a function call and the
    # integer 3, resulting in 18
    a_1f = ex01_01f_oog(ex01_01f_oof, 3)
    # It will print: 18
    print(a_1f)


def run_ex01_part1g():
    """Use to run part 1f of exercise 01."""
    # Here, checks if an int, it is not
    # Next check if a float, it is, prints:
    # True
    print(ex01_01g_is_number_og(5.5))
    # Here, checks if an int, it is, prints:
    # True
    print(ex01_01g_is_number_og(42))
    # Next run again with improved version, same results
    print(ex01_01g_is_number_new(5.5))
    print(ex01_01g_is_number_new(42))


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    Discuss the purpose of the code.
    Write down what you think will be printed.
    Type the code into your IDE, exactly as stated.
    Run it.
    """
    print('\nThis is exercise 1, "Discuss", from week 4.')
    print('The exercise is to add code "exactly" as written.')
    print('However, will not pass without errors and warnings, '
          'e.g. in pylint and pydocstyle, hence had to make '
          'some changes anyway, though keeping true to the '
          'OG intention, I believe.')
    press_continue()
    # 1a
    print('Running part 1a.\nWill print:\ntest\n'
          'This is regardless what is used as parameter to the '
          'function.\n')
    run_ex01_part1a()
    print('\nYes, it did what I believed it would.')
    press_continue()
    # 1b
    print('Running part 1b.\nWill print:\n3 5\n'
          'The function is never called.\n')
    run_ex01_part1b()
    print('\nYes, it did what I believed it would.')
    press_continue()
    # 1c
    print('Running part 1c.\nWill print:\n15\n')
    run_ex01_part1c()
    print('\nYes, it did what I believed it would.')
    press_continue()
    # 1d
    print('Running part 1d.\nWill print:\n125\n')
    run_ex01_part1d()
    print('\nYes, it did what I believed it would.')
    press_continue()
    # 1e
    print('Running part 1e.\nWill print:\n7\n'
          'The function is never called.\n')
    run_ex01_part1e()
    print('\nYes, it did what I believed it would.')
    press_continue()
    # 1f
    print('Running part 1f.\nWill print:\n18\n')
    run_ex01_part1f()
    print('\nYes, it did what I believed it would.')
    press_continue()
    # 1g
    print('Running part 1g "OG", followed by "New".\n'
          'Will print:\nTrue\nTrue\nTrue\nTrue\n')
    run_ex01_part1g()
    print('\nYes, it did what I believed it would.')
    press_continue()


    press_exit()


if __name__ == "__main__":
    main()
