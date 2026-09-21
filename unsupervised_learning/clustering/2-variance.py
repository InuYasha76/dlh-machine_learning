#!/usr/bin/env python3
"""Module that calculates total intra-cluster variance for a dataset."""
import numpy as np


def variance(X, C):
    """Calculate the total intra-cluster variance for a dataset.

    For each data point the squared distance to its nearest centroid
    is computed; the variance is the sum of those minimum distances.

    Args:
        X (numpy.ndarray): Dataset of shape (n, d).
        C (numpy.ndarray): Centroid means of shape (k, d).

    Returns:
        float: Total intra-cluster variance, or None on failure.
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None
    if not isinstance(C, np.ndarray) or C.ndim != 2:
        return None
    if X.shape[1] != C.shape[1]:
        return None
    distances_sq = np.sum((X[:, np.newaxis] - C) ** 2, axis=2)
    return np.sum(np.min(distances_sq, axis=1))
