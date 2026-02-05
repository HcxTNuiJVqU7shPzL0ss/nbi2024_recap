"""Functions for Lesson 02, Week 04, Exercise 02."""

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


from my_funct_dir.my_base_functions import (press_continue,
                                            press_goback,
                                            press_exit,
                                            enter_string,
                                            enter_int,
                                            enter_int_range)


def my_function_2_1(in_name):
    """Use for exercise 02, part 01."""
    add_string = ' is a real hacker'
    print('\n' + in_name + add_string)


def ex01():
    """Use to run exercise 01."""
    print('This is exercise 01.\n')
    name_02_01 = 'What is your name: '
    use_name_02_01 = enter_string(name_02_01)
    my_function_2_1(use_name_02_01)
    print('\nEnd of part 01.')
    press_continue()


def eko_2a(in_string):
    """Use to echo incoming string."""
    # print(in_string + in_string)
    print(in_string*2)


def ex02a():
    """Use to run exercise 02a."""
    print('This is exercise 02a.\n')
    echo_string_2a = enter_string('Please enter what to echo: ')
    eko_2a(echo_string_2a)
    print('\nEnd of part 02a.')
    press_continue()


def eko_2b(in_string, count):
    """Use to echo incoming string count number of times."""
    print('\n' + in_string * count)


def ex02b():
    """Use to run exercise 02a."""
    print('This is exercise 02b.\n')
    echo_string_2b = enter_string('Please enter what to echo: ')
    cnt_string = 'Please enter how many times to echo: '
    echo_cnt_2b = enter_int_range(cnt_string, 3, 10, True)
    eko_2b(echo_string_2b, echo_cnt_2b)
    print('\nEnd of part 02b.')
    press_continue()


def my_function_2_3():
    """Use for exercise 02, part 03."""
    # Loop 5 times, should print out: 32.
    end = 5
    y = 1
    for x in range(1, 100):
        y *= 2
        # avsluta loopen med en if-sats här
        if x == end:
            break
    print(y)


def ex03():
    """Use to run exercise 03."""
    print('This is exercise 03.\n')
    my_function_2_3()
    print('\nEnd of part 03.')
    press_continue()


def last(in_list_04):
    """Use to return the last element of the list parameter."""
    return in_list_04[-1]


def ex04():
    """Use to run exercise 04."""
    print('This is exercise 04.\n')
    return_04 = last([1, 2, 3])
    print(return_04)
    print('\nEnd of part 04.')
    press_continue()


def cut_edges(in_list_05):
    """Use to return the list without the first and last element."""
    internal_list = in_list_05
    internal_list.pop(0)
    internal_list.pop(-1)
    return internal_list


def ex05():
    """Use to run exercise 05."""
    print('This is exercise 05.\n')
    return_05 = cut_edges([0, 1, 2, 3])
    print(return_05)
    print('\nEnd of part 05.')
    press_continue()


def increase(x):
    """Use to increase x by 1 and return the result."""
    x += 1
    return x


def ex06():
    """Use to run exercise 06."""
    print('This is exercise 06.\n')
    print(increase(1))
    print('\nEnd of part 06.')
    press_continue()


def average(x, y):
    """Use to return the average value of the two parameters."""
    aver_value_07 = (x + y) / 2
    return aver_value_07


def ex07():
    """Use to run exercise 07."""
    print('This is exercise 07.\n')
    result_07 = average(4, 8)
    print(result_07)
    print('\nEnd of part 07.')
    press_continue()


def pretty_list(in_list_08):
    """Use for exercise 08."""
    if len(in_list_08) == 0:
        print('\nYour list is empty.')
    else:
        for i, index in enumerate(in_list_08):
            print(f'{i + 1}. {index}')


def ex08():
    """Use to run exercise 07."""
    print('This is exercise 08.\n')
    pretty_list(['a', 'b', 3.14])
    print('\nEnd of part 08.')
    press_continue()


def run_w04_ex02():
    """Use to run week 04 exercise 02."""
    exercises = ['ex01', 'ex02a', 'ex02b', 'ex03', 'ex04', 'ex05',
                'ex06', 'ex07', 'ex08', 'all', 'quit']
    ex_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    exc = [ex01, ex02a, ex02b, ex03, ex04, ex05, ex06, ex07, ex08]
    while True:
        print('Available exercises to run are:\n')
        for i, ex in enumerate(exercises):
            print(f'{i}: {ex}')
        print('')
        run_one = enter_int('Select which exercise to run: ')
        print('')
        if run_one not in ex_numbers:
            print('\nNot valid!')
            press_goback()
            continue
        if run_one == 10:
            print('Goodbye!')
            press_exit()
            break
        if run_one == 9:
            for i, func in enumerate(exc):
                func()
        else:
            exc[run_one]()
