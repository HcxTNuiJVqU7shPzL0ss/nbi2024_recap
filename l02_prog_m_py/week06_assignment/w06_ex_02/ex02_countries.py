"""Module for 'Countries'.

Lesson 02, Week 06, Exercise 02, parts 1a through 1f.
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
                                            press_exit)


class Country:
    """Use as class to handle values for different countries."""

    def __init__(self, name, pop, area=None):
        """Use when constructing and initializing an object."""
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__language = []

    def add_language(self, lang):
        """Use to add an official language to the country."""
        self.__language.append(lang)

    # Example has other name: print_info for method
    def print_country_information(self):
        """Use to print out country information."""
        print_area_info = ''
        if self.__area is not None:
            print_area_info = (f', the area of the country is '
                               f'{self.__area} km2')
        print(f'In {self.__name} there are {self.__population} '
              f'million inhabitants{print_area_info}.')

        print_language = 'They speak the following language'
        if not self.__language:
            print('No language added for this country.')
        else:
            first_index = self.__language[0]
            last_index = self.__language[-1]
            if len(self.__language) == 1:
                print_language += f':\n{self.__language[0]}'
            else:
                print_language += 's: '
                for lang in self.__language:
                    if lang == first_index:
                        print_language += f'\n{lang}'
                    elif lang != last_index:
                        print_language += f'\n{lang}'
                    else:
                        # print_language += f'\nand\n{lang}'
                        print_language += f'\n{lang}'
            print(print_language)

        press_continue()


def create_country_information():
    """Use to create and store information about countries."""
    se = Country('Sweden', 10.5, 450295)
    no = Country('Norway', 5.5)
    isl = Country('Iceland', 0.4)
    dk = Country('Denmark', 6.0)
    ch = Country('Switzerland', 8.9)
    fi = Country('Finland', 5.6)

    se.add_language('Swedish')

    fi.add_language('Swedish')
    fi.add_language('Finnish')

    ch.add_language('German')
    ch.add_language('French')
    ch.add_language('Italian')
    ch.add_language('Romanch')

    list_of_countries = [se, no, isl, dk, ch, fi]

    for country in list_of_countries:
        Country.print_country_information(country)


def main():
    """Use as module for Main.

    This version made for the recap of 2024.
    Refactored for TAP HT 25D.
    """
    print('\nLesson 02, Week 06, Exercise 02, Countries.')
    press_continue()

    create_country_information()

    print('That was all entered countries.')

    press_exit()


if __name__ == "__main__":
    main()
