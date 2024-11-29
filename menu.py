class MenuItem:
    """Represents a single drink item on the menu."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """Handles the collection of drink options on the menu."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3.0),
        ]

    def get_items(self):
        """Provides a list of available drink names as a formatted string."""
        return "/".join([item.name for item in self.menu]) + "/"

    def find_drink(self, drink_name):
        """Locates a drink by name and returns the corresponding MenuItem object, if found."""
        for item in self.menu:
            if item.name == drink_name:
                return item
        print("Apologies, we don't serve that drink.")
        return None
