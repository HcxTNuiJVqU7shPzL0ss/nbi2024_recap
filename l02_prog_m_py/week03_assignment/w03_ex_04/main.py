"""Module for 'Figures with Loops'.

Lesson 02, Week 03, Exercise 04.
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


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


def ex4_figure_a(x_input_a):
    """Use to print figure 'a'."""
    if x_input_a == 1:
        return '#'
    return '.'


def ex4_figure_b(x_input_b, y_input_b):
    """Use to print figure 'b'."""
    if x_input_b == y_input_b:
        return '#'
    return '.'


def ex4_figure_c(x_input_c):
    """Use to print figure 'c'."""
    if x_input_c in [3, 4, 5]:
        return '#'
    return '.'


def ex4_figure_d(x_input_d, y_input_d):
    """Use to print figure 'd'."""
    if x_input_d == 3 or y_input_d == 3:
        return '#'
    return '.'


def ex4_figure_e(x_input_e, y_input_e):
    """Use to print figure 'e'."""
    if x_input_e in (5, 7 - y_input_e):
        return '#'
    return '.'


def ex4_figure_f(x_input_f, y_input_f):
    """Use to print figure 'f'."""
    if x_input_f in (y_input_f, 7 - y_input_f):
        return '#'
    return '.'


def ex4_figure_g(x_input_g):
    """Use to print figure 'g'."""
    if x_input_g % 2 != 0:
        return '#'
    return '.'


def ex4_figure_h(x_input_h, y_input_h):
    """Use to print figure 'h'."""
    use_pound_hash = False
    if (1 < x_input_h < 8) and y_input_h in (2, 5):
        use_pound_hash = True
    elif x_input_h in (2, 7) and y_input_h in (3, 4):
        use_pound_hash = True

    if use_pound_hash:
        return '#'
    return '.'


def ex4_figure_i(x_input_i, y_input_i):
    """Use to print figure 'i'."""
    use_pound_hash = False
    use_zero = False
    if x_input_i % 3 == (y_input_i + 1) % 3:
        use_pound_hash = True
    elif x_input_i % 3 == (y_input_i + 2) % 3:
        use_zero = True

    if use_pound_hash:
        return '#'
    if use_zero:
        return '0'
    return '.'


def ex4_figure_j(x_input_j, y_input_j):
    """Use to print figure 'j'."""
    use_pound_hash = False
    if x_input_j in (3, 6) and (1 <= y_input_j <= 3):
        use_pound_hash = True
    elif x_input_j % 2 == 0 and y_input_j == 5:
        use_pound_hash = True
    elif x_input_j % 2 != 0 and y_input_j == 6:
        use_pound_hash = True

    if use_pound_hash:
        return '#'
    return '.'


def print_figures():
    """Use to print the supported figures."""
    supported_figures = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                         'h', 'i', 'j']
    for i in supported_figures:
        press_continue()
        print('This is figure ' + i + ':')
        for y in range (1, 7, 1):
            s = ''
            for x in range(1, 9, 1):
                dispatch = {
                    'a': ex4_figure_a,
                    'b': ex4_figure_b,
                    'c': ex4_figure_c,
                    'd': ex4_figure_d,
                    'e': ex4_figure_e,
                    'f': ex4_figure_f,
                    'g': ex4_figure_g,
                    'h': ex4_figure_h,
                    'i': ex4_figure_i,
                    'j': ex4_figure_j,
                }

                # Detect whether the function expects 1 or 2 args
                func = dispatch[i]
                s += func(x) if func.__code__.co_argcount == 1 \
                    else func(x, y)

                # Below code may be easier to understand when
                # reading, but generates too-many-branches
                # in pylint
                # if i == 'a':
                #     s += ex4_figure_a(x)
                # elif i == 'b':
                #     s+= ex4_figure_b(x, y)
                # elif i == 'c':
                #     s += ex4_figure_c(x)
                # elif i == 'd':
                #     s+= ex4_figure_d(x, y)
                # elif i == 'e':
                #     s += ex4_figure_e(x, y)
                # elif i == 'f':
                #     s+= ex4_figure_f(x, y)
                # elif i == 'g':
                #     s += ex4_figure_g(x)
                # elif i == 'h':
                #     s += ex4_figure_h(x, y)
                # elif i == 'i':
                #     s += ex4_figure_i(x, y)
                # elif i == 'j':
                #     s += ex4_figure_j(x, y)
            print(s)


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    """
    print('\nThis is exercise 4, "Figures with Loops", '
          'from week 3.')

    print_figures()

    press_exit()


if __name__ == "__main__":
    main()
