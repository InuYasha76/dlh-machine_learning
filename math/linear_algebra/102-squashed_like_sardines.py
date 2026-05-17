#!/usr/bin/env python3
"""This module is about matrices concatenation."""


def get_shape(matrix):
    """Recursive matrix shape finder."""
    if not isinstance(matrix, list):
        return []
    return [len(matrix)] + get_shape(matrix[0])


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.
    Args:
        mat1: list containing ints or floats or lists (of list) of ints/floats.
        mat2: list containing ints of floats or lists (of list) of ints/floats.
        axis: 0 is the row axis (defautl), 1 the column axis.
    Returns:
        A new matrix.
    """
    shape1 = get_shape(mat1)
    shape2 = get_shape(mat2)
    # Concat Rule 1: ranks of mat1 and mat2 must be identical
    if len(shape1) != len(shape2):
        return None
    # Concat Rule 2: all dimensions except on the axis must be identical
    for i in range(len(shape1)):
        if i != axis and shape1[i] != shape2[i]:
            return None
    if axis == 0:
        return mat1 + mat2
    return [cat_matrices(sub1, sub2, axis - 1)
            for sub1, sub2 in zip(mat1, mat2)]
