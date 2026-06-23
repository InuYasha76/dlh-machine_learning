#!/usr/bin/env python3
"""This module is about multivariate probability."""

import numpy as np


def correlation(C):
    """
    Calculates a correlation matrix from a covariance matrix.

    Args:
        C (numpy.ndarray): Shape (d, d) containing a covariance matrix.

    Returns:
        numpy.ndarray: Shape (d, d) containing the correlation matrix.
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")
    std_devs = np.sqrt(np.diag(C))
    std_devs = std_devs.reshape(-1, 1)
    return C / np.dot(std_devs, std_devs.T)
