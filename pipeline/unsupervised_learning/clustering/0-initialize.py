#!/usr/bin/env python3
"""Module that initializes cluster centroids for K-means clustering."""
import numpy as np


def initialize(X, k):
    """Initialize cluster centroids for K-means using uniform sampling.

    Args:
        X (numpy.ndarray): Dataset of shape (n, d).
        k (int): Number of clusters (positive integer).

    Returns:
        numpy.ndarray: Initialized centroids of shape (k, d),
            or None on failure.
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None
    if not isinstance(k, int) or isinstance(k, bool) or k <= 0:
        return None
    if not X.size:
        return None
    n, d = X.shape
    low, high = X.min(axis=0), X.max(axis=0)
    return np.random.uniform(low, high, size=(k, d))
