class CoffeeMaker:
    """Simulates a coffee machine that brews drinks."""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Displays the current levels of all available resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Checks if there are enough resources to prepare the selected drink."""
        for ingredient, amount_required in drink.ingredients.items():
            if amount_required > self.resources.get(ingredient, 0):
                print(f"Sorry, there isn't enough {ingredient}.")
                return False
        return True

    def make_coffee(self, order):
        """Uses the required resources to prepare the drink and updates the resource levels."""
        for ingredient, amount_used in order.ingredients.items():
            self.resources[ingredient] -= amount_used
        print(f"Enjoy your {order.name}! ☕️")
