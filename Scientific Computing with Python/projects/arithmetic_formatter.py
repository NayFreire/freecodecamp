import re
import string

digits = string.digits

def is_it_just_numbers(number):
    for n in number:
        if n not in digits:
            return False
    return True

def get_vertical(problems):
    no_result = []
    first_line = []
    second_line = []
    third_line = []
    forth_line = []

    for problem in problems:
        operation = 0
        first_line.append(f'{problem.split()[0]}')

        second_line.append(f'{problem.split()[1]}    {problem.split()[2]}')
        third_line.append('-----')

        if problem.split()[1] == '+':
            operation = int(problem.split()[0]) + int(problem.split()[2])
        else:
            operation = int(problem.split()[0]) - int(problem.split()[2])
        
        forth_line.append(operation)
        
    no_result.append(first_line)
    no_result.append(second_line)
    no_result.append(third_line)
    no_result.append(forth_line)
    return no_result

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
            

        problems = get_vertical(problems)
        # print(problems)
    except ValueError as e:
        print("Error: ", e)


    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
# print(is_it_just_numbers('12.9'))