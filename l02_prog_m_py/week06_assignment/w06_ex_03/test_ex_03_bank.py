"""Module for tests, L02, W06, Ex03."""

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


from .ex_03_bank import Bank


# pylint: disable=too-few-public-methods
class MyValues:
    """Use to handle values."""

    def __init__(self):
        """Use when constructing and initializing an object."""
        self.deposit_money = 1000
        self.withdraw_money = 500
        self.diff_money = self.deposit_money - self.withdraw_money
        self.interest_percent = 0.1
        self.with_interest = (self.diff_money *
                              (1 + self.interest_percent))
        self.bill_ok = 100
        self.bill_no = 1500

    def __str__(self):
        """Use when wanting to print out the parent class name."""
        return self.__class__.__name__
# pylint: enable=too-few-public-methods


my_account = Bank()
the_values = MyValues()


def test_deposit():
    """Use to test function deposit."""
    assert my_account.balance() == 0
    my_account.deposit(the_values.deposit_money)
    assert my_account.balance() == the_values.deposit_money


def test_withdraw():
    """Use to test function withdraw."""
    my_account.withdraw(the_values.withdraw_money)
    assert (my_account.balance() ==
            the_values.deposit_money - the_values.withdraw_money)


def test_balance():
    """Use to test function balance."""
    deposit_other = 42
    other_account = Bank(deposit_other)
    assert other_account.balance() == deposit_other


def test_apply_interest():
    """Use to test function apply_interest."""
    my_account.apply_interest(the_values.interest_percent)
    assert my_account.balance() == the_values.with_interest


def test_bill_check():
    """Use to test function bill_check."""
    assert my_account.bill_check(the_values.bill_ok) is True
    assert my_account.bill_check(the_values.bill_no) is False
