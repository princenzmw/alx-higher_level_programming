#!/usr/bin/python3
""" A Function that divides numbers (integers or float) from a matrix
    and divide them by a given divider to return a new matrix."""


def matrix_divided(matrix, div):
    """Matrix division

    Args:
        matrix (list): a list wit rows with equal size
        div (int / float): a number to be divided

    Raises:
        TypeError: matrix must contain lists of numbers only
        TypeError: the length of lists in matrix must be equal
        TypeError: div must be a number
        ZeroDivisionError: div must not be equal to 0

    Returns:
        list : a new matrix where each element is divided by div
    """
    for one in matrix:
        for two in one:
            if not isinstance(two, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
                    of integers/floats"
                )
    # Same as:
    # if not all(len(row) == len(matrix[0]) for row in matrix[1:]):
    #       raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = [[round(num / div, 2) for num in sub_ls] for sub_ls in matrix]

    return new_list
