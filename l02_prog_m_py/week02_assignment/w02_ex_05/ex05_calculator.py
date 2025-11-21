"""Module for Lesson 02, Week 02, Exercise 05, Calculator."""


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
                                            press_exit, enter_int)


# CONSTANT PEP8
CRASH_INFO = '\nSomething crashed, check your code!'


def get_int_cnt():
    """Use to get how many integers to add."""
    ask_string = 'Enter a value for how many integers to add: '
    user_cnt = enter_int(ask_string, 0, 0, False)
    return user_cnt


def ask_for_some_ints(no_of_int):
    """Use to request user to input integers."""
    # Version 1 (ask for "three" integers).
    loop_count = no_of_int
    loop_nos = []
    base_string = 'Please input integer number '
    print('\nYou will be asked to input an integer', loop_count, 'times.\n')
    press_continue()
    i = 0
    while i < loop_count:
        send_string = base_string + str(i+1) + ': '
        loop_nos.append(enter_int(send_string, 0, 0, False))
        i += 1
        #print('i:', i)
        #print('loop_nos:', loop_nos)
    return loop_nos


def sum_ints(int_list_sum):
    """Use to add the integers from a list and report the sum."""
    # Version 1 (sum up the integers).
    total_sum = 0
    for value in int_list_sum:
        total_sum += value
    # Sanity check with built-in sum()
    check_sum = sum(int_list_sum)
    if total_sum == check_sum:
        return total_sum
    #else:
    print(CRASH_INFO)
    sys.exit()


def largest_int(int_list_largest):
    """Use to find the largest integer."""
    # Variant 2 (find the largest integer).
    # Smallest possible: -9223372036854775808
    largest = -sys.maxsize - 1
    for value in int_list_largest:
        # pylint: disable=consider-using-max-builtin
        # Part of assignment, have to use it!
        if value > largest:
            largest = value
        # pylint: enable=consider-using-max-builtin
    # Sanity check with built-in max()
    sanity_large = max(int_list_largest)
    if largest == sanity_large:
        return largest
    print(CRASH_INFO)
    sys.exit()


def check_same(int_list_same):
    """Use to check for duplicates in the list."""
    # Version 3
    loop_cnt = len(int_list_same)
    i = 0
    duplicates = 0
    dup_list = []
    orig_list = int_list_same[:]
    while i < loop_cnt:
        j = i
        while j < loop_cnt:
            if i == j:
                j += 1
                continue
            if int_list_same[i] == int_list_same[j]:
                duplicates += 1
                if not int_list_same[i] in dup_list:
                    dup_list.append(int_list_same[i])
                int_list_same[j] = 'd' + str(j)
            j += 1
        i += 1
    if duplicates > 0:
        if len(dup_list) == 1:
            print('\nYes,', str(duplicates), 'duplicates.')
        else:
            print('\nThere are different duplicate numbers.')
        print('The duplicate number(s):', dup_list)
    else:
        print('\nNo duplicates found.')
    print('The list of numbers:', orig_list)
    return orig_list


def check_dupl_if3(nr_list):
    """Use only if three values, check middle value."""
    # Version 4
    # All are the same
    if (nr_list[0] == nr_list[1]) and (nr_list[0] == nr_list[2]):
        middle = nr_list[0]
        mid_check = True
    # Two are the same, index 0 and: 1 or 2
    elif (nr_list[0] == nr_list[1]) or nr_list[0] == nr_list[2]:
        middle = nr_list[0] # As to not have assigned
        mid_check = False
    # Two are the same, index 1 and 2
    elif nr_list[1] == nr_list[2]:
        middle = nr_list[0] # As to not have assigned
        mid_check = False
    # Check which number is middle
    else:
        # Index 0 is middle
        if ((nr_list[0] > nr_list[1]) and (nr_list[0] < nr_list[2])) \
                or ((nr_list[0] < nr_list[1]) and (nr_list[0] > nr_list[2])):
            middle = nr_list[0]
            mid_check = True
        # Index 1 is middle
        elif ((nr_list[1] > nr_list[0]) and (nr_list[1] < nr_list[2])) \
                or ((nr_list[1] < nr_list[0]) and (nr_list[1] > nr_list[2])):
            middle = nr_list[1]
            mid_check = True
        # Index2 is middle
        else:
            middle = nr_list[2]
            mid_check = True
    if mid_check:
        print('\nThe middle value is:', middle)
    else:
        print('\nThere are 2 (not 3) values that are the same.')
    print('')


def run_calculator():
    """Run the program."""
    int_cnt = get_int_cnt()
    numbers_list = ask_for_some_ints(int_cnt)
    #print(numbers_list)
    your_sum = sum_ints(numbers_list)
    big_int = largest_int(numbers_list)

    print('\nYour integers were:', numbers_list, '\n')
    press_continue()
    print('\nYour sum of input integers is:', your_sum, '\n')
    press_continue()
    print('\nThe largest integer entered was:', big_int)

    # Needed to avoid aliasing issue of list in "check same"
    keep_list = check_same(numbers_list)

    # Only run if 3 has been selected
    if int_cnt == 3:
        check_dupl_if3(keep_list)
    else:
        print('\nOnly handle if 3 int was selected '
              'to check for middle.\n')


def main():
    """Use as main function."""
    print('\nWeek 02, Exercise 05, Calculator.\n')
    press_continue()

    run_calculator()

    print('')
    press_exit()


if __name__ == "__main__":
    main()
