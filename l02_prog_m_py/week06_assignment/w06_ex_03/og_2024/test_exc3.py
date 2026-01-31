# pylint: skip-file
# noqa
from exc_3 import *


my_test_acc = Bank()
cash_dep = 50
cash_wit = 10
cash_res = cash_dep - cash_wit
interest = 0.50
cash_int = 60
bill_yes = cash_res


def test_deposit():
    # noqa
    my_test_acc.deposit(cash_dep)
    assert my_test_acc.balance() == cash_dep

def test_withdraw():
    # noqa
    my_test_acc.withdraw(cash_wit)
    assert my_test_acc.balance() == cash_res

def test_balance():
    # noqa
    bal_test_acc = Bank(25)
    assert bal_test_acc.balance() == 25

def test_apply_interest():
    # noqa
    my_test_acc.apply_interest(interest)
    assert my_test_acc.balance() == cash_int

def test_check_bill():
    # noqa
    assert my_test_acc.check_bill(bill_yes) == True
    assert my_test_acc.check_bill(100) == False

