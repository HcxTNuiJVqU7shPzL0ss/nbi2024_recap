"""Module for 'Variables and data types'.

Lesson 02, Week 01, Exercise 03, Parts: 1a, 1b, 2a and 2b.
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


# pylint: disable=import-error
from ex03_02b import special_discount_text
# pylint: enable=import-error


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit,
                                            enter_int_range,
                                            enter_int)


def ex3_1_integers():
    """Use as module for part 1a and 1b of Exercise 3.

    Use "input" to request user for two integers, save the input
    in variables, change into integers, sum up, print the result.
    """
    print('\nThis is part 1a, enter an integer.')
    press_continue()
    ask_str_1a = 'Please enter an integer: '
    first_int = enter_int(ask_str_1a)
    if first_int == 42:
        print('\nI see you also like the magic number!')
        press_continue()
    print(f'\nYour entered integer for 1a is: {first_int}.')
    press_continue()

    print('\nThis is part 1b, enter a second integer.')
    press_continue()
    ask_str_1b = 'Please enter one more integer: '
    second_int = enter_int(ask_str_1b)
    if second_int == 42:
        print('\nI see you also like the magic number!')
        press_continue()
    print(f'\nYour entered integer for 1b is: {second_int}.\n')
    print(f'The sum of your two integers '
          f'{first_int} and {second_int} is: '
          f'{first_int + second_int}')
    press_continue()


def ex_3_2a_jacket_discount_75():
    """Use as module for part 2a of Exercise 3.

    Calculate the price of a jacket with OG price of 2000 SEK,
    that is now on discount with 75% off.
    """
    jacket_og_price = 2000
    discount_percent = 75.0
    print('\nThis is part 2a, display the discounted price.')
    press_continue()
    sell_price = (jacket_og_price -
                  (jacket_og_price * discount_percent / 100))
    print(f'The list price was {jacket_og_price} SEK and the '
          f'discount was {int(discount_percent)}%.')
    print(f'Your price for the jacket is {sell_price:.2f} SEK.')
    press_continue()


def ex_3_2b_jacket_discount_user_set():
    """Use as module for part 2b of Exercise 3.

    Calculate the price of a jacket with OG price of 2000 SEK,
    that is now on discount set by the user input.
    """
    print('\nThis is part 2b, set the discount percentage.')
    press_continue()

    jacket_og_price = 2000
    discount_string = 'Enter a discount as integer (in %): '

    discount = enter_int_range(discount_string, 0, 100, True)

    sell_price = jacket_og_price - (jacket_og_price * discount / 100)

    print(f'\nThe list price was: {jacket_og_price} SEK.')
    print(f'The discount was: {discount}%.')
    print(f'Your price for the jacket is {sell_price:.2f} SEK.')

    special_discount_text(discount)


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    """
    ex3_1_integers()
    ex_3_2a_jacket_discount_75()
    ex_3_2b_jacket_discount_user_set()
    press_exit()


if __name__ == "__main__":
    main()
