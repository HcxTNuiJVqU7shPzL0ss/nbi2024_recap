"""Module for functions used in exercise 02, week 04.

Lesson 02, Week 04, Exercise 02.
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


def ex02_01_hacker(name_str):
    """Use to take a name string input.

    Exercise 02, part 01.
    Will print:
    "<name_str> is a real hacker!"
    If a str is not used as argument, will return None.
    Note that assignment calls for the use of Swedish,
    as well as a function name of "my_function".
    Have used different names, and use English.
    """
    add_str = ' is a real hacker'
    if not isinstance(name_str, str):
        return None
    return name_str + add_str


def ex02_02a_echo_twice(echo2_str):
    """Use to echo an incoming string twice.

    Exercise 02, part 02a.
    E.g., calling with argument 'hi' for parameter 'echo2_Str'
    will print: 'hihi'.
    Note that assignment calls for a function name of "eko".
    Have used a different name.
    """
    if not isinstance(echo2_str, str):
        return None
    return echo2_str * 2


def ex02_02b_echo_multi(echo_multi_str, multiplier):
    """Use to echo an incoming string 'multiplier' number of times.

    Exercise 02, part 02b.
    E.g., calling with argument 'hi' for parameter 'echo_multi_str'
    and '3' for 'multiplier' will print: 'hihihi'.
    Note that assignment calls for a function name of "eko", and
    this to be added to part 02a.
    Have used a different name, and as separate functions all
    together.
    """
    if ((not isinstance(echo_multi_str, str)) or
            (not isinstance(multiplier, int))):
        return None
    return echo_multi_str * multiplier


def ex02_03_end_loop():
    """Use to end the loop of code after 5 times.

    Exercise 02, part 03.
    Adding code and adjusting according to comment.
    Note that assignment calls for use of specific names in the
    code, I have used different names.
    Also, to be able to use unit test without mocking, moving
    the print to a different function, replacing here with a
    return statement instead.
    """
    end_loop_03 = 5
    y_03 = 1
    for x_03 in range(1, 100):
        y_03 *= 2
        # End the loop with an if statement here
        if x_03 == end_loop_03:
            break
    # print(y_03)
    # Shall become 32 (1 = 2, 2 = 4, 3 = 8, 4 = 16, 5 = 32)
    return y_03


def ex02_04_last_element(list_04):
    """Use to display the last element in the supplied list.

    Exercise 02, part 04.
    Take the input list parameter (list_04) and return the last
    element of the list.
    Note that assignment calls specifically for the function to
    be named 'last'.
    Have taken creative decision to change this.
    If anything but a list, or an empty list, is sent as argument
    during the function call, will return: None.
    """
    if (not isinstance(list_04, list)) or (not list_04):
        return None
    return list_04[-1]


def ex02_05_cut_edges(list_05):
    """Use to cut the edges of the parameter list.

    Exercise 02, part 05.
    Take the input list parameter (list_05), remove the first and
    the last element, return the new list without these removed
    elements.
    Note that assignment calls specifically for the function to
    be named 'cut_edges'.
    Have done some changes to this name.
    If anything but a list, an empty list, or a list with less than
    three (3) is sent as argument during the function call,
    will return: None.
    """
    if ((not isinstance(list_05, list)) or (not list_05) or
            (len(list_05) < 3)):
        return None
    # Use 'copy()' to make a copy of the list, then edit it
    # Ensure the original list stays unchanged
    copy_list_05 = list_05.copy()
    copy_list_05.pop(0) # Remove the first element
    copy_list_05.pop(-1) # Remove the last element
    # Use list slicing to make a copy of the list, then edit it
    sliced_list = list_05[1:-1] # From index 1, not including last
    if copy_list_05 == sliced_list:
        return copy_list_05
    return False # Safeguard if something went horribly wrong


def ex02_06_increase(x_06):
    """Use to increase input parameter (x_06) by 1.

    Exercise 02, part 06.
    Takes one parameter as input, increase it by one (1) and
    then returns the result.
    Note that assignment calls for the function to be called
    'increase' and the input parameter as 'x', I have decided
    to make changes to this.
    Also, the assignment calls for fixing the code, this has
    been done.
    If invalid argument input to parameter, returns None.
    """
    if not isinstance(x_06, (int, float)):
        return None
    x_06 += 1
    return x_06
