#!/usr/bin/env python3
"""This module is about element-wise matrix operations."""


# import numpy as np


def np_elementwise(mat1, mat2):
    """
    Returns element-wise add, sub, mul, div of two matrices.
    Safely handles division by zero and invalid shapes.
    """
    arr1 = np.asarray(mat1)
    arr2 = np.asarray(mat2)

    if arr1.shape != arr2.shape:
        return None

    add_res = arr1 + arr2
    sub_res = arr1 - arr2
    mul_res = arr1 * arr2

    div_output = np.full_like(arr1, np.nan, dtype=float)
    div_res = np.divide(arr1, arr2, out=div_output, where=arr2 != 0)

    return add_res, sub_res, mul_res, div_res
