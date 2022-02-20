from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

should_continue = True
while should_continue:
    order_name = input(f"What would you like? ({menu.get_items()}): ")
    if order_name == "off":
        should_continue = False
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_name)
        if drink and coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
