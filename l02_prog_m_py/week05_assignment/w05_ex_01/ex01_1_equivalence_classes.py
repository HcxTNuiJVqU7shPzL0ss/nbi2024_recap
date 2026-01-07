"""Module for Lesson 02, Week 05, Exercise 01, Discuss.

Which equivalence classes does the expressions have?
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
                                            press_exit, ask_y_or_n)


def w05_ex01_1a(x, unit):
    """Use for 1.1a part."""
    if not unit:
        print('This is part 1.1a.\nFunction: ',
              w05_ex01_1a.__name__, sep='')
        press_continue()
    # x > 100 # EC == Any number greater than 100
    if x > 100:
        return True
    return False


def w05_ex01_1b(y, unit):
    """Use for 1.1b part."""
    if not unit:
        print('This is part 1b.\nFunction: ',
              w05_ex01_1b.__name__, sep='')
        press_continue()
    # y == 42 # EC == Only number 42
    if y == 42:
        return True
    return False


def w05_ex01_1c(text, unit):
    """Use for 1.1c part."""
    if not unit:
        print('This is part 1c.\nFunction: ',
              w05_ex01_1c.__name__, sep='')
        press_continue()
    # len(text) >= 5 # EC == Length of 5 or greater
    if len(text) >= 5:
        return True
    return False


def w05_ex01_1d(z, unit):
    """Use for 1.1d part."""
    if not unit:
        print('This is part 1d.\nFunction: ',
              w05_ex01_1d.__name__, sep='')
        print('\nShould print out:\n125')
        press_continue()
    # z == True # EC == True (Boolean)
    if z is True:
        return True
    return False


def w05_ex01_1e(v, unit):
    """Use for a.1e part."""
    if not unit:
        print('This is part 1e.\nFunction: ',
              w05_ex01_1e.__name__, sep='')
        press_continue()
    # 8 < v < 16 # EC == 9 through 15
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
    if w == 32 or w == 64 or w == 128:
        return True
    return False


def w05_ex01_1g():
    """Use for 1g."""
    print('This is part 1g.\nFunction: ',
          w05_ex01_1g.__name__, sep='')
    press_continue()


def main():
    """Use as main function."""
    print('\nWeek 05, Exercise 01, Discuss.\nFunction: ',
          main.__name__, sep = '')
    press_continue()


    # check_1_1_a = w05_ex01_1a(100, False)
    # print(check_1_1_a) # False
    # print('\nShould have been False.\n')
    # ask_y_or_n()
    # check_1_1_a = w05_ex01_1a(101, False)
    # print(check_1_1_a)  # True
    # print('\nShould have been True.\n')
    # ask_y_or_n()
    # press_continue()
    #
    #
    # check_1_1_b = w05_ex01_1b(41, False)
    # print(check_1_1_b)  # False
    # print('\nShould have been False.\n')
    # ask_y_or_n()
    # check_1_1_b = w05_ex01_1b(42, False)
    # print(check_1_1_b)  # True
    # print('\nShould have been True.\n')
    # ask_y_or_n()
    # press_continue()


    # check_1_1_c = w05_ex01_1c('1234', False)
    # print(check_1_1_c)  # False
    # print('\nShould have been False.\n')
    # ask_y_or_n()
    # check_1_1_c = w05_ex01_1c('12345', False)
    # print(check_1_1_c)  # True
    # print('\nShould have been True.\n')
    # ask_y_or_n()
    # press_continue()

    # check_1_1_d = w05_ex01_1d('1234', False)
    # print(check_1_1_d)  # False
    # print('\nShould have been False.\n')
    # ask_y_or_n()
    # check_1_1_d = w05_ex01_1d(True, False)
    # print(check_1_1_d)  # True
    # print('\nShould have been True.\n')
    # ask_y_or_n()
    # press_continue()

    # check_1_1_e = w05_ex01_1e(8, False)
    # print(check_1_1_e)  # False
    # print('\nShould have been False.\n')
    # ask_y_or_n()
    # check_1_1_e = w05_ex01_1e(16, False)
    # print(check_1_1_e)  # False
    # print('\nShould have been False.\n')
    # ask_y_or_n()
    # check_1_1_e = w05_ex01_1e(12, False)
    # print(check_1_1_e)  # True
    # print('\nShould have been True.\n')
    # ask_y_or_n()
    # press_continue()

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




    press_exit()


if __name__ == "__main__":
    main()
