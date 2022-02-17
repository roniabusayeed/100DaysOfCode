MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def print_report(res):
    """"Prints a report of the resources available and profits made"""
    print(f"Water: {res['water']} ml")
    print(f"Milk: {res['milk']} ml")
    print(f"Coffee: {res['coffee']} g")
    print(f"Money: ${profit}")


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def deduct_resources(order_ingredients):
    """Deducts amounts of water, milk and coffee from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


def process_coins():
    """
    Receives number of Quarters, Dimes, Nickels and Pennies from user and returns
    total monetary value
    """
    print("Please insert coins.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    return quarters * .25 + dimes * .1 + nickels * .05 + pennies * .01


is_on = True


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report(resources)
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            paid_amount = process_coins()
            if paid_amount < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                profit += drink["cost"]
                if paid_amount > drink["cost"]:
                    print(f"Here is ${round(paid_amount - drink['cost'], 2)} dollars in change.")
                deduct_resources(drink["ingredients"])
                print(f"Here is your {choice}. Enjoy!")
