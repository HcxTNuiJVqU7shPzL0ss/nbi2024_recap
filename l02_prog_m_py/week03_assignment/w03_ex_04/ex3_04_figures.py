"""Module for Lesson 02, Week 03, Exercise 04.

Draw figures a though j.
"""

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


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


# Example code:
# for y in range(1, 7):
#     s = ""
#     for x in range(1, 9):
#         if x == y:
#             s += "#"
#         else:
#             s += "."
#     print(s)


def w3_ex4_fig_base():
    """Use to draw figure 'base'."""
    print('Ex 04 Figure base.\nFunction: ',
          w3_ex4_fig_base.__name__, sep='')
    print('\nThis is figure base from example.\n')
    print('Fig base:')
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == y:
                s += "#"
            else:
                s += "."
        print(s)


def w3_ex4_fig_a():
    """Use to draw figure 'a'."""
    print('Ex 04 Figure a.\nFunction: ',
          w3_ex4_fig_a.__name__, sep='')
    print('\nThis is figure a.\n')
    print('Fig a:')
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == 1:
                s += "#"
            else:
                s += "."
        print(s)


def w3_ex4_fig_b():
    """Use to draw figure 'b'."""
    print('Ex 04 Figure b.\nFunction: ',
          w3_ex4_fig_b.__name__, sep='')
    print('\nThis is figure b from example.\n')
    print('Fig b:')
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == y:
                s += "#"
            else:
                s += "."
        print(s)


def w3_ex4_fig_c():
    """Use to draw figure 'c'."""
    print('Ex 04 Figure c.\nFunction: ',
          w3_ex4_fig_c.__name__, sep='')
    print('\nThis is figure c from example.\n')
    print('Fig c:')
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == 3 or y == 3:
                s += "#"
            else:
                s += "."
        print(s)


def main():
    """Use as main function."""
    print('\nWeek 03, Exercise 04, Draw Figures.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    # w3_ex4_fig_base()
    # press_continue()
    #
    # w3_ex4_fig_a()
    # press_continue()
    #
    # w3_ex4_fig_b()
    # press_continue()

    w3_ex4_fig_c()

    press_exit()


if __name__ == "__main__":
    main()
