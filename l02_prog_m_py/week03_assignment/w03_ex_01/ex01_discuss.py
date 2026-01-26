"""Module for Discuss.

Lesson 02, Week 03, Exercise 01,
Done "off course".
"""

#####################################################################
# Copyright 2025-2026 gnoff
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
                                            press_exit,
                                            ask_y_or_n)


# pylint: disable=duplicate-code
def w03_ex01_part01():
    """Use to run part 01."""
    print('This is part 01 "what will print"?\nFunction: ',
          w03_ex01_part01.__name__, sep = '')
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
    print('This is part 02 "what will print"?\nFunction: ',
          w03_ex01_part02.__name__, sep = '')
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
          '"what is the sum"?\nFunction: ',
          w03_ex01_part03.__name__, sep = '')
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
    print('This is part 04 "what will print"?\nFunction: ',
          w03_ex01_part04.__name__, sep = '')
    press_continue()
    print('As of original, nothing will print!')
    print('\nHowever, x should be:\n145')
    x_check = 145
    print('\n... and y should be:\n10')
    y_check = 10
    press_continue()

    # Nothing in stated code will print anything!
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


def w03_ex01_part05():
    """Use to run part 05."""
    print('This is part 05 "what will print"?\nFunction: ',
          w03_ex01_part05.__name__, sep = '')
    press_continue()
    print('Should be: _tim')
    print('i.e., from index 3, up to, but not including, '
          'index 7.')
    press_continue()

    # Code Start
    message = 'its_time_to_get_coding'
    print(message[3:7])
    # Code End

    print('\nEnd of part 05, did it match?')
    press_continue()
    ask_y_or_n()

    # Print "time", version 1
    print('\nNow to instead select index [4:8], '
          'so it becomes: time')
    press_continue()
    print(message[4:8])
    print('')
    ask_y_or_n()

    # Print "time", version 2
    first_index = message.find('_')
    second_index = message.find('_', first_index+1)
    print('\nVersion 2, still to print: time')
    press_continue()
    print(message[first_index+1:second_index], '\n')
    ask_y_or_n()


def w03_ex01_part06():
    """Use to run part 06."""
    print('This is part 06 "what will print"?\nFunction: ',
          w03_ex01_part06.__name__, sep = '')
    press_continue()
    print('Outer loop goes 1 through 6.')
    print('Inner loop goes 1 through 8.')
    print('Inner loop will build s to first print:\n'
          '#.......')
    print('Outer loop + inner will then print a line '
          'where for each time the hash has moved one '
          'step to the right, a total of 6 lines.')
    press_continue()

    # Code Start
    for y in range(1, 7):
        s = ''
        for x in range(1, 9):
            if x == y:
                s += '#'
            else:
                s += '.'
        print(s)
    # Code End

    print('\nEnd of part 06, did it match?')
    press_continue()
    ask_y_or_n()

    print('\nSecond part: Can you move the line one step to '
          'the right?')
    print('Do not really follow what is meant by this description.')
    print('If the idea is to start with a space, then the same as '
          'before, init s to a space.')
# pylint: enable=duplicate-code


def main():
    """Use as main function.

    This version made for the recap of 2024.
    """
    print('\nWeek 03, Exercise 01, Discuss.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    w03_ex01_part01()
    w03_ex01_part02()
    w03_ex01_part03()
    w03_ex01_part04()
    w03_ex01_part05()
    w03_ex01_part06()

    press_exit()


if __name__ == "__main__":
    main()
