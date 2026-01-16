"""Module for 'Hello World'.

Lesson 02, Week 01, Exercise 01.
Done "off course".
"""

#####################################################################
# Copyright 2025-2026 gnoff
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


def main():
    """Use as module for Main.

    This version made for the recap of 2024.
    """
    print('\nLesson 02, Week 01, Exercise 01.')
    press_continue()

    my_name = 'Jan (gnoff)'

    # Print "Hello world"
    print('Hello world')

    # Print a welcome message
    print(f'This program was made by {my_name}.')

    press_exit()


if __name__ == "__main__":
    main()
