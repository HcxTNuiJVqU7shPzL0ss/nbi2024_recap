"""Module for functions used in exercise 01, week 04.

Lesson 02, Week 04, Exercise 01.
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


# 1a
def ex01_01a(t_1a):
    """Use for exercise 01, part 1a.

    Function will always print: test
    The parameter 't_1a' is never used.
    Whenever the function is called, the same resulting
    print of 'test' will happen, regardless what is used
    as argument for 't_1a'.
    """
    print('test')


# 1b
def ex01_01b(x_1b, y_1b):
    """Use for exercise 01, part 1b.

    When called with arguments for the two parameters, assuming
    at least one of them is an int, or both are either int
    or float, will return the multiplied value of the two
    arguments.
    However, for 1b, a print will be done, resulting in:
    3 5
    The function is never called, hence not used.
    """
    return x_1b * y_1b


# 1c
def ex01_01c(x_1c, y_1c):
    """Use for exercise 01, part 1c.

    When called with arguments for the two parameters, assuming
    at least one of them is an int, or both are either int
    or float, will return the multiplied value of the two
    arguments.
    For part 1c calling with (3, 5) will return a value of:
    15
    """
    return x_1c * y_1c


# 1d
def ex01_01d(i_1d):
    """Use for exercise 01, part 1d.

    When called with argument for the parameter will return
    the multiplied value of the argument times 5.
    For part 1d, will first get 5 * 2 = 10,
    next 5 * 3 = 15.
    10 and 15 are added to: 25
    25 is sent into the function as argument to the parameter,
    resulting in 5 * 25 = 125
    """
    return 5 * i_1d


# 1e
def ex01_01e(a_1e):
    """Use for exercise 01, part 1e.

    When called with argument for the parameter will add
    1 to the argument.
    Nothing is however returned from the function, also
    the function is never called.
    """
    a_1e += 1


# 1f
def ex01_01f_oof(i_1f):
    """Use for exercise 01, part 1f.

    When called with argument for the parameter will add
    multiply 2 with argument times the argument.
    This value is then returned.
    This is called with 3 as argument, resulting in:
    2 * 3 * 3 = 18, which is returned.
    """
    return 2 * i_1f * i_1f


def ex01_01f_oog(x_1f, y_1f):
    """Use for exercise 01, part 1f.

    When called with arguments for the parameters, will
    use the first argument as a function call, using the
    second as the input to that function's parameter.
    This is then returned.
    So, calls the oof function, with 3 as the argument
    for that function's parameter.
    18 is the result, then returned.
    """
    return x_1f(y_1f)


# 1g
def ex01_01g_is_number_og(x_1g_og):
    """Use for exercise 01, part 1g, OG.

    When called with argument for the parameter, will
    check if an int, if so return: True.
    Next will check if a float, if so return: True.
    Else, will return False.
    Yes, it can be improved, will do one more function
    for this below.
    """
    if isinstance(x_1g_og, int):
        return True
    elif isinstance(x_1g_og, float):
        return True
    return False


def ex01_01g_is_number_new(x_1g_new):
    """Use for exercise 01, part 1g, New and Improved.

    When called with argument for the parameter, will
    check if an int or a float, if so return: True.
    Else, will return False.
    Has been improved.
    """
    if isinstance(x_1g_new, (int, float)):
        return True
    return False


#### 1h
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found


average_words(["sup", "how's", "it", "going", "reflecting", "on",
               "programs", "and", "coding"])

#### 1i
def find_min(numbers):
    counter = 0
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter


find_min([10, 3, -4, -11])
find_min([])
find_min([100])
