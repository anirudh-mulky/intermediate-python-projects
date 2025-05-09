from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


on = True

coffee_maker.report()
money_machine.report()

while on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):")
    if choice == "off":
        on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
