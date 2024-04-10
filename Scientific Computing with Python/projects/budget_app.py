"""
Complete the Category class. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list.
"""
NUM_OF_ASTERISKS = 30
NUM_OF_DIGITS = 7

class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    """
    6 - When the budget object is printed it should display:

    - A title line of 30 characters where the name of the category is centered in a line of * characters.
    - A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
    - A line displaying the category total.
    """

    def __str__(self):
        display = ''
        total_of_asterisks = NUM_OF_ASTERISKS - len(self.category)

        title = f"{'*' * int(total_of_asterisks/2)}{self.category}{'*' * int(total_of_asterisks/2)}"

        display += title + '\n'

        for ledge in self.ledger:
            ledge_dict = f"{ledge['description']}{str(round(ledge['amount'], 2))[:NUM_OF_DIGITS-1]}"
            if len(ledge_dict) > len(title):
                new_size = len(title) - len(str(ledge['amount']))
                display += f"{ledge['description'][:new_size-1]}{' '}{str(round(ledge['amount'], 2))[:NUM_OF_DIGITS-1]}"
            else:
                display += f"{ledge['description']}{(len(title) - len(ledge_dict)) * ' '}{str(round(ledge['amount'], 2))[:NUM_OF_DIGITS-1]}"
            display += '\n'
            print(len(title), len(ledge_dict))

        total = self.get_balance()
        display += f"Total: {total}"

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
    5 - A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
    """

    def check_funds(self, amount):
        balance = self.get_balance()

        if amount > balance:
            return False
        return True
    
    def get_spending(self):
        spending = 0
        spending = sum([spend['amount'] for spend in self.ledger if spend['amount'] < 0]) * -1

food = Category("Food")
food.deposit(1000.1234, "deposit")
food.withdraw(10.150, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)

food.get_spending()

"""
7 - Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".
"""

def create_spend_chart(categories):
    pass