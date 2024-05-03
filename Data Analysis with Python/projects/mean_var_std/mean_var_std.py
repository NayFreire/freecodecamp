import numpy as np

def turn_into_matrix(list):
    return np.vstack([list[:3], list[3:6], list[6:10]])

def mean_values(matrix):
    mean_row = np.mean(matrix, axis=0)
    mean_col = np.mean(matrix, axis=1)
    mean_mat = np.mean(matrix)

    return [mean_row, mean_col, mean_mat]

def variance_values(matrix):
    var_row = np.var(matrix, axis=0)
    var_col = np.var(matrix, axis=1)
    var_mat = np.var(matrix) 

    return [var_row, var_col, var_mat]

def std_values(matrix):
    std_row = np.std(matrix, axis=0)
    std_col = np.std(matrix, axis=1)
    std_mat = np.std(matrix)

    return [std_row, std_col, std_mat]

def max_values(matrix):
    max_row = np.max(matrix, axis=0)
    max_col = np.max(matrix, axis=1)
    max_mat = np.max(matrix)

    return [max_row, max_col, max_mat]

def min_values(matrix):
    min_row = np.min(matrix, axis=0)
    min_col = np.min(matrix, axis=1)
    min_mat = np.min(matrix)

    return [min_row, min_col, min_mat]

def sum_values(matrix):
    sum_row = np.sum(matrix, axis=0)
    sum_col = np.sum(matrix, axis=1)
    sum_mat = np.sum(matrix)

    return [sum_row, sum_col, sum_mat]

