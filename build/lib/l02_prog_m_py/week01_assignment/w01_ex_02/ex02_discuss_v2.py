"""Module for Lesson 02, Week 01, Exercise 02, Discuss, Version 2."""

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


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit, press_goback)


def calc_funds_left(ticket_price, available_funds):
    """Calculate funds vs ticket price.

    Subtract ticket price from available funds.
    """
    funds_left = available_funds - ticket_price
    return funds_left


def calc_half_left(funds_left):
    """Calculate half of what is left."""
    half_left = funds_left / 2
    return half_left


def enter_ticket_price():
    """Prompt user to input the ticket price."""
    i_ticket_price = 0
    while True:
        s_ticket_price = input('Please enter the ticket '
                               'price (SEK): ')
        try:
            i_ticket_price = int(s_ticket_price)
            if i_ticket_price > 0:
                break
            print('\nNot a positive integer!')
            press_goback()
            continue
        except ValueError:
            print('\nNot valid integer!')
            press_goback()
            continue
    return i_ticket_price


def enter_available_funds():
    """Prompt user to input the available funds."""
    i_av_funds = 0
    while True:
        s_av_funds = input('\nPlease enter the available '
                           'funds (SEK): ')
        try:
            i_av_funds = int(s_av_funds)
            if i_av_funds > 0:
                break
            print('\nNot a positive integer!')
            press_goback()
            continue
        except ValueError:
            print('\nNot valid integer!')
            press_goback()
            continue
    return i_av_funds


def run_w1_ex2(i_ticket_price, i_av_funds):
    """Use to print out the exercise results."""
    i_funds_left = calc_funds_left(i_ticket_price, i_av_funds)

    if i_funds_left < 0:
        print('\nYou cannot afford the ticket!')
    elif i_funds_left == 0:
        print('\nYou have no money left!')
    else:
        i_half_left = calc_half_left(i_funds_left)
        print('\nThere is', i_funds_left, "SEK over.")
        print('Half of what is left over is:', i_half_left,
              'SEK.')

    press_exit()


def main():
    """Use as module for Main."""
    print('\nLesson 02, Week 01, Exercise 02 (version 2).')
    press_continue()

    i_ticket_price = enter_ticket_price()
    i_av_funds = enter_available_funds()
    run_w1_ex2(i_ticket_price, i_av_funds)


if __name__ == "__main__":
    main()
