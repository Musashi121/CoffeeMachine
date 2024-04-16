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

def print_report():
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: ${profit}')


def check_resources(ingredient_dict):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in ingredient_dict:
        if ingredient_dict[item] > resources[item]:
            print(f"Sorry! There is not enough {item}")
            return False
        else:
            return True


def process_coins():
    print("Please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction_successful(coins_paid, drink_cost):
    if coins_paid >= drink_cost:
        change = round(coins_paid - drink_cost, 2)
        print(f"Here is {change} in change.")
        global profit
        profit += coins_paid
        return True
    else:
        print("Sorry! That is not enough! Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name}. Enjoy!")


machine_on = True

while machine_on:
    choice = input("What would you like? (Espresso/Latte/Cappuccino? )").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print_report()
    else:
        if choice not in MENU:
            print("Stop wasting my time, kiddo.")
            continue
        cust_drink = MENU[choice]
        if check_resources(cust_drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, cust_drink["cost"]):
                make_coffee(choice, cust_drink["ingredients"])


