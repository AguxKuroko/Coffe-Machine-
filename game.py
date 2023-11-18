from main import MENU, resources

def coin_check(choice_drink, cost):
    # Prompt the user to input the number of each coin
    quarters = int(input(f"How many quarters for {choice_drink}? "))
    dimes = int(input(f"How many dimes for {choice_drink}? "))
    nickels = int(input(f"How many nickels for {choice_drink}? "))
    pennies = int(input(f"How many pennies for {choice_drink}? "))

    # Calculate the total money inserted by the user
    total_money_inserted = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

    # Check if the total money inserted is enough for the selected drink
    if total_money_inserted >= cost:
        return total_money_inserted
    else:
        print(f"That's not enough. Money refunded")
        return 0
def make_coffee(choice_drink, cost, total_money_inserted):
    # Check if the user inserted enough money for the selected coffee
    if total_money_inserted > 0:
        # Calculate and print the change, then display the order
        change = total_money_inserted - cost
        order = f"Here is your change ${round(change, 4)}.\nHere is your {choice_drink} ☕️. Enjoy!"
        print(order)
        return True
    else:
        return False
def update_resources(name_drink):
    # Update the resources based on the ingredients of the selected drink
    ingredients = MENU[name_drink]["ingredients"]

    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount
def print_report(total_money_inserted):
    # Print a report of the current resources and the total money inserted
    print("\nReport:")
    for key, value in resources.items():
        if key == "coffee":
            print(f"{key.capitalize()}: {value} gr")
        else:
            print(f"{key.capitalize()}: {value} ml")

    print(f"Coins: ${round(total_money_inserted, 4)}")

print("Hi! I will take your order for a drink")

flag = True
total_money_inserted = 0  # Initialize total_money_inserted outside the loop
while flag:
    user_choice = input('What would you like? (espresso/latte/cappuccino/report):')

    if user_choice == "report":
        print_report(total_money_inserted)
        #flag = False
    elif user_choice in ["espresso", "latte", "cappuccino"]:
        cost = MENU[user_choice]["cost"]
        print("Please insert coins")
        money_for_coffee = coin_check(user_choice, cost)

        if make_coffee(user_choice, cost, money_for_coffee):
            total_money_inserted += money_for_coffee
            update_resources(user_choice)
    else:
        print("Invalid choice. Please enter espresso, latte, cappuccino, or report.")
