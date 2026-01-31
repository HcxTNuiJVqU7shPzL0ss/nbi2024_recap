# pylint: skip-file
# noqa


class Bank:
    # noqa
    def __init__(self, cash = 0):
        # noqa
        self.current_balance = cash

    def deposit(self, cash):
        # noqa
        self.current_balance += cash

    def withdraw(self, cash):
        # noqa
        self.current_balance -= cash

    def balance(self):
        # noqa
        return self.current_balance

    def apply_interest(self, cash):
        # noqa
        if cash >= 1:
            print(f"\nInterest to be presented as decimals, {cash} is not likely!")
            return
        mult_interest = 1 + cash
        self.current_balance = round((self.current_balance * mult_interest), 2)

    def check_bill(self, cash):
        # noqa
        if self.current_balance > cash:
            print("\nGood news! You can afford to pay that bill!")
            return True
        else:
            print("\nHaha, you do not have enough! Call Lyxfällan!")
            return False
"""
acc = Bank()

acc.deposit(50)
print(acc.current_balance)

acc.withdraw(25)
print(acc.current_balance)

my_bal = acc.balance()
print(my_bal)

acc.apply_interest(1.10)
print(acc.current_balance)

acc.apply_interest(0.10)
print(acc.current_balance)

afford = acc.check_bill(2.50)
if afford:
    pass
else:
    print("For your own good, lets exit!")
    quit()

afford = acc.check_bill(50)
if afford:
    pass
else:
    print("For your own good, lets exit!")
    quit()
"""