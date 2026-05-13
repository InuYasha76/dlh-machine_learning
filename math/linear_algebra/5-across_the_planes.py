#!/usr/bin/env python3
"""This module is about linear algebra."""


def matrix_shape(matrix):
    """Calculates the shape of a matrix recursively"""
    if not isinstance(matrix, list):
        return []
    return [len(matrix)] + matrix_shape(matrix[0])


def add_matrices2D(mat1, mat2):
    """Adds two matrices element-wise."""
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    return [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(mat1, mat2)]
