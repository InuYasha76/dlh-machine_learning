#!/usr/bin/env python3
"""This module is about matrices concatenation."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two matrices along a specific axis."""
    if axis == 0 and len(mat1[0]) == len(mat2[0]):
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    elif axis == 1 and len(mat1) == len(mat2):
        return [r_mat1 + r_mat2 for r_mat1, r_mat2 in zip(mat1, mat2)]
    else:
        return None
