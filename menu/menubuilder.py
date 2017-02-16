import os
from .menuitem import MenuItem

"""This class is open for anyone to use"""
class MenuBuilder():
    """Responsible for building a command line menu system from MenuItems"""

    def __init__(self):
        self.__menu = list()

    # Ad hoc polymorphism (i.e. method overloading)
    def add(self, menu_item=None, menu_items=None):
        if menu_items is not None:
            self.__menu.extend(menu_items)
        elif menu_item is not None:
            self.__menu.append(menu_item)

    def show(self):
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')

        # Display each menu item
        for index, menu_item in enumerate(self.__menu):
            if type(menu_item) is MenuItem:
                print("{}. {}".format(index+1, menu_item.prompt))

        try:
            # Accept user choice
            choice = int(input(">> "))

            # Invoke the class corresponding to the choice
            for menu_item in self.__menu:
                if choice == self.__menu.index(menu_item) + 1:
                    menu_item.action()

        # Handle ctrl+c
        except KeyboardInterrupt:
            exit()

        # Handle any invalid choice by ignoring it
        except ValueError:
            pass

        # Display the MenuItems
        self.show()
