"""
Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

"""

MAX_PROBLEMS = 5

def arithmetic_arranger(problems, show_answer=True):
    """
        Returns the problem arrenged.

        Args:
            problems (list): each item is a string for each problem
            show_answer (bool): condition to show or not the answer of each problem

        Returns:
            string: problems arrenged
    """

    #1) If there are too many problems supplied to the function. The limit is five, anything more will return: #!'Error: Too many problems.'
    
    if len(problems)> MAX_PROBLEMS:
        return "Error: Too many problems."
    
    #2) The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: #!"Error: Operator must be '+' or '-'."

    #3) Each number (operand) should only contain digits. Otherwise, the function will return: #!'Error: Numbers must only contain digits.'

    #4) Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: #!'Error: Numbers cannot be more than four digits.'
    


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))