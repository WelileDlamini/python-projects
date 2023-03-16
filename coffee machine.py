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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """return True when can be made"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry,the is no enough water, {item}.")
            return False
        return True
def process_coins():
    """returns the total caluculated from coins inserted"""
    print("please insert coins")
    total = int(input("how many quarters?")) *0.25
    total += int(input("how many dimes?")) * 0.1
    total += int(input("how many nickles?")) *0.05
    total += int(input("how many pennies?")) * 0.01
    return total

def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved>=drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"here is ${change}, in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry thats not enough money. Money refunded.")
        return False




is_on = True
while is_on:
    choice = input("What would you like? (expresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffe: {resources['coffee']}g")
        print(f"Money: {profit}$")
    else:
        drink = MENU
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])

