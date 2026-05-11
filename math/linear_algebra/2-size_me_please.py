#!/usr/bin/env python3
"""This module id about  matrices"""


def matrix_shape(matrix):
    """Calculates the shape of a matrix recursively"""
    if not isinstance(matrix, list):
        return []
    return [len(matrix)] + matrix_shape(matrix[0])
