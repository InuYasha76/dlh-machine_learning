#!/usr/bin/env python3
"""This module is about numpy concatenation."""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenates two matrices along a specific axis."""
    return np.concatenate((mat1, mat2), axis)
