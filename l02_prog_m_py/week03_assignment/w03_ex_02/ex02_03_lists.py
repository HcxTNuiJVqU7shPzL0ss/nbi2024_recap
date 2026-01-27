"""Module for Lesson 02, Week 03, Exercise 02, Part 03: Lists.

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
                       + str(movie_no) + ':\n')
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
    print('\nThe list of movies from part a is:\n' +
          str(part03a_list))
    press_continue()
    return part03a_list


def w03_ex02_part03b(s_error, in_list, add_movie):
    """Use to solve part 03b.

    Add a movie to the end of the list.
    """
    print('Part 03b.\nFunction: ',
          w03_ex02_part03b.__name__, sep='')
    press_continue()
    added_list = in_list
    try:
        added_list.append(add_movie)
    except ValueError:
        print(s_error)
        sys.exit()
    print('b:\nThe movie' + ' "' + add_movie + '" ' +
          'was added to the end.')
    press_continue()
    return added_list


def w03_ex02_part03c(s_error, in_list, add_movie):
    """Use to solve part 03c.

    Add (insert) a movie to the first index [0] of the list.
    """
    print('Part 03c.\nFunction: ',
          w03_ex02_part03c.__name__, sep='')
    press_continue()
    added_list = in_list
    try:
        added_list.insert(0, add_movie)
    except ValueError:
        print(s_error)
        sys.exit()
    print('c:\nThe movie' + ' "' + add_movie + '" ' +
          'was added at index 0.')
    press_continue()
    return added_list


def w03_ex02_part03d(s_error, in_list, check_movie):
    """Use to solve part 03d.

    Check the index of a specific movie.
    """
    print('Part 03d.\nFunction: ',
          w03_ex02_part03d.__name__, sep='')
    press_continue()
    try:
        which_index = in_list.index(check_movie)
    except ValueError:
        print(s_error)
        sys.exit()
    print('d:\nThe movie "' + str(check_movie) + '" is at index:\n'
          + str(which_index))
    press_continue()
    return which_index


def w03_ex02_part03e(s_error, in_list, remove_index):
    """Use to solve part 03e.

    Remove the index position of a specific movie.
    """
    print('Part 03e.\nFunction: ',
          w03_ex02_part03e.__name__, sep='')
    press_continue()
    gone_movie = in_list[remove_index]
    try:
        in_list.pop(remove_index)
    except ValueError:
        print(s_error)
        sys.exit()
    print('e:\nThe movie "' + gone_movie + '" from index',
          str(remove_index), 'is no more.')
    press_continue()


def w03_ex02_part03f(s_error, in_list):
    """Use to solve part 03f.

    Check the length (len) of the list.
    """
    print('Part 03f.\nFunction: ',
          w03_ex02_part03f.__name__, sep='')
    press_continue()
    try:
        print('f:\nThe length of the list is currently:\n' +
              str(len(in_list)))
        press_continue()
    except ValueError:
        print(s_error)
        sys.exit()


def w03_ex02_part03g(s_error, in_list):
    """Use to solve part 03g.

    Reverse the order of the list.
    """
    print('Part 03g.\nFunction: ',
          w03_ex02_part03g.__name__, sep='')
    press_continue()
    print('g:\nThe incoming list looks as so:\n' + str(in_list))
    try:
        in_list.reverse()
        print('g:\nThe now reversed list:\n' +
              str(in_list))
        press_continue()
    except ValueError:
        print(s_error)
        sys.exit()


def w03_ex02_part03h(s_error, in_list):
    """Use to solve part 03h.

    Sort the list in alphabetical order (as of Python).
    """
    print('Part 03h.\nFunction: ',
          w03_ex02_part03h.__name__, sep='')
    press_continue()
    print('h:\nThe incoming list looks as so:\n' + str(in_list))
    try:
        in_list.sort()
        print('h:\nThe now sorted list:\n' +
              str(in_list))
        press_continue()
    except ValueError:
        print(s_error)
        sys.exit()


def main():
    """Use as main function.

    This version made for the recap of 2024.
    """
    print('\nWeek 03, Exercise 02.03, Lists.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    s_ohno = 'Oh no, check your code!'

    # Part 03a, create a list with four movies (as strings)
    movie_list = w03_ex02_part03a(s_ohno)

    # Part 03b, add a movie to the end of the list
    b_string = 'Fellowship of the Ring'
    movie_list_b = w03_ex02_part03b(s_ohno, movie_list, b_string)
    print('b:\n' + str(movie_list_b) + '\n')

    # Part 03c, insert a movie at the first index [0]
    c_string = 'The Two Towers'
    movie_list_c = w03_ex02_part03c(s_ohno, movie_list_b, c_string)
    print('c:\n' + str(movie_list_c))
    press_continue()

    # Part 03d, check the index of a specific movie
    d_index = w03_ex02_part03d(s_ohno, movie_list_c, b_string)

    # Part 03e, remove one of the original four movies.
    # Has the movie from part d a different index?
    movie_index_remove_e = 1
    w03_ex02_part03e(s_ohno, movie_list_c, movie_index_remove_e)
    e_index = w03_ex02_part03d(s_ohno, movie_list_c, b_string)
    print('e:')
    print('"' + b_string + '" was before at index:\n' + str(d_index) + '\n'
          'Now, the index is:\n' + str(e_index))
    try:
        if d_index == e_index:
            print(s_ohno)
            sys.exit()
    except ValueError:
        print('Exception (e)!')
        sys.exit()
    press_continue()

    # Part 03f, check the length (len) of the list.
    w03_ex02_part03f(s_ohno, movie_list_c)

    # Part 03g, reverse the list.
    w03_ex02_part03g(s_ohno, movie_list_c)

    # Part 03h, sort the list.
    w03_ex02_part03h(s_ohno, movie_list_c)

    print('The final list is now:\n' + str(movie_list_c))

    press_exit()


if __name__ == "__main__":
    main()
