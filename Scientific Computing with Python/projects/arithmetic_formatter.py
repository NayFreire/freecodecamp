"""
Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

"""

MAX_PROBLEMS = 5
MAX_DIGITS = 4
NUM_SPACES = 4

def has_error(problems):
    """
        Returns true or false + a message if the operation has any error.

        Args:
            problems (list): each item is a string for each problem

        Returns:
            bool, string: it returns the verification for error and the message
    """

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
    """
        Verifies what is the operator and returns the result for the problem.

        Args:
            operand_1 (string): first operand of the operation
            operator (string): operator (+ or -)
            operand_2 (string): second operand of the operation 

        Returns:
            int: result of the operation
    """

    if operator == '+':
        return int(operand_1) + int(operand_2)
    else:
        return int(operand_1) - int(operand_2)
    
def operand_1_with_space(operand_1, operator, operand_2, index, list_size):
    """
        Verifies what operand is the biggest and add spaces according to each size

        Args:
            operand_1 (string): first operand of the operation
            operator (string): operator (+ or -)
            operand_2 (string): second operand of the operation 
            index (int): index of the problem in the list
            list_size (int): size of the list problems

        Returns:
            string: the operand_1 with the spaces needed to fit the string
    """

    operand_with_space = ''
    
    if len(operand_1) >= len(operand_2): # Verifying the size of the operands
        operand_with_space = f"{'  ' + operand_1}" # This needs 2 spaces because it has to mach the '+ ' or '- ' of the second line
    else:
        operand_2_and_operator_size = len(f"{operator + ' ' + operand_2}")
        operand_with_space = f"{' '}{' ' * (operand_2_and_operator_size - len(operand_1) - 1)}{operand_1}" # If operand_2's size is bigger, operand_1 needs more than just the 2 spaces to fit

    # If the problem is the last, it doesn't need the 4 spaces after
    if index != list_size - 1:
        return f"{operand_with_space}{' ' * NUM_SPACES}"
    else:
        return f"{operand_with_space}"

def operand_2_with_space(operand_1, operator, operand_2, index, list_size):
    """
        Verifies what operand is the biggest and add spaces according to each size

        Args:
            operand_1 (string): first operand of the operation
            operator (string): operator (+ or -)
            operand_2 (string): second operand of the operation 
            index (int): index of the problem in the list
            list_size (int): size of the list problems

        Returns:
            string: the operand_2 with the spaces needed to fit the string
    """

    operand_with_space = ''

    if len(operand_1) >= len(operand_2): # Verifying the size of the operands
        operand_with_space = f"{operator + ' '}{' ' * (len(operand_1) - len(operand_2))}{operand_2}" # If operand_1's size is bigger, operand_2 needs more spaces to fit
    else:
        operand_with_space = f"{operator + ' ' + operand_2}" # If operand_2's size is bigger, it jusr needs the space between the operand and he operator

    # If the problem is the last, it doesn't need the 4 spaces after
    if index != list_size - 1:
        return f"{operand_with_space}{' ' * NUM_SPACES}"
    else:
        return f"{operand_with_space}"

def number_of_dashes_per_operation(operand_1, operator, operand_2, index, list_size):
    """
        Calculates the number of '-' needed and returns a string with the number of dashes

        Args:
            operand_1 (string): first operand of the operation
            operator (string): operator (+ or -)
            operand_2 (string): second operand of the operation 
            index (int): index of the problem in the list
            list_size (int): size of the list problems

        Returns:
            string: the result symbol formed by the dashes 
    """

    # If the problem is the last, it doesn't need the 4 spaces after
    if index != list_size - 1:
        return f"{(len(operand_2_with_space(operand_1, operator, operand_2, index, list_size)) - NUM_SPACES) * '-'}{' ' * NUM_SPACES}"
    else:
        return f"{(len(operand_2_with_space(operand_1, operator, operand_2, index, list_size))) * '-'}"

def result_with_spaces(operand_1, operator, operand_2, index, list_size):
    """
        Add the number of spaces needed to the result of the operation

        Args:
            operand_1 (string): first operand of the operation
            operator (string): operator (+ or -)
            operand_2 (string): second operand of the operation 
            index (int): index of the problem in the list
            list_size (int): size of the list problems

        Returns:
            string: the result with the spaces needed to fit the string
    """

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
        Returns the problem arranged.

        Args:
            problems (list): each item is a string for each problem
            show_answer (bool): condition to show or not the answer of each problem

        Returns:
            string: problems vertically arranged
    """
    
    there_are_errors, error_message = has_error(problems) #unpacking returns from function

    if not there_are_errors:
        operation = ''

        # Getting the line with the first operands
        for index, problem in enumerate(problems):
            operand_1, operator, operand_2 = problem.split()

            operation += operand_1_with_space(operand_1, operator, operand_2, index, len(problems))

        operation += '\n'
        
        # Getting the line with the second operands and its operators
        for index, problem in enumerate(problems):
            operand_1, operator, operand_2 = problem.split()

            operation += operand_2_with_space(operand_1, operator, operand_2, index, len(problems))

        operation += '\n'

        # Getting the line of dashes before the results
        for index, problem in enumerate(problems):
            operand_1, operator, operand_2 = problem.split()

            operation += number_of_dashes_per_operation(operand_1, operator, operand_2, index, len(problems))
        
        if show_answer: # Verifying if the user want to show the answer
            operation += '\n'

            # Getting the line with the results
            for index, problem in enumerate(problems):
                operand_1, operator, operand_2 = problem.split()

                operation += result_with_spaces(operand_1, operator, operand_2, index, len(problems))

        return operation
    else:
        return error_message

print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print(len(arithmetic_arranger(["3 + 855", "988 + 40"], True)))
