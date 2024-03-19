import re
import string

digits = string.digits

def is_it_just_numbers(number):
    for n in number:
        if n not in digits:
            return False
    return True

def get_vertical(problems, show_answers):
    with_space = []
    first_line = []
    second_line = []
    third_line = []
    fourth_line = []
    full_operation = []
    vertical = ''

    operation = 0

    for problem in problems:
        first_operand = problem.split()[0]
        operator = problem.split()[1]
        second_operand = problem.split()[2]

        if len(first_operand) > len(second_operand):
            # print('#1', first_operand)
            with_space = f"{' ' * (len(operator + ' ' + first_operand) - len(first_operand))}{first_operand}"
            first_line.append(with_space)

            with_space_and_operator = f"{operator}{' ' * (len(operator + ' ' + first_operand) - len(second_operand) - 1)}{second_operand}"
            second_line.append(with_space_and_operator)

            third_line.append(f"{'-' * len(operator + ' ' + first_operand)}")

        elif len(first_operand) < len(second_operand):
            # print('#2', second_operand)
            with_space = f"{' ' * (len(operator + ' ' + second_operand) - len(first_operand))}{first_operand}"
            first_line.append(with_space)

            with_space_and_operator = f"{operator} {second_operand}"
            second_line.append(with_space_and_operator)

            third_line.append(f"{'-' * len(operator + ' ' + second_operand)}")
        else:
            # print('#3', second_operand)
            with_space = f"{' ' * (len(operator + ' ' + second_operand) - len(first_operand))}{first_operand}"
            first_line.append(with_space)

            with_space_and_operator = f"{operator} {second_operand}"
            second_line.append(with_space_and_operator)

            third_line.append(f"{'-' * len(operator + ' ' + second_operand)}")

        if operator == '+':
            operation = int(first_operand) + int(second_operand)
        else:
            operation = int(first_operand) - int(second_operand)

        if show_answers:
            equal_line = f"{' ' * ((len(with_space_and_operator) - len(str(operation))))}{str(operation)}"
        else:
            equal_line = f"{' ' * len(with_space_and_operator)}"
        
        fourth_line.append(equal_line)

    first_line[len(first_line) - 1] += f'\n'
    second_line[len(second_line) - 1] += f'\n'
    third_line[len(third_line) - 1] += f'\n'
    fourth_line[len(fourth_line) - 1] += f'\n'

    for i in range(len(problems)):
        vertical += first_line[i]        
        if i != len(problems) - 1:
            # print(i, '*')
            vertical += '    '
    
    for i in range(len(problems)):
        vertical += second_line[i]         
        if i != len(problems) - 1:
            # print(i, '*')
            vertical += '    '            

    for i in range(len(problems)):
        vertical += third_line[i]        
        if i != len(problems) - 1:
            # print(i, '*')
            vertical += '    '

    for i in range(len(problems)):
        vertical += fourth_line[i]           
        if i != len(problems) - 1:
            # print(i, '*')
            vertical += '    '
    
    full_operation.append(first_line)
    full_operation.append(second_line)
    full_operation.append(third_line)
    full_operation.append(fourth_line)
    print(vertical)
    return full_operation

def arithmetic_arranger(problems, show_answers=False):
    try:
        # 1) If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
        if len(problems) > 5:
            raise ValueError("Too many problems.")
        
        # 2) The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
        for problem in problems:
            # print(problem)
            if '*' in problem or '/' in problem:
                raise ValueError("Operator must be '+' or '-'.")
            
            just_digits_1 = is_it_just_numbers(problem.split()[0])
            just_digits_2 = is_it_just_numbers(problem.split()[2])

            # 3) Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
            if not just_digits_1 or not just_digits_2:
                raise ValueError("Numbers must only contain digits.")
            
            # 4) Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'
            if len(problem.split()[0]) > 4 or len(problem.split()[2]) > 4:
                raise ValueError("Numbers cannot be more than four digits.")
            

        problems = get_vertical(problems, show_answers)
        # print(problems)
    except ValueError as e:
        print("Error: ", e)


    return problems

print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
# print(is_it_just_numbers('12.9'))