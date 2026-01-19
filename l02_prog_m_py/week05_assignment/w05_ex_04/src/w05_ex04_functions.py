"""Module for Lesson 02, Week 05, Exercise 04.

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


from my_funct_dir.my_base_functions import enter_int_range


def select_integers():
    """Prompt user to select the two integers to use."""
    str_for_n = 'Please select the integer for the multiplicand: '
    str_for_limit = 'Please select the integer for the multiplier: '
    low_limit = 1
    high_limit = 10
    use_range = True
    n_int = enter_int_range(str_for_n, low_limit, high_limit,
                            use_range)
    limit_int = enter_int_range(str_for_limit, low_limit,
                                high_limit, use_range)
    return n_int, limit_int


def multiplication_table(n, limit):
    """Use to generate the resulting multiplication table.

    Here n is the "base" multiplicand, while limit is how far to
    go, the multiplier.
    The result shall be the multiplication different results as
    a list, e.g.,
    multiplication_table(3, 4) → [3, 6, 9, 12]
    """
    return_list = []
    # Not an int used for either n, limit, or both
    if not isinstance(n, int):
        return return_list
    if not isinstance(limit, int):
        return return_list
    # Either n, limit or both use 0
    if n == 0 or limit == 0:
        return return_list
    # Either n, limit or both are greater than 10
    if n > 10 or limit > 10:
        return return_list
    ### Calculations below ###
    # Use a simple while loop (version 1)
    cnt = 0
    while cnt < limit:
        cnt += 1
        return_list.append(n * cnt)
    # Use list comprehension (version 2)
    return_list_v2 = [n * value for value in range (1, limit + 1)]
    # Use another type of list comprehension (version 3)
    return_list_v3 = [n * (value + 1) for value in range(limit)]
    if return_list == return_list_v2:
        if return_list_v2 == return_list_v3:
            return return_list
    # This should not be possible
    return None
