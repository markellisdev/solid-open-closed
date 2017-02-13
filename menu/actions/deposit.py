from . import menuaction


# Polymorphism via sub-typing
class Deposit(menuaction.MenuAction):
    def __init__(self, account):
        self.account = account

    def __call__(self):
        amount = input("How much? ")
        self.account.add_money(amount)
