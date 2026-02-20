"""Module for 'Bank'.

Lesson 02, Week 06, Exercise 03.
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
                                            press_exit,
                                            enter_string)


class Bank:
    """Use as class to handle various bank functionality."""

    def __init__(self, cash=0):
        """Use when constructing and initializing an object."""
        self.balance_now = cash

    def deposit(self, plus_money):
        """Use to deposit money."""
        if plus_money > 0:
            self.balance_now += plus_money
        else:
            raise ValueError('Not allowed to deposit negative!')

    def withdraw(self, minus_money):
        """Use to withdraw money."""
        if self.balance_now >= minus_money:
            self.balance_now -= minus_money
        else:
            raise ValueError('Not allowed to withdraw too much!')

    def balance(self):
        """Use to display the current balance."""
        return self.balance_now

    def apply_interest(self, interest):
        """Use to apply interest."""
        if interest >= 0:
            self.balance_now = (
                round((self.balance_now * (1 + interest)), 2))
        else:
            raise ValueError('Negative interest not allowed!')

    def bill_check(self, bill):
        """Use to check if there is money for the bill."""
        if self.balance_now >= bill:
            return True
        return False


def create_account(input_list):
    """Use to create a new account."""
    ask_str = ('Please enter the name of the account holder '
               'for the new bank account: ')
    account_name = enter_string(ask_str)

    input_list.append(account_name)

    input_list[-1] = Bank()


def main():
    """Use as module for Main.

    TAP HT 25D, though done in near time off course, then
    refactored for this week.
    """
    print('\nLesson 02, Week 06, Exercise 03, Bank.')
    press_continue()

    list_of_accounts = []
    create_account(list_of_accounts)
    handle_account = list_of_accounts[-1]
    handle_account.deposit(50)
    check = handle_account.bill_check(100)
    print(check)
    # check_neg = handle_account.deposit(-100)
    # print(check_neg)

    press_exit()


if __name__ == "__main__":
    main()
