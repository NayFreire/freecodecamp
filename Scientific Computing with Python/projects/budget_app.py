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

def create_spend_chart(categories):
    percentages = []
    chart = []

    total_spent = get_total_spent(categories)

    sum_spent = sum([int(spent['spent']) for spent in total_spent])
    # print(total_spent, sum_spent)

    percentages = get_percentages(total_spent, sum_spent)
    # print(percentages)

    percentages = rounded_down_percentages(percentages)
    # print(percentages)

    chart.append({'percent': None, 'line': ['Percentage spent by category']})
    chart.append({'percent': 100, 'line': ['100|']})
    chart.append({'percent': 90, 'line': [' 90|']})
    chart.append({'percent': 80, 'line': [' 80|']})
    chart.append({'percent': 70, 'line': [' 70|']})
    chart.append({'percent': 60, 'line': [' 60|']})
    chart.append({'percent': 50, 'line': [' 50|']})
    chart.append({'percent': 40, 'line': [' 40|']})
    chart.append({'percent': 30, 'line': [' 30|']})
    chart.append({'percent': 20, 'line': [' 20|']})
    chart.append({'percent': 10, 'line': [' 10|']})
    chart.append({'percent': 0, 'line': ['  0|']})

    for index, list_line in enumerate(chart):
        if index != 0:
            for pos in range(len(categories) + 1):
                if not pos == len(categories):
                    list_line['line'].append('   ')
                else:
                    list_line['line'].append(' ')
            
                

    for index, percentage in enumerate(percentages):
        for pace in range(100, -10, -10):
            # print('porcentagem: ', pace)
            if percentage['percent'] == pace:
                for i, value in enumerate(chart):
                    # print('index no chart:', i, '\nvalue[percent]:', value['percent'])
                    if value['percent'] == pace:
                        chart[i]['line'][index+1] = ' o '
                        for pos in range(i+1, len(chart)):
                            chart[pos]['line'][index+1] = ' o '
    
    chart.append({'percent': None, 'line': [f"    {'-' * (len(categories) * 3)}-"]})
    
    categories_names = []

    for category in categories: 
        letters = [letter for letter in category.category]
        categories_names.append(letters)
    
    biggest_name = max(categories_names, key=len)
    
    for name in categories_names:
        if name != biggest_name:
            num_spaces_added = len(biggest_name) - len(name)
            for _ in range(num_spaces_added):
                name.append(' ')


    letters = []
    for letter in range(len(biggest_name)):
        for index in range(len(categories_names)):
            # print(categories_names[index][letter])
            if index == 0:
                letters.append(f'     {categories_names[index][letter]} ')
            elif index == len(categories_names) - 1:
                letters.append(f' {categories_names[index][letter]}  ')
            else:
                letters.append(f' {categories_names[index][letter]} ')
        chart.append({'percent': None, 'line': letters})
        letters = []
        # print('***')
        
    # print(categories_names)

    string_chart = ''

    for line in chart:
        # for item in line['line']:
        #     print(f">{item}< | {len(item)}")
        #     string_chart += item
        string_line = ''.join(line['line'])
        string_chart += repr(string_line).replace("'", "")
        string_chart += '\n'
        
    print(string_chart, len(string_chart))
    # print(chart)


food = Category("Food")
food.deposit(1000.1234, "deposit")
food.withdraw(10.150, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50.33, clothing)

# clothing.withdraw(10, "test")

health = Category("Health")
health.deposit(300.52, "deposit")
health.withdraw(56.130, "ritalina")
health.withdraw(30.31, 'carbamazepina')

print(health)

print(food)
print(clothing)

# food.get_spending()

# create_spend_chart([health, food, clothing])