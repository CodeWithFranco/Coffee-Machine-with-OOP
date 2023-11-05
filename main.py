"""
Author: Franco Nepomuceno
Title: Coffee Machine with OOP
Description: Utilizing object-oriented-programming rather procedural-programming
Date: November 23, 2023
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# object = blueprint
money = MoneyMachine()
coffee = CoffeeMaker()
selection = Menu()

product_on = True
while product_on:
    # get_items() Gets all available items for sale separated by '/', This is coming from Menu() class.
    # available_beverages is a 'str' variable.
    available_beverages = selection.get_items()
    # print(available_beverages)
    user_input = input(f'What is your order? These are your choices: {available_beverages}\n').lower()
    if user_input == 'off':
        product_on = False
    elif user_input == 'report':
        # prints "report money" from MoneyMachine() class and "ingredients" from CoffeeMaker() class
        # object.method
        print(money.report())
        print(coffee.report())
    else:
        """
        selection(object).find_drink(function inside 'Menu' class)(order_name input)
        This line transfers 'menu.MenuItem' object at a memory location
        """
        kind_of_coffee = selection.find_drink(user_input)
        # print(kind_of_coffee)
        if coffee.is_resource_sufficient(kind_of_coffee):
            """
            Above: Returns 'True' if ingredients are enough for 'kind_of_coffee'
            Below: object.method('menu.MenuItem' object.attribute)
            """
            if money.make_payment(kind_of_coffee.cost):
                coffee.make_coffee(kind_of_coffee)
