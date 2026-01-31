"""Module for 'Guess the Number'.

Lesson 02, Week 03, Exercise 05.
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


import random


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit, enter_int_range)


def generate_random_int():
    """Use to generate a random integer."""
    lowest_int = 1 # Lowest int that can be generated
    highest_int = 100 # Highest int that can be generated

    # Generate the random number based on lowest and highest allowed
    random_int = random.randint(lowest_int, highest_int)

    return [random_int, lowest_int, highest_int]


def guess_the_number(secret):
    """Use to guess the secret number."""
    the_secret_one = secret[0]
    lowest = secret[1]
    highest = secret[2]
    ask_str_number = 'Please enter your guess: '

    no_of_guesses = 0

    print(f'Welcome to guess the number!\n'
          f'I am thinking about a number between {lowest} '
          f'and {highest}.\n'
          f'Can you guess which number it is?')
    press_continue()

    while True:
        guess = enter_int_range(ask_str_number, lowest, highest,
                                True)
        no_of_guesses += 1
        print('')
        if guess == the_secret_one:
            print(f'Your guess {guess} is correct!\n'
                  f'You managed it in {no_of_guesses} guesses.')
            break
        if guess < the_secret_one:
            print('No, sorry, that is too low!')
        else:
            print('No, sorry, that is too high!')
        if abs(guess - the_secret_one) <= 5:
            print('However, you are now getting close!')
        press_continue()
        continue


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    """
    print('\nThis is exercise 5, "Guess the Number", '
          'from week 3.')

    press_continue()

    secret_number = generate_random_int()
    guess_the_number(secret_number)

    press_exit()


if __name__ == "__main__":
    main()
