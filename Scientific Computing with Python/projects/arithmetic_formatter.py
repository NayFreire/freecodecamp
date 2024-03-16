import re
import string

digits = string.digits

def is_it_just_numbers(number):
    for n in number:
        if n not in digits:
            return False
    return True

def arithmetic_arranger(problems, show_answers=False):
    try:
        if len(problems) > 5:
            raise ValueError("Too many problems.")
        for problem in problems:
            print(problem)
            if '*' in problem or '/' in problem:
                raise ValueError("Operator must be '+' or '-'.")
            
            just_digits_1 = is_it_just_numbers(problem.split()[0])
            just_digits_2 = is_it_just_numbers(problem.split()[2])

            if not just_digits_1 or not just_digits_2:
                raise ValueError("Numbers must only contain digits.")
            
            if len(problem.split()[0]) > 4 or len(problem.split()[2]) > 4:
                raise ValueError("Numbers cannot be more than four digits.")
    except ValueError as e:
        print("Error: ", e)

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
# print(is_it_just_numbers('12.9'))