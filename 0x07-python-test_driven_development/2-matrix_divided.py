#!/usr/bin/python3
"""module for division all elements of a matrix"""

def matrix_divided(matrix, div):
    """divides all elements in the matrix

    Args:
    matrix: the matrix whose elements would be divided
    div: the divisor

    Raises:
    TypeError: if matrix is not a list of int or float numbers
    TypeError: if each row of matrix is not the same size
    TypeError: if div is neither an int nor float
    ZeroDivisionError: if div is 0

    Returns:
    a new matrix whose elements are round to 2 d.p
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_length = []
    for row in matrix:
        row_length.append(len(row))
    if not all(elements == row_length[0] for elements in row_length):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
