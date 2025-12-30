"""Module for Lesson 02, Week 04, Exercise 02.

Practice using functions and modules.
"""

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


# pylint: disable=import-error
# from ex02_functions import my_function_2_1
# from ex02_functions import eko_2a
# from ex02_functions import eko_2b
from ex02_functions import my_function_2_3
# pylint: disable=enable


from my_funct_dir.my_base_functions import (press_exit,
                                            press_continue)#,
                                            # enter_string,
                                            # enter_int_range)


def main():
    """Use as main function."""
    print('\nWeek 04, Exercise 02, Functions and Modules.'
          '\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    # # Part 01
    # name_02_01 = 'What is your name: '
    # use_name_02_01 = enter_string(name_02_01)
    # my_function_2_1(use_name_02_01)

    # # Part 02a
    # echo_string_2a = enter_string('Please enter what to echo: ')
    # eko_2a(echo_string_2a)

    # # Part 02b
    # echo_string_2b = enter_string('Please enter what to echo: ')
    # cnt_string = 'Please enter how many times to echo: '
    # echo_cnt_2b = enter_int_range(cnt_string, 3, 10, True)
    # eko_2b(echo_string_2b, echo_cnt_2b)

    # Part 03
    my_function_2_3()


    press_exit()


if __name__ == "__main__":
    main()
