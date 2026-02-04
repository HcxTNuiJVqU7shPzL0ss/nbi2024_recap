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

    E.g., calling with argument 'hi' for parameter 'echo2_Str'
    will print: 'hihi'.
    Note that assignment calls for a function name of "eko".
    Have used a different name.
    """
    if not isinstance(echo2_str, str):
        return None
    return echo2_str * 2
