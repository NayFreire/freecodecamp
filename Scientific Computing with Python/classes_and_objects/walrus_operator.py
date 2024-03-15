'''
The walrus operator allows you to assign a value to a variable as part of an expression. This can be particularly useful in situations where you need to both assign a value to a variable and use that value in an expression.
'''

# Without using the walrus operator
name = input("Enter your name: ")
if len(name) > 10:
    print("Your name is too long!")
else:
    print("Your name is:", name)

# Using the walrus operator
if (name := input("Enter your name: ")) > 10:
    print("Your name is too long!")
else:
    print("Your name is:", name)

'''
In this example, the walrus operator := allows us to both assign the value returned by input("Enter your name: ") to the variable name and use that value in the subsequent comparison within the if statement.
'''