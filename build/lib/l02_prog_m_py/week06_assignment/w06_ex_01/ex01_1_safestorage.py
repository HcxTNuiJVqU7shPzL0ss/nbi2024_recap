"""Module for 'Discuss'.

Lesson 02, Week 06, Exercise 01, part 1.
What does the code do?
TAP HT 25D, though done in near time off course, then
refactored for this week.
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
                                            press_exit,
                                            ask_y_or_n)


# What does the following code do?
class SafeStorage:
    """Class used for storing and retrieving data."""

    def __init__(self):
        """Use when constructing an object and initializing data."""
        self.__data = None # Non-public variable ("private")

    def get(self):
        """Use as method to get data that is stored in variable."""
        return self.__data

    def put(self, data):
        """Use as method to store data in variable."""
        self.__data = data

    def __del__(self):
        """Use to highlight if an object gets destroyed."""
        print(f'The following data just got destroyed:\n'
              f'{self.__data}')


def main():
    """Use as module for Main.

    This version made for the recap of 2024.
    Refactored for TAP HT 25D.
    """
    print('\nLesson 02, Week 06, Exercise 01, part 1.')
    press_continue()

    print('The program will print out:\n'
          'Anakonda Boarom')
    press_continue()

    safe = SafeStorage()  # New instance / object of the class
    safe.put('Anakonda')  # Put Anakonda in data for safe
    x = safe.get()  # Grab data (Anakonda) and place in variable x
    safe.put('Boaorm')  # Overwrite earlier data with Boaorm
    y = safe.get()  # Grab data (Boarom) and place in variable y
    print(x, y, '\n')  # Print both == Anakonda Boarom

    ask_y_or_n()

    # Yes, I got the result I had figured out

    press_exit()


if __name__ == "__main__":
    main()
