#!/usr/bin/env python3
"""This module is about matrix multiplication."""


import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication.
    Assumes that mat1 and mat2 are ndarrays and never empty.
    """
    return mat1 @ mat2
