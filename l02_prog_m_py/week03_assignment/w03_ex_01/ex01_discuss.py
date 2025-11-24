"""Module for Lesson 02, Week 03, Exercise 01, Discuss."""

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


import sys


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit, press_goback)


def ask_y_or_n():
    """Use to ask if yes or no."""
    while True:
        check_01 = input('Did it match/work, (y) yes or (n) no: ')
        a_yes = ('y', '(y)', '(y) yes', 'yes')
        a_no = ('n', '(n)', '(n) no', 'no')
        try:
            if check_01.lower() in a_yes:
                print('\nAwesome!')
                break
            if check_01.lower() in a_no:
                print('\nDarn, must rethink and try again, exit')
                press_exit()
                sys.exit()
        except ValueError:
            print('\nPlease try again.\n')
            press_goback()
            continue


def w03_ex01_part01():
    """Use to run part 01."""
    print('This is part 01 "what will print"?')
    press_continue()
    print('Should be: 5, 7, 9, 11, 13, 15')
    press_continue()

    # Code Start
    limit = 15
    index = 5

    while index <= limit:
        print(index)
        index = index + 2
    # Code End

    print('\nEnd of part 01, did it match?')
    press_continue()

    ask_y_or_n()


def w03_ex01_part02():
    """Use to run part 02."""
    print('This is part 02 "what will print"?')
    press_continue()
    print('Should be: 0, 1, 2, 3, 4, blank new line, '
          '6, 7, 8, 9')
    press_continue()

    # Code Start
    for i in range (10):
        if i == 5:
            print('')
        else:
            print(i)
        i += 1 # PyCharm likes this better
        #i = i + 1 # PyCharm does not like it: Local variable
                        ## 'i' value not used
    # Code End

    print('\nEnd of part 02, did it match?')
    press_continue()

    ask_y_or_n()


def w03_ex01_part03():
    """Use to run part 03."""
    print('This is part 03 "what will print", or '
          '"what is the sum"?')
    press_continue()
    print('Should be: 0 + 0 + 1 + 2 + 3 + 4 + 5 = 15')
    print('\ni.e.:\n15')
    press_continue()

    # Code Start
    counter = 0
    for i in range (6):
        counter += i
    print(counter)
    # Code End

    print('\nEnd of part 03, did it match?')
    press_continue()

    ask_y_or_n()


def w03_ex01_part04():
    """Use to run part 04."""
    print('This is part 04 "what will print"?')
    press_continue()
    print('As of original, nothing will print!')
    print('\nHowever, x should be:\n145')
    x_check = 145
    print('\n... and y should be:\n10')
    y_check = 10
    press_continue()

    # Code Start
    x = 0
    y = 1
    while y < 10:
        if y % 2 == 0:
            x -= y # Tips: sätt en brytpunkt här
        else:
            x += y * y # och här
        y += 1
    # Code End

    # Need this to check
    # x == 0, 1, -1, 8, 4, 29, 23, 72, 64, 145
    print('\nx is:', x)
    # y == 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print('\ny is:', y)
    # Done

    print('\nEnd of part 04, did it match?')
    press_continue()

    if x == x_check and y == y_check:
        ask_y_or_n()
    else:
        print('\nSomething has gone horribly wrong, '
              'check code, exit!')
        sys.exit()


def main():
    """Use as main function."""
    print('\nWeek 03, Exercise 01, Discuss.')
    press_continue()

    #w03_ex01_part01()
    #w03_ex01_part02()
    #w03_ex01_part03()
    w03_ex01_part04()

    press_exit()


if __name__ == "__main__":
    main()
