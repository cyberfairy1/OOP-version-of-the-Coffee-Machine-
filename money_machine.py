class MoneyMachine:
    """Handles monetary transactions for the coffee machine."""
    
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Displays the total profit earned."""
        print(f"Total Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Calculates the total value of coins inserted by the user."""
        print("Please insert coins:")
        for coin, value in self.COIN_VALUES.items():
            count = int(input(f"How many {coin}? "))
            self.money_received += count * value
        return self.money_received

    def make_payment(self, cost):
        """Checks if the inserted money covers the cost and processes the transaction."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Insufficient funds. Money refunded.")
            self.money_received = 0
            return False

