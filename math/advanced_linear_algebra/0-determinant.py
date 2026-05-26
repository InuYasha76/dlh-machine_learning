#!/usr/bin/env python3
"""This module is about matrices an determinant."""


def get_minor(matrix, i, j):
    """Extracts the submatrix by removing the i-th row and the j-th column."""
    remaining_rows = matrix[:i] + matrix[i + 1:]
    return [row[:j] + row[j + 1:] for row in remaining_rows]


def determinant(matrix):
    """
    Calculates the determinant of a matrix recursively.
    Args:
        - matrix (list of lists).
    Returns:
        - the determinant of matrix.
    """
    n = len(matrix)
    det = 0
    sign = 1

    if not (matrix and
            isinstance(matrix, list) and
            isinstance(matrix[0], list)):
        raise TypeError("matrix must be a list of lists")

    if n != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")

    if n == 0 or len(matrix[0]) == 0:
        return 1

    if n == 1:
        return matrix[0][0]

    for i in range(n):
        sub_matrix = get_minor(matrix, i)
        det += sign * matrix[0][i] * determinant(sub_matrix)
        sign *= -1

    return det
