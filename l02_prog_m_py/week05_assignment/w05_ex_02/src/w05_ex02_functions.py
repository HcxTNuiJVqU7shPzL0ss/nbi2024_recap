"""Module for Lesson 02, Week 05, Exercise 02.

Parts 2.1 through 2.4, functions.
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


def c_to_f(degree):
    """Use to convert degree Celsius to Fahrenheit.

    Will return None if input is less than
    the absolute zero.
    Note this will not handle input that differ from int or float.
    Going by exercise for this, will not add difficulty or
    functionality at this time.
    """
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32


def count_words(sentence):
    """Use to count the number of words in a sentence (string).

    Will return None if empty string.
    Will return False if non-string input.
    Space is used to indicate new word.
    Several consecutive spaces is only counted ones.
    Leading or trailing space not to be counted.
    An input of only space(s) is handles the same as an empty string.
    """
    latest_char = ''
    reduced_sentence = ''
    if not isinstance(sentence, str):
        return False # Not a sentence used as input
    if not sentence:
        return None # Empty sentence used as input
    for char in sentence:
        if char == ' ' and latest_char == ' ':
            continue # Skips any repeated space(s)
        reduced_sentence += char
        latest_char = char
    if reduced_sentence[0] == ' ':
        # Skips any leading space (more than one handled previously)
        reduced_sentence = reduced_sentence[1:]
    if not reduced_sentence:
        return None # Only leading space(s) used as input
    if reduced_sentence[-1] == ' ':
        # Skips any trailing space (more than one handled previously)
        reduced_sentence = reduced_sentence[:-1]

    cnt_space = reduced_sentence.count(' ')
    return cnt_space + 1


def find_median(numbers):
    """Use to find the median from a list of numbers.

    Will return None if empty list.
    Will return False if non-list or non-number (in list) input.
    """
    if not isinstance(numbers, list):
        return False # Not a list used as input
    if not all(isinstance(item, (int, float)) for item in numbers):
        return False # List, but includes item(s) not int nor float
    if not numbers:
        return None # Empty list
    # Find the length of the list
    list_length = len(numbers)
    if list_length < 2:
        return None  # List too short, not enough numbers
    # Sort the list from smallest to highest value (ascending)
    numbers.sort()
    # Handle if odd number of list elements
    if list_length % 2 != 0:
        median_index = list_length // 2
        return numbers[median_index]
    # Handle if even number of list elements
    first_mid_index = list_length // 2 - 1
    second_mid_index = list_length // 2
    median_odd_value = (numbers[first_mid_index] +
                        numbers[second_mid_index]) / 2
    return median_odd_value


def is_sorted_ascending(numbers):
    """Use to check if list is sorted as ascending or not.

    If the list "numbers" is sorted ascending, returns
    True, else False.
    Will return None if empty list, or if non-list or
    non-number (in list) input.
    """
    if not isinstance(numbers, list):
        return None # Not a list used as input
    if not all(isinstance(item, (int, float)) for item in numbers):
        return None # List, but includes item(s) not int nor float
    if not numbers:
        return None # Empty list
    list_copy = numbers[:]
    list_copy.sort()
    if list_copy == numbers:
        return True
    return False
