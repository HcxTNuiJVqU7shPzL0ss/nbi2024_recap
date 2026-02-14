"""Module for Lesson 02, Week 05, Exercise 1.3, Count vowels.

Update the code and fix it, including tests in separate file.
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
                                            press_exit, enter_string)


def count_vowels(word_in):
    """Count vowels in incoming word."""
    check_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    # vowel = 0
    if not word_in:
        return None
    if isinstance(word_in, str):
        # word_in = word_in.casefold()
        # # pylint: disable=consider-using-generator
        # # For max, min and sum using a generator
        # # is also recommended by pep289.
        # vowel = sum([1 for char in word_in.casefold() if
        #              char in check_vowels])
        # # pylint: enable=consider-using-generator
        vowel = sum(1 for char in word_in.casefold() if
                     char in check_vowels)
        # for char in word_in:
        #     if char.lower() in check_vowels:
        #         vowel += 1
    else:
        vowel = 'incorrect'
    return vowel


def run_count_vowels():
    """Use to create input and handle output.

    Runs function count_vowels.
    """
    print('You will be asked for input, the number of vowels '
          'you entered (English language, y is considered a vowel '
          'for this purpose) will then be presented.\n')

    use_string = enter_string('Enter what to count: ')

    vowels = count_vowels(use_string)

    print(f'\nYou had: {vowels} vowels.')


def main():
    """Use as main function."""
    print('\nWeek 05, Exercise 1.3, Count vowels.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    run_count_vowels()

    press_exit()


if __name__ == "__main__":
    main()
