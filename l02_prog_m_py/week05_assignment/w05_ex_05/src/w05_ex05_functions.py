"""Module for Lesson 02, Week 05, Exercise 05.

Functions.
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


def balance_lists(first_list, second_list):
    """Use to check two lists.

    Both inputs shall be lists.
    If the two lists differ more than 1 in length,
    return two balanced lists (order and content not important).
    """
    diff_len_too_long = 2
    # Not a list used for first_list
    if not isinstance(first_list, list):
        return [None, 'first_list is not a list']
    # Not a list used for second_list
    if not isinstance(second_list, list):
        return [None, 'second_list is not a list']
    if abs(len(first_list) - len(second_list)) < diff_len_too_long:
        return first_list, second_list
    # Concatenate the two lists into a temporary list
    temp_list = first_list + second_list
    result_first = []
    result_second = []
    # Create two new lists, with even index in one, odd in the other
    # Should never differ with more than 1 in len after this
    for index, element in enumerate(temp_list):
        if index % 2 == 0:
            result_first.append(element)
        else:
            result_second.append(element)
    return result_first, result_second
