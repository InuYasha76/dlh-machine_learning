#!/usr/bin/env python3
"""This module is about matrices, minor and determinant."""


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

    if n == 0 or len(matrix[0]) == 0:
        return 1
    if n == 1:
        return matrix[0][0]

    det = 0
    for j in range(n):
        sign = 1 if j % 2 == 0 else -1
        sub_matrix = get_minor(matrix, 0, j)
        det += sign * matrix[0][j] * determinant(sub_matrix)

    return det


def minor(matrix):
    """
    Calculates the minor matrix of a matrix.
    Args:
        matrix (list of lists).
    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is empty or not square.
    Returns:
        list of lists: The minor matrix.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    return [[determinant(get_minor(matrix, i, j)) for j in range(n)]
            for i in range(n)]

def cofactor(matrix):
    """
    Calculates the cofactor matrix of a matrix.
    Args:
        matrix (list of lists).
    Returns:
        List of lits: the cofactor matrix.
    """
    minor_matrix = minor(matrix)
    n = len(minor_matrix)

    return [[(-1) ** (i + j) * minor_matrix[i][j] for j in range(n)]
            for i in range(n)]
