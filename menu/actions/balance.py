import os
from . import menuaction


# Polymorphism via sub-typing
class ShowBalance(menuaction.MenuAction):
    def __init__(self, account):
        self.account = account

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n   Your balance is: {}\n\n\n\n".format(self.account.show_balance()))
        input(">> Press enter to continue <<")
