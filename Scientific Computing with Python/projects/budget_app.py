"""
Complete the Category class. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list.
"""

class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        display = f"{'*' * 15}{self.category}{'*' * 15}"
        display += '\n'

        for ledge in self.ledger:
            # print(ledge)
            display += f"{ledge['description']}   {ledge['amount']}"
            display += '\n'

        return display
    
    """
    The class should also contain the following methods:

    1 - A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    """

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        
    """
    2 - A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
    """

    def withdraw(self, amount, description=''):
        can_transfer = self.check_funds(amount)

        if can_transfer:
            self.ledger.append({"amount": amount * -1, "description": description})

            return True
        return False
    
    """
    3 - A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    """

    def get_balance(self):
        return sum(ledge['amount'] for ledge in self.ledger)
    
    """
    4 - A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
    """

    def transfer(self, amount, destination):
        can_transfer = self.check_funds(amount)
        
        if can_transfer:
            self.withdraw(amount, f"Transfer to {destination.category}")
            destination.deposit(amount, f"Transfer from {self.category}")

            return True
        return False
    
    """
    A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
    """

    def check_funds(self, amount):
        balance = self.get_balance()

        if amount > balance:
            return False
        return True

food_cat = Category("Food")
food_cat.deposit(100, 'cheese')
food_cat.deposit(30, 'rice')
food_cat.withdraw(15, 'acai')
print(food_cat.get_balance())

health_cat = Category("Health")
health_cat.deposit(20)
health_cat.withdraw(5, 'dipirona')
# print(health_cat.get_balence())

print(food_cat.transfer(50, health_cat))

# print(food_cat.ledger)
# print(health_cat.ledger)
# print(food_cat.get_balance())

# print(food_cat, health_cat.category)

print(food_cat)

def create_spend_chart(categories):
    pass