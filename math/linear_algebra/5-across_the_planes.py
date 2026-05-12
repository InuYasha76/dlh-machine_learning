#!/usr/bin/env python3
"""This module is about linear algebra."""


def matrix_shape(matrix):
    """Calculates the shape of a matrix recursively"""
    if not isinstance(matrix, list):
        return []
    return [len(matrix)] + matrix_shape(matrix[0])


def add_matrices2D(mat1, mat2):
    """Adds two matrices element-wise."""
    if not (mat1 and mat1[0] and mat2 and mat1[0]
            and matrix_shape(mat1) == matrix_shape(mat2)):
        return None
    result = []
    for row_m1, row_m2 in zip(mat1, mat2):
        result.append([a + b for a, b in zip(row_m1, row_m2)])
    return result


if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    print(add_matrices2D([], []))
    print(add_matrices2D(mat1, mat2))
    print(mat1)
    print(mat2)
    print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))
