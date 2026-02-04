"""Module for extra function calls used in exercise 02, week 04.

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


# pylint: disable=import-error
from ex02_functions import (ex02_01_hacker, ex02_02a_echo_twice)
# pylint: enable=import-error


from my_funct_dir.my_base_functions import (press_continue,
                                            enter_string)


def ex02_part01_add_name():
    """Use to add name for exercise 04 part 01."""
    print('This is part 01 from exercise 02.\n'
          'Your entered name will be added to a string that '
          'will print.')
    press_continue()
    ask_str = 'Please enter your name: '
    entered_name = enter_string(ask_str)
    final_string = ex02_01_hacker(entered_name)
    print(f'\n{final_string}')
    press_continue()


def ex02_part02a_add_echo_str():
    """Use to echo incoming string twice.

    To call function and handle printout for exercise 04 part 2a.
    """
    print('This is part 02 a, from exercise 02.\n'
          'Your entered string will be echoed twice, this '
          'will then print.')
    press_continue()
    ask_str_echo = 'Please enter what to echo: '
    echo_text = enter_string(ask_str_echo)
    echoed_for_print = ex02_02a_echo_twice(echo_text)
    print(f'\n{echoed_for_print}')
    press_continue()
