#!/usr/bin/python3
"""
matrix_divided() - divides each element of a matrix by a divisor
Returns input errors
Returns a new matrix with the newly calculated elements if no errros
"""


def matrix_divided(matrix, divisor):
    msg_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(divisor, int) and not isinstance(divisor, float):
        raise TypeError('divisor must be a number')
    if matrix == [] or not isinstance(matrix, list):
        raise TypeError(msg_error)
    if not all(isinstance(i, list) for i in matrix):
        raise TypeError(msg_error)
    if len(matrix[0]) == 0:
        raise TypeError(msg_error)
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for item in row:
            if isinstance(item, (int, float)):
                item = int(item)
            else:
                raise TypeError(msg_error)
        if divisor == 0:
            raise ZeroDivisionError('error:division by zero')
    new_matrix = [[round(elem / divisor, 2) for elem in row] for row in matrix]
    return new_matrix
