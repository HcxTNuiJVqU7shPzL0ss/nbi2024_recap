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


my_account = Bank()
deposit_money = 1000
withdraw_money = 500
diff_money = deposit_money - withdraw_money
interest_percent = 0.1
with_interest = diff_money * (1 + interest_percent)
bill_ok = 100
bill_no = 1500


def test_deposit():
    """Use to test function deposit."""
    assert my_account.balance() == 0
    my_account.deposit(deposit_money)
    assert my_account.balance() == deposit_money


def test_withdraw():
    """Use to test function withdraw."""
    my_account.withdraw(withdraw_money)
    assert my_account.balance() == deposit_money - withdraw_money


def test_balance():
    """Use to test function balance."""
    deposit_other = 42
    other_account = Bank(deposit_other)
    assert other_account.balance() == deposit_other


def test_apply_interest():
    my_account.apply_interest(interest_percent)
    assert my_account.balance() == with_interest


def test_bill_check():
    """Use to test function bill_check."""
    assert my_account.bill_check(bill_ok) == True
    assert my_account.bill_check(bill_no) == False
