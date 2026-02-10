"""Module for Lesson 02, Week 05, Exercise 01.1, Discuss.

Which equivalence classes does the expressions have?
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
                                            press_exit, ask_y_or_n,
                                            y_or_n)


def w05_ex01_1a(x, unit):
    """Use for 1.1a part.

    Parameter 'unit' used as True if to run unit test,
    if False instead 'normal run'.
    If other than int or float used as argument for
    parameter 'x', raises TypeError.
    x > 100
    EC1 == Any number greater than 100 (int or float)
    EC2 == Any number of 100 or lower (int or float)
    EC1 for x returns True.
    EC2 for x returns False.
    """
    if not unit:
        print('This is part 1.1a.\nFunction: ',
              w05_ex01_1a.__name__, sep='')
        press_continue()
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        raise TypeError('Need int or float for parameter: x.')

    if x > 100:
        return True
    return False


def w05_ex01_1b(y, unit):
    """Use for 1.1b part.

    Parameter 'unit' used as True if to run unit test,
    if False instead 'normal run'.
    If other than int or float used as argument for
    parameter 'y', raises TypeError.
    y == 42
    EC1 == Only number 42 / 42.0 (int or float)
    EC2 == All other numbers (int or float)
    EC1 returns True.
    EC2 returns False.
    """
    if not unit:
        print('This is part 1.1b.\nFunction: ',
              w05_ex01_1b.__name__, sep='')
        press_continue()
    if isinstance(y, bool) or not isinstance(y, (int, float)):
        raise TypeError('Need int or float for parameter: y.')
    if y == 42:
        return True
    return False


def w05_ex01_1c(text, unit):
    """Use for 1.1c part.

    Parameter 'unit' used as True if to run unit test,
    if False instead 'normal run'.
    If other than a type supporting len used as argument for
    parameter 'text', raises TypeError.
    len(text) >= 5
    EC1 == Length of 5 or greater
    EC2 == Length less than 5 (4 to 0)
    EC1 returns True.
    EC2 returns False.
    """
    if not unit:
        print('This is part 1c.\nFunction: ',
              w05_ex01_1c.__name__, sep='')
        press_continue()
    # if isinstance(text, (int, float, bool, complex, type(None))):
    #     raise TypeError('Need parameter of type that '
    #                     'supports len().')
    # if isinstance(text, (range, str, list, tuple, dict, set,
    #                      bytes, bytearray)):
    #     # len(text) >= 5
    #     # EC1 == Length of 5 or greater
    #     # EC0 == Length less than 5 (4 to 0)
    #     if len(text) >= 5:
    #         return True
    #     return False
    # return None
    try:
        return len(text) >= 5
    except TypeError as exc:
        raise TypeError('Need parameter of type that '
                        'supports len().') from exc


def w05_ex01_1d(z, unit):
    """Use for 1.1d part.

    Parameter 'unit' used as True if to run unit test,
    if False instead 'normal run'.
    If other than bool used as argument for
    parameter 'z', raises TypeError.
    z == True
    EC1 == True (Boolean)
    EC2 == False (Boolean)
    EC1 returns True.
    EC2 returns False.
    """
    if not unit:
        print('This is part 1d.\nFunction: ',
              w05_ex01_1d.__name__, sep='')
        press_continue()
    if not isinstance(z, bool):
        raise TypeError('Need bool for parameter: z.')
    if z is True:
        return True
    return False


def w05_ex01_1e(v, unit):
    """Use for 1.1e part.

    Parameter 'unit' used as True if to run unit test,
    if False instead 'normal run'.
    If other than bool used as argument for
    parameter 'z', raises TypeError.
    8 < v < 16
    EC1 == All numbers above 8 and below 16 (int or float)
    EC2 == Numbers (int or float) from 8 and below (inc negative)
    EC3 == Numbers (int or float) from 16 and above
    EC1 returns True.
    EC2 returns False.
    EC3 returns False.
    """
    if not unit:
        print('This is part 1e.\nFunction: ',
              w05_ex01_1e.__name__, sep='')
        press_continue()
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        raise TypeError('Need int or float for parameter: v.')
    if 8 < v < 16:
        return True
    return False


def w05_ex01_1f(w, unit):
    """Use for 1.1f part."""
    if not unit:
        print('This is part 1f.\nFunction: ',
              w05_ex01_1f.__name__, sep='')
        press_continue()
    # w == 32 or w == 64 or w == 128 # EX== 32, 64 or 128
    if w in (32, 64, 128):
        return True
    return False


def w05_ex01_1g(x, unit):
    """Use for 1.1g part."""
    if not unit:
        print('This is part 1g.\nFunction: ',
              w05_ex01_1g.__name__, sep='')
        press_continue()
    if x < 5:
        check_value = 'less_5'
    elif x < 10:
        check_value = 'less10_more5'
    elif x < 15:
        check_value = 'less15_more10'
    else:
        check_value = 'more15'
    return check_value


def run_1_1_a():
    """Use to run separate test of 1.1a."""
    check_1_1_a = w05_ex01_1a(100, False)
    print(check_1_1_a)  # False
    print('\nShould have been False.\n')
    ask_y_or_n()
    check_1_1_a = w05_ex01_1a(101, False)
    print(check_1_1_a)  # True
    print('\nShould have been True.\n')
    ask_y_or_n()
    press_continue()


def run_1_1_b():
    """Use to run separate test of 1.1b."""
    check_1_1_b = w05_ex01_1b(41, False)
    print(check_1_1_b)  # False
    print('\nShould have been False.\n')
    ask_y_or_n()
    check_1_1_b = w05_ex01_1b(42.0, False)
    print(check_1_1_b)  # True
    print('\nShould have been True.\n')
    ask_y_or_n()
    check_1_1_b = w05_ex01_1b(43, False)
    print(check_1_1_b)  # False
    print('\nShould have been False.\n')
    ask_y_or_n()
    press_continue()


def run_1_1_c():
    """Use to run separate test of 1.1c."""
    check_1_1_c = w05_ex01_1c('1234', False)
    print(check_1_1_c)  # False
    print('\nShould have been False.\n')
    ask_y_or_n()
    check_1_1_c = w05_ex01_1c('12345', False)
    print(check_1_1_c)  # True
    print('\nShould have been True.\n')
    ask_y_or_n()
    press_continue()


def run_1_1_d():
    """Use to run separate test of 1.1d."""
    check_1_1_d = w05_ex01_1d(False, False)
    print(check_1_1_d)  # False
    print('\nShould have been False.\n')
    ask_y_or_n()
    check_1_1_d = w05_ex01_1d(True, False)
    print(check_1_1_d)  # True
    print('\nShould have been True.\n')
    ask_y_or_n()
    press_continue()


def run_1_1_e():
    """Use to run separate test of 1.1e."""
    check_1_1_e = w05_ex01_1e(8, False)
    print(check_1_1_e)  # False
    print('\nShould have been False.\n')
    ask_y_or_n()
    check_1_1_e = w05_ex01_1e(16, False)
    print(check_1_1_e)  # False
    print('\nShould have been False.\n')
    ask_y_or_n()
    check_1_1_e = w05_ex01_1e(12, False)
    print(check_1_1_e)  # True
    print('\nShould have been True.\n')
    ask_y_or_n()
    press_continue()


def run_1_1_f():
    """Use to run separate test of 1.1f."""
    check_1_1_f_8 = w05_ex01_1f(8, False)
    check_1_1_f_42 = w05_ex01_1f(42, False)
    check_1_1_f_100 = w05_ex01_1f(100, False)
    check_1_1_f_129 = w05_ex01_1f(129, False)
    check_1_1_f_final = check_1_1_f_8 or check_1_1_f_42 or \
                        check_1_1_f_100 or check_1_1_f_129
    print(check_1_1_f_final)  # False
    print('\nShould have been False.\n')
    ask_y_or_n()
    check_1_1_f_32 = w05_ex01_1f(32, False)
    check_1_1_f_64 = w05_ex01_1f(64, False)
    check_1_1_f_128 = w05_ex01_1f(128, False)
    check_1_1_f_final = check_1_1_f_32 and check_1_1_f_64 and \
                        check_1_1_f_128
    print(check_1_1_f_final)  # True
    print('\nShould have been True.\n')
    ask_y_or_n()


def run_1_1_g():
    """Use to run separate test of 1.1g."""
    print(w05_ex01_1g(4.99, False))
    y_or_n('Did you get less than 5, y or n: ')
    print(w05_ex01_1g(5, False))
    y_or_n('Did you get more than 5 and less than 10, y or n: ')
    print(w05_ex01_1g(10, False))
    y_or_n('Did you get more than 10 and less than 15, y or n: ')
    print(w05_ex01_1g(15, False))
    y_or_n('Did you get more than 15, y or n: ')


def main():
    """Use as main function."""
    print('\nWeek 05, Exercise 01.1, Discuss.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    run_1_1_a()
    run_1_1_b()
    run_1_1_c()
    run_1_1_d()
    run_1_1_e()
    run_1_1_f()
    run_1_1_g()

    press_exit()


if __name__ == "__main__":
    main()
