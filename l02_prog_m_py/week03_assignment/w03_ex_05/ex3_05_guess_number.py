"""Module for Lesson 02, Week 03, Exercise 05.

Guess the number.
"""

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


import random


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit,
                                            enter_int)


def rando_num():
    """Use to generate a random integer between 1 and 100."""
    print('\nGenerate random number.\nFunction: ',
          rando_num.__name__, sep='')
    secret = random.randint(1, 100)
    return secret


def enter_and_guess(answer):
    """Use to get a guess from the user and check against random."""
    print('\nGuess the number.\nFunction: ',
          enter_and_guess.__name__, sep='')
    in_string = 'Please enter your guess: '
    close_string = 'You are getting close!'
    no_of_guesses = 0
    guess_list = []
    print('\nWelcome to guess the number!')
    print('I am thinking about a number between 1 and 100.')
    print('Can you guess which one it is?\n')
    while True:
        if no_of_guesses > 0:
            print('\nGuessed to far:', guess_list, '\n')

        guess = enter_int(in_string)
        guess_list.append(guess)
        no_of_guesses += 1
        print('\nGuess: ' + str(guess) + '\n')
        if guess == answer:
            print('Yes! You did it!')
            print('You made it in ' + str(no_of_guesses) + ' guesses.')
            break
        if guess > answer:
            print('No, that is too high!')
            guess_list.append('High')
            # Version 2
            if (guess - answer) <= 5:
                print(close_string)
                guess_list.append('Close')
            press_continue()
            continue
        if answer > guess:
            print('No, that is too low!')
            guess_list.append('Low')
            # Version 2
            if (answer - guess) <= 5:
                print(close_string)
                guess_list.append('Close')
            press_continue()
            continue


def main():
    """Use as main function."""
    print('\nWeek 03, Exercise 05, Guess the number.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    # Get the random number
    correct = rando_num()

    # Guess and check until correct
    enter_and_guess(correct)


    press_exit()


if __name__ == "__main__":
    main()
