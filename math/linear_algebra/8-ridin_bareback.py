#!/usr/bin/env python3
"""This module is about matrices multiplication."""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication:"""
    if len(mat1[0]) != len(mat2):
        return None
    mat2_t = list(zip(*mat2))
    return [[sum(a * b for a, b in zip(row, col))
             for col in mat2_t]
            for row in mat1]
