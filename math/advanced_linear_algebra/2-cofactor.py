#!/usr/bin/env python3
"""This module is about matrices, minors, cofactors."""


def cofactor(matrix):
    """
    Calculates the cofactor matrix of a matrix.
    Args:
        matrix (list of list)
    Returns:
        List of lits: the cofactor matrix.
    """
    minor_matrix = minor(matrix)
    n = len(minor_matrix)

    return [[(-1) ** (i + j) * minor_matrix[i][j] for j in range(n)]
            for i in range(n)]
