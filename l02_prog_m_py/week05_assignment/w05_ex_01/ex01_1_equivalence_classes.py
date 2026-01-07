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
    if z is True:
        return True
    return False


def w05_ex01_1e():
    """Use for 1e."""
    print('This is part 1e.\nFunction: ',
          w05_ex01_1e.__name__, sep='')
    print('\nShould print out:\n7')
    press_continue()


def w05_ex01_1f():
    """Use for 1f."""
    print('This is part 1f.\nFunction: ',
          w05_ex01_1f.__name__, sep='')
    print('\nShould print out:\n18')
    press_continue()


def w05_ex01_1g():
    """Use for 1g."""
    print('This is part 1g.\nFunction: ',
          w05_ex01_1g.__name__, sep='')
    print('\nShould print out:\nTrue\nTrue')
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

    check_1_1_d = w05_ex01_1d('1234', False)
    print(check_1_1_d)  # False
    print('\nShould have been False.\n')
    ask_y_or_n()
    check_1_1_d = w05_ex01_1d(True, False)
    print(check_1_1_d)  # True
    print('\nShould have been True.\n')
    ask_y_or_n()
    press_continue()




    press_exit()


if __name__ == "__main__":
    main()
