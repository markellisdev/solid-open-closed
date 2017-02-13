import os
from bank import *


class Teller():
  """This class is the interface to a customer's bank acccount"""

  def __init__(self):
    self.account = BankAccount()

  def build_menu(self):
    """Construct the main menu items for the command line user interface"""

    # Clear the console first
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print all the options
    print("1. Add money")
    print("2. Withdraw money")
    print("3. Show balance")
    print("4. Quit")

  def main_menu(self):
    """Show teller options"""

    # Build the menu
    self.build_menu()

    # Wait for user input
    choice = input(">> ")

    # Perform the appropriate actions corresponding to user choice
    if choice == "1":
      deposit = input("How much? ")
      self.account.add_money(deposit)

    if choice == "2":
      withdrawal = input("How much? ")
      self.account.withdraw_money(withdrawal)

    if choice == "3":
      print(self.account.show_balance())
      input()

    # If the user chose anything except Quit, show the menu again
    if choice != "4":
      self.main_menu()


if __name__ == "__main__":
  teller = Teller()
  teller.main_menu()
