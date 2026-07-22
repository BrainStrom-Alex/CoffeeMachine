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

def coins_entry():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return quarters, dimes, nickles, pennies

def coin_calculator(coffee_type, quarters_coin, dimes_coin, nickles_coin, pennies_coin):
    total_money = (quarters_coin*0.25) + (dimes_coin*0.1) + (nickles_coin*0.05) + (pennies_coin*0.01)
    money_left = total_money - MENU[coffee_type]["cost"]
    return money_left, total_money

def money_process():
    print("Please insert coins.")
    output = coins_entry()
    money_output = coin_calculator(initial_input, output[0], output[1], output[2], output[3])
    if money_output[1] > MENU[initial_input]["cost"]:
        print(f"Here is ${round(money_output[0], 2)} in change.")
    total_money_input = money_output[1]
    return total_money_input


def resources_left(coffee_type):

    if coffee_type == "espresso":
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            return True
        else:
            return False

    elif coffee_type == "latte":
        if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
            return True
        else:
            return False

    elif coffee_type == "cappuccino":
        if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
            return True
        else:
            return False

restart = True
while restart:
    initial_input = input("What would you like? (espresso/latte/cappuccino): ")

    if initial_input == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    elif initial_input == "espresso":
        if resources_left(initial_input):
            output = money_process()
            if output >= MENU[initial_input]["cost"]:
                print("Here is your espresso ☕️. Enjoy!")
                money += MENU[initial_input]["cost"]

                resources["water"] -= 50
                resources["coffee"] -= 18
            else:
                print("Sorry that's not enough money. Money refunded.")

        elif not resources_left(initial_input):
            if resources["water"] < 50:
                print("Sorry there is not enough water.")
            if resources["coffee"] < 18:
                print("Sorry there is not enough coffee.")



    elif initial_input == "latte":
        if resources_left(initial_input):
            output = money_process()
            if output >= MENU[initial_input]["cost"]:
                print("Here is your latte ☕️. Enjoy!")
                money += MENU[initial_input]["cost"]

                resources["water"] -= 200
                resources["milk"] -= 150
                resources["coffee"] -= 24
            else:
                print("Sorry that's not enough money. Money refunded.")


        elif not resources_left(initial_input):
            if resources["water"] < 200:
                print("Sorry there is not enough water.")
            if resources["milk"] < 150:
                print("Sorry there is not enough milk.")
            if resources["coffee"] < 24:
                print("Sorry there is not enough coffee.")

        elif initial_input == "cappuccino":
            if resources_left(initial_input):
                output = money_process()
                if output >= MENU[initial_input]["cost"]:
                    print("Here is your cappuccino ☕️. Enjoy!")
                    money += MENU[initial_input]["cost"]

                    resources["water"] -= 250
                    resources["milk"] -= 100
                    resources["coffee"] -= 24
                else:
                    print("Sorry that's not enough money. Money refunded.")

            elif not resources_left(initial_input):
                if resources["water"] < 250:
                    print("Sorry there is not enough water.")
                if resources["milk"] < 100:
                    print("Sorry there is not enough milk.")
                if resources["coffee"] < 24:
                    print("Sorry there is not enough coffee.")

            else:
                if resources["water"] == 0:
                    restart = False
                elif resources["milk"] == 0:
                    restart = False
                elif resources["coffee"] == 0:
                    restart = False

        elif initial_input == "off":
            restart = False
