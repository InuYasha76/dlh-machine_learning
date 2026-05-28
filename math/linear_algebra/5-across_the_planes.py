#!/usr/bin/env python3
"""This module is about linear algebra."""


def add_matrices2D(mat1, mat2):
    """Adds two matrices element-wise."""
    try:
        return [
                [a + b for a, b in zip(r1, r2, strict=True)]
                for r1, r2 in zip(mat1, mat2, strict=True)
                ]
    except ValueError:
        return None
