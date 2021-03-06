from sys import exit

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

money = 0
total = 0
coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}


def required(choice):
    """This checks if the resources available cover the requested coffee. Returns True if resources sufficient else,
    RETURNS False """
    for key in MENU[choice]["ingredients"]:
        if resources[key] < MENU[choice]["ingredients"][key]:
            print(f"Sorry there isn't enough {key}")
            return False
    return True


def coffee():
    """the main function used to start the coffee machine process"""
    global total
    global money
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "random":
        for key in resources:
            print(f"{key} : {resources[key]}")
        print(f"money : {money}")
        coffee()
    elif choice == "off":
        exit()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if required(choice):
            print("Please insert coins")
            for key in coins:
                total += int(input(f"How many {key}? ")) * coins[key]
            change = total - MENU[choice]["cost"]
            money += MENU[choice]["cost"]
            total = 0
            if change < 0:
                print("Sorry that's not enough money. Money refunded")
                coffee()
            else:
                for key in MENU[choice]["ingredients"]:
                    resources[key] -= MENU[choice]["ingredients"][key]
                print(f"Here is ${round(change, 1)} in change")
                print(f"Here is your {choice} ☕ Enjoy!")
                coffee()
        else:
            coffee()


coffee()
