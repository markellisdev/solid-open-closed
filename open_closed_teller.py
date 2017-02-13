from bank import *
from menu.actions.deposit import Deposit
from menu.actions.withdraw import Withdraw
from menu.actions.balance import ShowBalance
from menu.menubuilder import MenuBuilder
from menu.menuitem import MenuItem

class Teller():
    """This class is the interface to a customer's bank account"""

    def __init__(self):
        # Using composition to establish relationship between the bank 
        # and the teller, as well as the teller and the CLI menu that 
        # serves as the UI
        self.account = BankAccount()
        self.menu = MenuBuilder()

    def build_menu(self):
        """Defines each of the MenuActions that will be used for the Teller"""

        deposit = MenuItem("Add Money", Deposit(self.account))
        
        # Add a single menu item (ad hoc polymorphism)
        self.menu.add(menu_item=deposit)

        withdraw = MenuItem("Withdraw Money", Withdraw(self.account))
        balance = MenuItem("Show Balance", ShowBalance(self.account))
        quitter = MenuItem("Quit", exit)

        # Add a list of menu items (ad hoc polymorphism)
        self.menu.add(menu_items=[withdraw, balance, quitter])

        self.menu.show()
