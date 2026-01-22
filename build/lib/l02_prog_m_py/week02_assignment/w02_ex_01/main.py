"""Module for 'Discuss'.

Lesson 02, Week 02, Exercise 01.
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


# Code example:
# is_member = False
# level1 = 100
# level2 = 300
# discount = 0
#
# price = input("Välkommen, köp något dyrt: ")
# price = float(price)
# if price > level1:
#     print("Grattis! Du har avancerat till nivå 1 och
#     får 10% rabatt.")
#     discount = discount + 10
# if price >= level2:
#     print("Grattis! Du har avancerat till nivå 2 och
#     får 25% rabatt.")
#     discount = discount + 25
#
# final_price = price * (100 - discount) / 100
# print("Efter rabatter blir priset.... " + final_price)


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit,
                                            y_or_n,
                                            enter_float)


def check_membership():
    """Use to check for membership or not."""
    ask_member = ('If you are a member, enter y(es), else '
                  'enter n(o): ')
    check_member = y_or_n(ask_member)
    if check_member == 'y':
        return True
    return False


def check_discount(price, member):
    """Use to check member discount."""
    discount = 0
    level_1 = 100
    level_2 = 300
    if member:
        if price >= level_2:
            print('\nCongratulations!\nYou have advanced to level 2 '
                  'and will receive 25% discount!')
            discount += 25
        elif price >= level_1:
            print('\nCongratulations!\nYou have advanced to level 1 '
                  'and will receive 10% discount!')
            discount += 10
    return discount


def check_price():
    """Use to check if to apply discount.

    If the user is a member, a discount is possible.
    Depending on purchase level, either no discount,
    or two different discount levels apply.
    """
    is_member = check_membership()
    ask_price = 'Please enter the price of what you want to buy: '
    print('')
    price_float = enter_float(ask_price)
    discount = check_discount(price_float, is_member)
    if discount == 0:
        print(f'\nThe price (without discount) is '
              f'{price_float:.2f} SEK.')
    else:
        discounted_price = price_float * (100 - discount) / 100
        print(f'\nThe discounted price is '
              f'{discounted_price:.2f} SEK.')


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    Discuss the purpose of the code.
    Test the code for some different values.
    Are there and bugs in the code?
    Are there any logical flaws in the code?
    Discuss potential solutions to bugs/flaws found.
    Discuss potential improvements for the code.
    """
    print('\nThis is exercise 1, "Discuss", from week 2.')
    press_continue()

    check_price()

    press_exit()


if __name__ == "__main__":
    main()
