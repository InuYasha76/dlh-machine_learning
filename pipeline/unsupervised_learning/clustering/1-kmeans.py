#!/usr/bin/env python3
"""Module that performs K-means clustering on a dataset."""
import numpy as np


def kmeans(X, k, iterations=1000):
    """Perform K-means clustering on a dataset.

    Args:
        X (numpy.ndarray): Dataset of shape (n, d).
        k (int): Number of clusters (positive integer).
        iterations (int): Maximum number of iterations (positive integer).

    Returns:
        tuple: (C, clss) where C is a numpy.ndarray of shape (k, d)
            containing the centroid means and clss is a numpy.ndarray
            of shape (n,) containing the cluster index per data point.
            Returns (None, None) on failure.
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None
    if not isinstance(k, int) or isinstance(k, bool) or k <= 0:
        return None, None
    if (not isinstance(iterations, int)
            or isinstance(iterations, bool)
            or iterations <= 0):
        return None, None
    n, d = X.shape
    low, high = X.min(axis=0), X.max(axis=0)
    # Initialize centroids uniformly
    C = np.random.uniform(low, high, size=(k, d))
    for _ in range(iterations):
        C_prev = C.copy()
        # Assign each point to its nearest centroid
        distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)
        clss = np.argmin(distances, axis=1)
        # Recompute centroids; reinitialize any empty cluster uniformly
        for j in range(k):
            mask = clss == j
            C[j] = (X[mask].mean(axis=0) if mask.any()
                    else np.random.uniform(low, high))
        if np.array_equal(C, C_prev):
            break
    # Final assignment after convergence or max iterations
    distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)
    clss = np.argmin(distances, axis=1)
    return C, clss
