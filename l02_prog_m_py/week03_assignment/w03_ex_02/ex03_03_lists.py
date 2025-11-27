"""Module for Lesson 02, Week 03, Exercise 02, Part 03: Lists."""

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


import sys


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit, press_goback)


def w03_ex02_part03a(s_error):
    """Use to solve part 03a.

    Create a list with the names of four movies (as
    strings), print the entire list.
    """
    print('Part 03a.\nFunction: ',
          w03_ex02_part03a.__name__, sep = '')
    print('\nYou will input four movie names.')
    press_continue()
    part03a_list = []
    i = 0
    while i < 4:
        movie_no = i + 1
        in_str = input('Please enter the name of movie number '
                       + str(movie_no) + '.\n')
        try:
            if len(in_str) > 0:
                part03a_list.append(in_str)
                i += 1
            else:
                print('\nNot enough characters!')
                press_goback()
                continue
        except ValueError:
            print(s_error)
            sys.exit()
    print('\nThe list of movies from part a is:', part03a_list)
    return part03a_list


def main():
    """Use as main function."""
    print('\nWeek 03, Exercise 02.03, Lists.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    s_ohno = 'Oh no, check your code!'

    # Part 03a, create a list with four movies (as strings)
    movie_list = w03_ex02_part03a(s_ohno)
    print(movie_list)

    press_exit()


if __name__ == "__main__":
    main()
