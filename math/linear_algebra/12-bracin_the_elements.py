#!/usr/bin/env python3
"""This module is about element-wise matrix operations."""


def np_elementwise(mat1, mat2):
    """Returns element-wise add, sub, mul, div of two matrices."""
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
