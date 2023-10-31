from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

continue_brewing = True
while continue_brewing:
    user_selection = input('What would you like? (espresso/latte/cappuccino)\n').lower()
    if user_selection == 'off':
        continue_brewing = False
    elif user_selection == 'report':
        machine_report = CoffeeMaker()
        # print object and methods
        print(machine_report.report())



