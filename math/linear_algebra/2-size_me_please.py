#!/usr/bin/env python3
"""This module id about  matrices"""


def matrix_shape(matrix):
    """Calculates the shape of a matrix"""
    try:
        shape = [len(matrix), len(matrix[0]), len(matrix[0][0])]
    except Exception:
        try:
            shape = [len(matrix), len(matrix[0])]
        except Exception:
            raise
    finally:
        return shape
