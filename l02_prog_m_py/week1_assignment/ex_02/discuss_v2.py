"""Module for 'Discuss', version 2."""


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


def press_exit():
    """Use to prompt user to hit enter to exit."""
    input('Press Return (Enter) to exit.\n')


def calc_funds_left(ticket_price, available_funds):
    """Calculate funds vs ticket price.

    Subtract ticket price from available funds."""
    funds_left = available_funds - ticket_price
    return funds_left


def calc_half_left(funds_left):
    """Calculate half of what is left."""
    half_left = funds_left / 2
    return half_left


# Prompt user to input the ticket price
while True:
    s_ticket_price = input('\nPlease enter the ticket price (SEK): ')
    i_ticket_price = 0
    try:
        i_ticket_price = int(s_ticket_price)
        if i_ticket_price > 0:
            break
        else:
            print('\nNot a positive integer!')
            continue
    except ValueError:
        print('\nNot valid integer!')
        continue


# Prompt user to input the available funds
while True:
    s_av_funds = input('\nPlease enter the available funds (SEK): ')
    i_av_funds = 0
    try:
        i_av_funds = int(s_av_funds)
        if i_av_funds > 0:
            break
        else:
            print('\nNot a positive integer!')
            continue
    except ValueError:
        print('\nNot valid integer!')
        continue


i_funds_left = calc_funds_left(i_ticket_price, i_av_funds)

if i_funds_left < 0:
    print('\nYou cannot afford the ticket!\n')
elif i_funds_left == 0:
    print('\nYou have no money left!')
else:
    i_half_left = calc_half_left(i_funds_left)
    print('\nThere is', i_funds_left, "SEK over.")
    print('Half of what is left over is:', i_half_left , '\n')


press_exit()
