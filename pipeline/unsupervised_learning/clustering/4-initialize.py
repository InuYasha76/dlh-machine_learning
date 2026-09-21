#!/usr/bin/env python3
"""Module that initializes variables for a Gaussian Mixture Model."""
import numpy as np
kmeans = __import__('1-kmeans').kmeans


def initialize(X, k):
    """Initialize variables for a Gaussian Mixture Model (GMM).

    Args:
        X (numpy.ndarray): Dataset of shape (n, d).
        k (int): Number of clusters (positive integer).

    Returns:
        tuple: (pi, m, S) or (None, None, None) on failure.
            pi (numpy.ndarray): Priors of shape (k,), evenly initialized.
            m (numpy.ndarray): Centroid means of shape (k, d) from K-means.
            S (numpy.ndarray): Covariance matrices of shape (k, d, d),
                initialized as identity matrices.
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None, None
    if not isinstance(k, int) or isinstance(k, bool) or k <= 0:
        return None, None, None
    n, d = X.shape
    m, _ = kmeans(X, k)
    if m is None:
        return None, None, None
    pi = np.ones(k) / k
    S = np.tile(np.eye(d), (k, 1, 1))
    return pi, m, S
