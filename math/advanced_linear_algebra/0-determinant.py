#!/usr/bin/env python3


def determinant(matrix):
    if not isinstance(matrix[0], list):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return 0 if matrix[0][0] is None else matrix[0][0]
    


