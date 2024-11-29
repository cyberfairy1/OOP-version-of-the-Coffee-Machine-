from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize the system components
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_running = True

while machine_running:
    # Display drink options
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    
    if choice == "off":
        # Turn off the machine
        machine_running = False
        print("Shutting down the coffee machine. Goodbye!")
    elif choice == "report":
        # Show current resource and profit reports
        coffee_maker.report()
        money_machine.report()
    else:
        # Process drink order if valid
        drink = menu.find_drink(choice)
        if drink and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

