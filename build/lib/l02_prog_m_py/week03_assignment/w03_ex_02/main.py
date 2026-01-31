"""Module for 'Loops and Lists'.

Lesson 02, Week 03, Exercise 02.
Parts: 1a through 1c, 2 and 3a through 3h.
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


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


def ex_2_1a_for():
    """Use for exercise 2.1, part a.

    Finish the code example, calculate the sum of all numbers from
    1 up to and including 10.
    The answer shall be 55.
    Specifically use a for loop.
    """
    print('This is exercise 2.1 part a.\n'
          'Calculate the sum of integers from 1 to 10.\n'
          'Answer should become: 55.')
    press_continue()
    answer_21a = 0
    for i in range (1, 11):
        answer_21a += i
    print('The sum of the integers 1 to 10 is: ' + str(answer_21a))
    press_continue()


def ex_2_1b_for():
    """Use for exercise 2.1, part b.

    Calculate the sum of all numbers between 1 and 100,
    including 1 and 100, which should be 5050.
    Specifically use a for loop.
    """
    print('This is exercise 2.1 part b.\n'
          'Calculate the sum of integers from 1 to 100.\n'
          'Answer should become: 5050.')
    press_continue()
    answer_21b = 0
    for i in range(1, 101):
        answer_21b += i
    print('The sum of the integers 1 to 100 is: ' + str(answer_21b))
    press_continue()


def ex_2_1c_while():
    """Use for exercise 2.1, part c.

    Apply the same idea as in part 1b, though instead of
    using a for loop, specifically use a while loop.
    """
    print('This is exercise 2.1 part c.\n'
          'Calculate the sum of integers from 1 to 100.\n'
          'Answer should become: 5050.')
    press_continue()
    answer_21c = 0
    i = 1
    while i < 101:
        answer_21c += i
        i += 1
    print('The sum of the integers 1 to 100 is: ' + str(answer_21c))
    press_continue()


def ex_2_2_sumup_list():
    """Use for exercise 2.2.

    Calculate the sum of all the elements in the list:
    [1, -2, 3, -2, 4, -3]
    """
    print('This is exercise 2.2.\n'
          'Calculate the sum of integers in the specified list.\n'
          'Control by head count and calculator should give: 1.')
    press_continue()
    list_of_int = [1, -2, 3, -2, 4, -3]
    sum_of_list = 0
    for i in list_of_int:
        sum_of_list += i
    print(f'The sum of the integers in the list is: {sum_of_list}.')
    press_continue()


def ex_2_3_list_of_movies():
    """Use for exercise 2.3.

    Create and then perform various actions on a list.
    a) Create and print a list with the names (str) of four movies.
    b) Add the movie "Fellowship of the Ring" at the last position.
    c) Add "The Two Towers" at index 0 (first).
    d) Find which index "Fellowship of the Ring" is at now.
    e) Remove another movie, check if "Fellowship" changed index.
    f) Use len() to find the length of the list.
    g) Turn the list into reverse order.
    h) Sort the list alphabetically.
    """
    print('This is exercise 2.3.\n'
          'Create and manipulate a list of movies.')
    press_continue()

    # Part 3a
    movie_list = ['Spaceballs', 'The Shawshank Redemption',
                  'Avatar', 'Bad Taste']

    print('Part 3a.\nThe list has been created, containing strings '
          'which has the names of movies, four in total.\n\n'
          'The movies are:\n')
    for movie in movie_list:
        print(movie)
    press_continue()

    # Part 3b
    movie_list.append('Fellowship of the Ring')

    print('Part 3b.\n"Fellowship of the Ring" has been added to '
          'the end of the list.\n\n'
          'The movies are now:\n')
    for movie in movie_list:
        print(movie)
    press_continue()

    # Part 3c
    movie_list.insert(0, 'The Two Towers')

    print('Part 3c.\n"The Two Towers" has been added to '
          'the first position of the list.\n\n'
          'The movies are now:\n')
    for movie in movie_list:
        print(movie)
    press_continue()

    # Part 3d
    print(f'Part 3d.\n"Fellowship of the Ring" has changed position '
          f'in the list (due to 3c).\n\n'
          f'The new index of that movie is: '
          f'{movie_list.index('Fellowship of the Ring')}.')
    press_continue()

    # Part 3e
    removed_movie_3e = movie_list[3]
    movie_list.pop(3)

    print(f'Part 3e.\nOne movie has been removed from the list '
          f'({removed_movie_3e}).\nSince "Fellowship" was at the '
          f'last position in the list, it has yet again changed, '
          f'it is now at index: '
          f'{movie_list.index('Fellowship of the Ring')}.')
    press_continue()

    # Part 3f
    print(f'Part 3e.\nThe length of the list '
          f'(how many movies are in it) is currently: '
          f'{len(movie_list)}.')
    press_continue()

    # Part 3g
    movie_list.reverse()

    print('Part 3g.\nThe list has been reversed.\n\n'
          'The movies are now in the following order:\n')
    for movie in movie_list:
        print(movie)
    press_continue()

    # Part 3h
    movie_list.sort()

    print('Part 3h.\nThe list has been sorted alphabetically.\n\n'
          'The movies are now in the following order:\n')
    for movie in movie_list:
        print(movie)
    press_continue()

    print('That was it for exercise 2.3, goodbye.')


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    """
    print('\nThis is exercise 2, "Loops and Lists", from week 3.')
    press_continue()

    # Part 1 a, b and c
    ex_2_1a_for()
    ex_2_1b_for()
    ex_2_1c_while()

    # Part 2
    ex_2_2_sumup_list()

    # Part 3
    ex_2_3_list_of_movies()

    press_exit()


if __name__ == "__main__":
    main()
