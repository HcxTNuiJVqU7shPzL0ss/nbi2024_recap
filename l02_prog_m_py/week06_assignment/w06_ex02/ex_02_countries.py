"""Module for 'Countries'.

Lesson 02, Week 06, Exercise 02, parts 1a through 1f.
Done "off course".
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


class Country:
    """Use as class to handle values for different countries."""

    def __init__(self, name, pop):
        """Use when constructing and initializing an object."""
        self.__name = name
        self.__population = pop

    # Example has name: print_info for method
    def print_country_information(self):
        """Use to print out country information."""
        print(f'In {self.__name} there are {self.__population} '
              f'million inhabitants.')


def create_country_information():
    """Use to create and store information about countries."""
    se = Country('Sweden', 10.5)
    no = Country('Norway', 5.5)
    isl = Country('Iceland', 0.4)
    dk = Country('Denmark', 6.0)

    list_of_countries = [se, no, isl, dk]

    for country in list_of_countries:
        Country.print_country_information(country)


def main():
    """Use as module for Main.

    This version made for the recap of 2024.
    """
    print('\nLesson 02, Week 06, Exercise 02, Countries.')
    press_continue()

    create_country_information()

    press_exit()


if __name__ == "__main__":
    main()
