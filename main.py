from menu import MENU, resources


def coffee_machine():
    coffee_machine_working = True
    while coffee_machine_working:
        refund = "Sorry, not enough money. Money will be refunded."
        quarter_value = 0.25
        dime_value = 0.10
        nickel_value = 0.05
        penny_value = 0.01
        cost_of_espresso = MENU['espresso']['cost']
        cost_of_latte = MENU['latte']['cost']
        cost_of_cappuccino = MENU['cappuccino']['cost']

        def report():
            """Prints amount of resources left."""
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
            print(f"Money: ${format(resources['money'], '.2f')}")

        def refill(water, milk, coffee):
            """Update amount of resources."""
            resources['water'] += water
            resources['milk'] += milk
            resources['coffee'] += coffee

        def sufficient_resources(water, milk, coffee):
            """Check if resources are sufficient."""
            espresso = MENU['espresso']['ingredients']
            latte = MENU['latte']['ingredients']
            cappuccino = MENU['cappuccino']['ingredients']

            if water < espresso['water'] or water < latte['water'] or water < cappuccino['water']:
                print("Sorry, there is not enough water.\nPlease refill water.")
                reboot = input("Reboot coffee machine now? Type 'y': ").lower()
                if reboot == 'y':
                    coffee_machine()
            elif milk < espresso['milk'] or milk < latte['milk'] or milk < cappuccino['milk']:
                print("Sorry, there is not enough milk.\nPlease refill milk.")
                reboot = input("Reboot coffee machine now? Type 'y': ").lower()
                if reboot == 'y':
                    coffee_machine()
            elif coffee < espresso['coffee'] or coffee < latte['coffee'] or coffee < cappuccino['coffee']:
                print("Sorry, there is not enough coffee.\nPlease restock coffee.")
                reboot = input("Reboot coffee machine now? Type 'y': ").lower()
                if reboot == 'y':
                    coffee_machine()

        def use_resources(selection):
            """Deduct required ingredients from resources."""
            resources['water'] -= MENU[selection]['ingredients']['water']
            resources['milk'] -= MENU[selection]['ingredients']['milk']
            resources['coffee'] -= MENU[selection]['ingredients']['coffee']

        def cost(choice):
            """Prints cost of selection: espresso, latte or cappuccino."""
            if choice == 'e':
                print(f"That'll be ${format(cost_of_espresso, '.2f')}.\nPlease insert coins.")
            elif choice == 'l':
                print(f"That'll be ${format(cost_of_latte, '.2f')}.\nPlease insert coins.")
            elif choice == 'c':
                print(f"That'll be ${format(cost_of_cappuccino, '.2f')}.\nPlease insert coins.")

        users_choice = input("What would you like? Espresso, Latte or Cappuccino?\nType 'e', 'l' or 'c': ").lower()
        if users_choice == 'report':
            report()
            exit_report = input("Exit report? Type 'y': ").lower()
            if exit_report == 'y':
                continue
        elif users_choice == 'refill':
            print("Before refill:")
            report()
            refill_water = int(input("Refill with how much water?(in ml): "))
            refill_milk = int(input("Refill with how much milk?(in ml): "))
            refill_coffee = int(input("Restock with how much coffee?(in g): "))
            refill(refill_water, refill_milk, refill_coffee)
            print("After refill:")
            report()
            exit_refill = input("Exit refill? Type 'y': ").lower()
            if exit_refill == 'y':
                continue
        elif users_choice == 'e' or users_choice == 'l' or users_choice == 'c':
            sufficient_resources(resources['water'], resources['milk'], resources['coffee'])

        def process_amount(amount_of_quarters, amount_of_dimes, amount_of_nickles, amount_of_pennies):
            """Calculates total value of users coins."""
            quarters_total = float(amount_of_quarters) * quarter_value
            dimes_total = float(amount_of_dimes) * dime_value
            nickles_total = float(amount_of_nickles) * nickel_value
            pennies_total = float(amount_of_pennies) * penny_value
            money_from_user = quarters_total + dimes_total + nickles_total + pennies_total
            return money_from_user

        def transaction(choice, users_money):
            """Check if transaction is successful. If successful, deducts ingredients and updates money."""
            if choice == 'e':
                if users_money >= cost_of_espresso:
                    print(f"Your total amount: ${format(users_money, '.2f')}.")
                    print(f"You get ${format(round(users_money - cost_of_espresso, 2), '.2f')} in change.")
                    print("Here is your espresso ☕  Enjoy!")
                    resources['money'] += cost_of_espresso
                    use_resources('espresso')
                else:
                    print(refund)
            elif choice == 'l':
                if users_money >= cost_of_latte:
                    print(f"You get ${format(round(users_money - cost_of_latte, 2), '.2f')} in change.")
                    print("Here is your latte ☕  Enjoy!")
                    resources['money'] += cost_of_latte
                    use_resources('latte')
                else:
                    print(refund)
            elif choice == 'c':
                if users_money >= cost_of_cappuccino:
                    print(f"You get ${format(round(users_money - cost_of_cappuccino, 2), '.2f')} in change.")
                    print("Here is your cappuccino ☕  Enjoy!")
                    resources['money'] += cost_of_cappuccino
                    use_resources('cappuccino')
                else:
                    print(refund)

        cost(users_choice)
        quarters = input("How many quarters?: ")
        dimes = input("How many dimes?: ")
        nickles = input("How many nickles?: ")
        pennies = input("How many pennies?: ")
        transaction(users_choice, process_amount(quarters, dimes, nickles, pennies))


coffee_machine()
