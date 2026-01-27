"""Module for 'Loops and Lists'.

Lesson 02, Week 03, Exercise 02.
Parts: 1a through 1c, 2 and 3a through 3h.
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


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


def ex_2_1a_for():
    """Use for exercise 2.1, part a.

    Finish the code example, calculate the sum of all numbers from
    1 up to and including 10.
    The answer shall be 55.
    Specifically use a for loop.
    """
    print('This is exercise 2.1 part a.\n'
          'Calculate the sum of integers from 1 to 10.\n'
          'Answer should become: 55.')
    press_continue()
    answer_21a = 0
    for i in range (1, 11):
        answer_21a += i
    print('The sum of the integers 1 to 10 is: ' + str(answer_21a))


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    """
    print('\nThis is exercise 2, "Loops and Lists", from week 3.')
    press_continue()

    ex_2_1a_for()

    press_exit()


if __name__ == "__main__":
    main()
