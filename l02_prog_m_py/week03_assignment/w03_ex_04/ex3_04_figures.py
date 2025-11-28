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


def w3_ex4_fig_base(des):
    """Use to draw figure 'base'."""
    print('Ex 04 Figure ' + des, '.\nFunction: ',
          w3_ex4_fig_base.__name__, sep='')
    print('\nThis is figure ' + des + ' from example.\n')
    print('Fig', des + ':')
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == y:
                s += "#"
            else:
                s += "."
        print(s)


def w3_ex4_fig_a(des):
    """Use to draw figure 'a'."""
    print('Ex 04 Figure ' + des, '.\nFunction: ',
          w3_ex4_fig_a.__name__, sep='')
    print('\nThis is figure ' + des + ' from example.\n')
    print('Fig', des + ':')
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == 1:
                s += "#"
            else:
                s += "."
        print(s)


def w3_ex4_fig_b(des):
    """Use to draw figure 'b'."""
    print('Ex 04 Figure ' + des, '.\nFunction: ',
          w3_ex4_fig_b.__name__, sep='')
    print('\nThis is figure ' + des + ' from example.\n')
    print('Fig', des + ':')
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == y:
                s += "#"
            else:
                s += "."
        print(s)


def w3_ex4_fig_c(des):
    """Use to draw figure 'c'."""
    print('Ex 04 Figure ' + des, '.\nFunction: ',
          w3_ex4_fig_c.__name__, sep='')
    print('\nThis is figure ' + des + ' from example.\n')
    print('Fig', des + ':')
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x in [3, 4, 5]:
                s += "#"
            else:
                s += "."
        print(s)


def w3_ex4_fig_d(des):
    """Use to draw figure 'd'."""
    print('Ex 04 Figure ' + des, '.\nFunction: ',
          w3_ex4_fig_d.__name__, sep='')
    print('\nThis is figure ' + des + ' from example.\n')
    print('Fig', des + ':')
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == 3 or y == 3:
                s += "#"
            else:
                s += "."
        print(s)


def w3_ex4_fig_e(des):
    """Use to draw figure 'e'."""
    print('Ex 04 Figure ' + des, '.\nFunction: ',
          w3_ex4_fig_e.__name__, sep='')
    print('\nThis is figure ' + des + ' from example.\n')
    print('Fig', des + ':')
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            #if x == 5 or (x == (7 - y)):
            if x in (5, 7 - y):
                s += "#"
            else:
                s += "."
        print(s)


def w3_ex4_fig_f(des):
    """Use to draw figure 'f'."""
    print('Ex 04 Figure ' + des, '.\nFunction: ',
          w3_ex4_fig_f.__name__, sep='')
    print('\nThis is figure ' + des + ' from example.\n')
    print('Fig', des + ':')
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            #if x == y or (x == (7 - y)):
            if x in (y, 7 - y):
                s += "#"
            else:
                s += "."
        print(s)


def w3_ex4_fig_g(des):
    """Use to draw figure 'g'."""
    print('Ex 04 Figure ' + des, '.\nFunction: ',
          w3_ex4_fig_g.__name__, sep='')
    print('\nThis is figure ' + des + ' from example.\n')
    print('Fig', des + ':')
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x % 2 != 0:
                s += "#"
            else:
                s += "."
        print(s)


def w3_ex4_fig_h(des):
    """Use to draw figure 'h'."""
    print('Ex 04 Figure ' + des, '.\nFunction: ',
          w3_ex4_fig_h.__name__, sep='')
    print('\nThis is figure ' + des + ' from example.\n')
    print('Fig', des + ':')
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if ((y in (2,5)) and (1 < x < 8)) \
                    or ((y in (3, 4)) and (x in (2, 7))):
                s += "#"
            else:
                s += "."
        print(s)


def w3_ex4_fig_i(des):
    """Use to draw figure 'i'."""
    print('Ex 04 Figure ' + des, '.\nFunction: ',
          w3_ex4_fig_i.__name__, sep='')
    print('\nThis is figure ' + des + ' from example.\n')
    print('Fig', des + ':')
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x % 3 == (y + 1) % 3:
                s += "#"
            elif x % 3 == (y + 2) % 3:
                s += "O"
            else:
                s += "."
        print(s)


def w3_ex4_fig_j(des):
    """Use to draw figure 'j'."""
    print('Ex 04 Figure ' + des, '.\nFunction: ',
          w3_ex4_fig_j.__name__, sep='')
    print('\nThis is figure ' + des + ' from example.\n')
    print('Fig', des + ':')
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if ((1 <= y <= 3) and (x in (3, 6))) or \
                ((y == 5) and (x % 2 == 0)) or \
                    ((y == 6) and (x % 2 != 0)):
                s += "#"
            else:
                s += "."
        print(s)


def main():
    """Use as main function."""
    print('\nWeek 03, Exercise 04, Draw Figures.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    w3_ex4_fig_base('base')
    press_continue()

    w3_ex4_fig_a('a')
    press_continue()

    w3_ex4_fig_b('b')
    press_continue()

    w3_ex4_fig_c('c')
    press_continue()

    w3_ex4_fig_d('d')
    press_continue()

    w3_ex4_fig_e('e')
    press_continue()

    w3_ex4_fig_f('f')
    press_continue()

    w3_ex4_fig_g('g')
    press_continue()

    w3_ex4_fig_h('h')
    press_continue()

    w3_ex4_fig_i('i')
    press_continue()

    w3_ex4_fig_j('j')

    press_exit()


if __name__ == "__main__":
    main()
