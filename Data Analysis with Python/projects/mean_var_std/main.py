import numpy as np
from mean_var_std import turn_into_matrix, mean_values, variance_values
from mean_var_std import std_values, max_values, min_values, sum_values

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        matrix = turn_into_matrix(np.array(list))
        mean = mean_values(matrix)
        variance = variance_values(matrix)
        std = std_values(matrix)
        max = max_values(matrix)
        min = min_values(matrix)
        sum = sum_values(matrix)

        return {
            'mean': mean,
            'variance': variance,
            'standard deviation': std,
            'max': max,
            'min': min,
            'sum': sum
        }

print(calculate([0,1,2,3,4,5,6,7,8]))