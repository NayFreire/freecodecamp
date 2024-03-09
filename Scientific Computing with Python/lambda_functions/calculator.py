addition = lambda x, y: x+y
subtraction = lambda x, y: x-y
multiplication = lambda x, y: x*y
division = lambda x,y: x/y

first_number = float(input('Whats the first number? '))
operation = input('Choose one operation? (+, -, *, /)')
second_number = float(input('Whats the second number? '))

if operation == '+':
    print(addition(first_number, second_number))
elif operation == '-':
    print(subtraction(first_number, second_number))
elif operation == '*':
    print(multiplication(first_number, second_number))
elif operation == '/':
    print(division(first_number, second_number))
else:
    print('This is not a valid operation')
