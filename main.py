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