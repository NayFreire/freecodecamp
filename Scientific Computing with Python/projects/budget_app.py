"""
Complete the Category class. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list.
"""

class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
            
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
        total_amount = sum(ledge['amount'] for ledge in self.ledger)
        if total_amount >= amount:
            self.ledger.append({"amount": amount * -1, "description": description})

            return True
        return False
    
    """
    3 - A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    """

    def get_balence(self):
        return sum(ledge['amount'] for ledge in self.ledger)

food_cat = Category("Food")
food_cat.deposit(100, 'cheese')
food_cat.deposit(30, 'rice')
print(food_cat.withdraw(15, 'acai'))
print(food_cat.get_balence())

print(food_cat.ledger)

def create_spend_chart(categories):
    pass