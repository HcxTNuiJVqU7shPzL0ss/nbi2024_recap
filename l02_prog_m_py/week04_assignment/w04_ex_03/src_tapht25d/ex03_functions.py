"""Module for functions used in exercise 03, week 04.

Lesson 02, Week 04, Exercise 03.
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


def ex03_01_find_number():
    """Use to find which number brings total above 21.

    Exercise 03, part 01.
    Adding numbers in the series 1 + 2 + 3, and so on.
    Returns the number which brings the sum above 21.
    """
    starting_number = 1
    largest_allowed = 21
    current_number = starting_number
    sum_so_far = 0
    while True:
        for numb in range(2, 100):
            if sum_so_far > largest_allowed:
                number_busting = current_number - 1
                return number_busting
            sum_so_far += current_number
            current_number = numb
