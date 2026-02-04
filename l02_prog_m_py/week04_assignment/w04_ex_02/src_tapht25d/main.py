"""Module for 'Functions and Modules'.

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
from ex02_extra_calls import (ex02_part01_add_name,
                              ex02_part02a_add_echo_str,
                              ex02_part02b_echo_str_multiplier,
                              ex02_part3_print_after_loop)
# pylint: enable=import-error


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    Practice functions and modules.
    """
    print('\nThis is exercise 2, "Functions and Modules", '
          'from week 4.')
    press_continue()

    # Part 1
    ex02_part01_add_name()

    # Part 2, a
    ex02_part02a_add_echo_str()

    # Part 2, b
    ex02_part02b_echo_str_multiplier()

    # Part 3
    ex02_part3_print_after_loop()

    press_exit()


if __name__ == "__main__":
    main()
