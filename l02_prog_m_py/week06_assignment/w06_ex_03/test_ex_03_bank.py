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


import pytest


from .ex_03_bank import Bank


# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes
class MyValues:
    """Use to handle values."""

    def __init__(self):
        """Use when constructing and initializing an object."""
        self.deposit_money = 1000
        self.not_allowed_deposit = -1
        self.withdraw_money = 500
        self.diff_money = self.deposit_money - self.withdraw_money
        self.interest_percent = 0.1
        self.with_interest = (self.diff_money *
                              (1 + self.interest_percent))
        self.bill_ok = 100
        self.bill_no = 1500
# pylint: enable=too-few-public-methods
# pylint: enable=too-many-instance-attributes


my_account = Bank()
the_values = MyValues()


def test_balance__nothing_deposited():
    """Test that initial balance is 0."""
    assert my_account.balance() == 0


def test_balance__add_at_start():
    """Use to check with initial value.

    If an account is created with an initial value,
    this is available without deposit.
    """
    initial_value = 50
    start_account = Bank(initial_value)
    assert start_account.balance() == initial_value


def test_deposit__add_money():
    """Use to test function deposit.

    Adding money works.
    """
    my_account.deposit(the_values.deposit_money)
    assert my_account.balance() == the_values.deposit_money


def test_deposit__negative_value():
    """Use to test you are not allowed a negative deposit value."""
    with pytest.raises(ValueError):
        my_account.deposit(the_values.not_allowed_deposit)


def test_withdraw__take_money():
    """Use to test function withdraw.

    Take money works.
    """
    my_account.withdraw(the_values.withdraw_money)
    assert (my_account.balance() ==
            the_values.deposit_money - the_values.withdraw_money)


def test_withdraw_take_too_much():
    """Use to test you cannot withdraw more than available."""
    too_much = my_account.balance() + 1
    with pytest.raises(ValueError):
        my_account.withdraw(too_much)


def test_balance__separate_account():
    """Use to test function balance.

    This will use a separate account only for this test.
    """
    deposit_other = 42
    other_account = Bank(deposit_other)
    assert other_account.balance() == deposit_other


def test_apply_interest__positive():
    """Use to test function apply_interest.

    Add a positive interest and check result.
    """
    my_account.apply_interest(the_values.interest_percent)
    assert my_account.balance() == the_values.with_interest


def test_apply_interest__zero_interest():
    """Use to check that 0 interest doesn't change balance."""
    zero_interest = 0
    current_balance = my_account.balance()
    my_account.apply_interest(zero_interest)
    new_balance = my_account.balance()
    assert current_balance == new_balance


def test_apply_interest__negative():
    """Use to chck negative interest not allowed."""
    neg_interest = -0.001
    with pytest.raises(ValueError):
        my_account.apply_interest(neg_interest)


def test_bill_check__true_and_false():
    """Use to test function bill_check.

    Both that you can afford and not afford a bill.
    """
    assert my_account.bill_check(the_values.bill_ok) is True
    assert my_account.bill_check(the_values.bill_no) is False
