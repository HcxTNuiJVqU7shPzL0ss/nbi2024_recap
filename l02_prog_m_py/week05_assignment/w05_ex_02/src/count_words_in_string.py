"""Module for Lesson 02, Week 05, Exercise 02, part 2.

Part 2.2 function.
See file w05_ex02_functions for "just following the exercise"
version of "easier not as complete" version.
This one here can be considered extensive and very
overworked, used for learning things.
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
                                            enter_string)


def remove_duplicate_spaces(string_in):
    """Use to remove any duplicate spaces in incoming string.

    Will use a stack, named st.
    By duplicate means consecutive, in this case.
    """
    st = []
    n = len(string_in)

    # Traverse through the string
    for i in range(n):
        # Push the character, unless the stack is empty,
        # or the current character is not equal to the
        # top of the stack.
        # If the current character is the same as the top of the
        # stack, do not add it.
        # For this, only care about space, push all else.
        if (string_in[i] == ' ') and (not st or st[-1] != string_in[i]):
            st.append(string_in[i])
        # Do not care about duplicated characters
        # which are not "space".
        elif string_in[i] != ' ':
            st.append(string_in[i])

    # Build the result from the stack
    result_str = ''.join(st) # Stack already maintains order
    return result_str


def count_words_in_sentence(sentence_in):
    """Use to count the number of words in a string.

    Will raise TypeError if input parameter is not of type str.
    Will return ValueError if empty string.
    Several consecutive spaces is only counted once.
    Leading or trailing space(s) not to be counted.
    An input of only space(s) is handled the same as an empty string.
    Space is used to indicate new word.
    Special case if only one word handled as well.
    """
    # Store the function first parameter name from
    # count_words_in_string
    param_name_cnt_words = dir()[0]
    # Do NOT add any variable above the line that contains "dir"

    # Has to have str as type for parameter input argument
    if not isinstance(sentence_in, str):
        wrong_type = type(sentence_in)
        raise TypeError(f'\nNeed a string for parameter: '
                        f'{param_name_cnt_words}.\n'
                        f'What was entered is of type: '
                        f'{wrong_type}')

    # Does not allow an empty string as input
    if not sentence_in:
        raise ValueError('\nThe input string must not be empty.')

    # Skip any repeated spaces
    sentence_in = remove_duplicate_spaces(sentence_in)

    # Do not allow a string with only spaces
    if sentence_in == ' ':
        raise ValueError('\nThe input string must contain at least one '
                         'character, which is not a space.')

    # Remove any leading space
    if sentence_in[0] == ' ':
        sentence_in = sentence_in[1:]

    # Remove any trailing space
    if sentence_in[-1] == ' ':
        sentence_in = sentence_in[:-1]

    cnt_space = sentence_in.count(' ')
    return cnt_space + 1


def run_space_check():
    """Use to get user input as string.

    Count how many "words" have been input, then print this
    information.
    """
    print('You will be asked to input a string.\n'
          'Depending on how may spaces separate non-spaces, '
          'the number of "words" you have entered will be reported.')
    press_continue()
    ask_str = ('Please enter the string where you '
               'want the words counted: ')
    use_to_count_words = enter_string(ask_str)
    no_of_words = count_words_in_sentence(use_to_count_words)
    print(f'\nYour string "{use_to_count_words}" contained '
          f'{no_of_words} separate words.')
