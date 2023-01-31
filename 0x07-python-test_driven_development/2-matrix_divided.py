#!/usr/bin/python3
"""define the function that divides a matrix"""


def matrix_divided(matrix, div):
    """
    divide all element of the matrix rounded to 2 decimal places

    args:
        matix: a list of list
        div(int or float): the divider

    Raises:
        TypeError: If the matrix contains non_numbers
        TypeError: If the matrix contains rows of diff sizes
        TypeError: if the div is not an int or float
        ZeroDivisionError: if div is 0
    Returns:
        a new matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matix for num in row])):
                raise TypeError("matrix must be a matix (list or lists) of ""integer/float")

    if not all(len(row) == len(matix[0]) for row in matrix):
        raise TypeError("Each row of te matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
