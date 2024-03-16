import string

def arithmetic_arranger(problems, show_answers=False):
    try:
        if len(problems) > 5:
            raise ValueError("Too many problems.")
        
    except ValueError as e:
        print("Error: ", e)

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 * 43", "123 + 49", "45 * 43", "123 + 49"])}')