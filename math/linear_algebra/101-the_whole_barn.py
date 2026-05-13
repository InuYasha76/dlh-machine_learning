#!/usr/bin/env python3
"""This module is about linear algebra."""


def matrix_shape(matrix):
    """Calculates the shape of a matrix recursively"""
    if not (matrix and isinstance(matrix, list)):
        return []
    return [len(matrix)] + matrix_shape(matrix[0])


def add_matrices(mat1, mat2):
    """Adds two matrices element-wise recursively."""
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    if not isinstance(mat1, list):
        return mat1 + mat2
    return [add_matrices(m1, m2) for m1, m2 in zip(mat1, mat2)]
