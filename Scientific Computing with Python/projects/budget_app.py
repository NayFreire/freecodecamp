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
        title = f"{self.category:*^30}"
        items = ''
        total = 0

        for transaction in self.ledger:
            description = transaction['description'][:23]
            amount = transaction['amount']
            total += amount
            items += f'{description:<23}{amount:>7.2f}\n'
        
        output = title + '\n' + items + f'Total: {total:.2f}'
        return output
    
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
        return round(sum(ledge['amount'] for ledge in self.ledger), 2)
    
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
        return sum([spend['amount'] for spend in self.ledger if spend['amount'] < 0]) * -1

"""
7 - Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".
"""

def get_total_spent(categories):
    total_spent = []
    for category in categories:
        spending = category.get_spending()
        # print(category.category, spending)

        total_spent.append({'category': category.category, 'spent':spending})
    return total_spent

def get_percentages(total_spent, sum_spent):
    percentages = []
    for spent in total_spent:
        percentage = (spent['spent'] * 100) / sum_spent
        percentages.append({'category': spent['category'], 'percent': int(percentage)})
    return percentages

def rounded_down_percentages(percentages):
    for percentage in percentages:
        new_percentage = int(percentage['percent'] / 10)
        new_percentage = new_percentage * 10
        percentage['percent'] = new_percentage
    return percentages

def getTotals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_spending()
        breakdown.append(category.get_spending())
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded

def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier

def create_spend_chart(categories):
    """
    create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart
    """
    res = "Percentage spent by category\n"
    i = 100
    totals = getTotals(categories)
    while i >= 0:
          cat_spaces = " "
          for total in totals:
              if total * 100 >= i:
                  cat_spaces += "o  "
              else:
                  cat_spaces += "   "
          res+= str(i).rjust(3) + "|" + cat_spaces + ("\n")
          i-=10
      
    dashes = "-" + "---"*len(categories)
    names = []
    x_axis = ""
    for category in categories:
          names.append(category.category)

    maxi = max(names, key=len)

    for x in range(len(maxi)):
        nameStr = '     '
        for name in names:
              if x >= len(name):
                  nameStr += "   "
              else:
                  nameStr += name[x] + "  "
        
        if(x != len(maxi) -1 ):
          nameStr += '\n'

          
        x_axis += nameStr

    res+= dashes.rjust(len(dashes)+4) + "\n" + x_axis
    return res


# food = Category("Food")
# food.deposit(1000.1234, "deposit")
# food.withdraw(10.150, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")

# clothing = Category("Clothing")
# food.transfer(50.33, clothing)

# # clothing.withdraw(10, "test")

# health = Category("Health")
# health.deposit(300.52, "deposit")
# health.withdraw(56.130, "ritalina")
# health.withdraw(30.31, 'carbamazepina')

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

# print(health)

# print(food)
# print(clothing)

# food.get_spending()

print(create_spend_chart([business, food, entertainment]))