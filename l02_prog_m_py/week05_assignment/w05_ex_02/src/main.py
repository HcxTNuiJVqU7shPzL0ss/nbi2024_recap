"""Module for Lesson 02, Week 05, Exercise 02.

Parts 2.1 through 2.4, file for main.py.
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
from w05_ex02_functions import c_to_f
# pylint: enable=import-error


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


def main():
    """Use as main function."""
    print('\nWeek 05, Exercise 02, Function calls.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    check32 = c_to_f(0)
    print(check32)

    press_exit()


if __name__ == "__main__":
    main()
