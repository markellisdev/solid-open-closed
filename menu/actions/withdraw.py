from . import menuaction


# Polymorphism via sub-typing
class Withdraw(menuaction.MenuAction):
    def __init__(self, account):
        self.account = account

    def __call__(self):
        amount = input("How much? ")
        self.account.withdraw_money(amount)
