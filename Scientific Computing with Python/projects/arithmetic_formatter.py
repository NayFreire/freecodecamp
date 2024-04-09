"""
Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

"""

MAX_PROBLEMS = 5
MAX_DIGITS = 4
NUM_SPACES = 4

def has_error(problems):
    #1) If there are too many problems supplied to the function. The limit is five, anything more will return: #!'Error: Too many problems.'
    
    if len(problems)> MAX_PROBLEMS:
        return True, "Error: Too many problems."
    
    for problem in problems:
        operand_1, operator, operand_2 = problem.split()
    
        #2) The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: #!"Error: Operator must be '+' or '-'."

        if operator not in ['+', '-']:
            return True, "Error: Operator must be '+' or '-'."

        #3) Each number (operand) should only contain digits. Otherwise, the function will return: #!'Error: Numbers must only contain digits.'

        if not operand_1.isdigit() or not operand_2.isdigit():
            return True, 'Error: Numbers must only contain digits.'

        #4) Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: #!'Error: Numbers cannot be more than four digits.'

        if len(operand_1) > MAX_DIGITS or len(operand_2) > MAX_DIGITS:
            return True, 'Error: Numbers cannot be more than four digits.'
    return False, 'Ok'

def result_operation(operand_1, operator, operand_2):
    if operator == '+':
        return int(operand_1) + int(operand_2)
    else:
        return int(operand_1) - int(operand_2)
    
def operand_1_with_space(operand_1, operator, operand_2, index, list_size):
    operand_with_space = ''
    
    if len(operand_1) >= len(operand_2):
        operand_with_space = f"{'  ' + operand_1}"
    else:
        operand_2_and_operator_size = len(f"{operator + ' ' + operand_2}")
        operand_with_space = f"{' '}{' ' * (operand_2_and_operator_size - len(operand_1) - 1)}{operand_1}"

    if index != list_size - 1:
        return f"{operand_with_space}{' ' * NUM_SPACES}"
    else:
        return f"{operand_with_space}"

def operand_2_with_space(operand_1, operator, operand_2, index, list_size):
    operand_with_space = ''
    if len(operand_1) >= len(operand_2):
        operand_2_and_operator_size = len(operand_2)
        operand_with_space = f"{operator + ' '}{' ' * (len(operand_1) - operand_2_and_operator_size)}{operand_2}"
    else:
        operand_with_space = f"{operator + ' ' + operand_2}"
    if index != list_size - 1:
        return f"{operand_with_space}{' ' * NUM_SPACES}"
    else:
        return f"{operand_with_space}"

def number_of_dashes_per_operation(operand_1, operator, operand_2, index, list_size):
    if index != list_size - 1:
        return f"{(len(operand_2_with_space(operand_1, operator, operand_2, index, list_size)) - NUM_SPACES) * '-'}{' ' * NUM_SPACES}"
    else:
        return f"{(len(operand_2_with_space(operand_1, operator, operand_2, index, list_size))) * '-'}"

def result_with_spaces(operand_1, operator, operand_2, index, list_size):
    if index != list_size - 1:
        num_of_dashes = len(number_of_dashes_per_operation(operand_1, operator, operand_2, index, list_size)) - NUM_SPACES
        num_of_spaces = num_of_dashes - len(str(result_operation(operand_1, operator, operand_2)))

        return f"{' ' * num_of_spaces}{result_operation(operand_1, operator, operand_2)}{' ' * NUM_SPACES}"
    else:
        num_of_dashes = len(number_of_dashes_per_operation(operand_1, operator, operand_2, index, list_size))
        num_of_spaces = num_of_dashes - len(str(result_operation(operand_1, operator, operand_2)))

        return f"{' ' * num_of_spaces}{result_operation(operand_1, operator, operand_2)}"

def arithmetic_arranger(problems, show_answer=False):
    """
        Returns the problem arrenged.

        Args:
            problems (list): each item is a string for each problem
            show_answer (bool): condition to show or not the answer of each problem

        Returns:
            string: problems arrenged
    """
    
    there_are_errors, error_message = has_error(problems) #unpacking returns from function

    if not there_are_errors:
        operation = ''

        for index, problem in enumerate(problems):
            operand_1, operator, operand_2 = problem.split()

            operation += operand_1_with_space(operand_1, operator, operand_2, index, len(problems))

        operation += '\n'
        
        for index, problem in enumerate(problems):
            operand_1, operator, operand_2 = problem.split()

            operation += operand_2_with_space(operand_1, operator, operand_2, index, len(problems))

        operation += '\n'

        for index, problem in enumerate(problems):
            operand_1, operator, operand_2 = problem.split()

            operation += number_of_dashes_per_operation(operand_1, operator, operand_2, index, len(problems))
        
        if show_answer:
            operation += '\n'

            for index, problem in enumerate(problems):
                operand_1, operator, operand_2 = problem.split()

                operation += result_with_spaces(operand_1, operator, operand_2, index, len(problems))

        return operation
    else:
        return error_message

print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print(len(arithmetic_arranger(["3 + 855", "988 + 40"], True)))
