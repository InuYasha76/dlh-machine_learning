#!/usr/bin/env python3
"""Module that finds the optimum number of K-means clusters by variance."""
import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """Find the optimum number of clusters for K-means by variance.

    Runs K-means for each k in [kmin, kmax] and records the drop in
    variance relative to kmin, producing the data for an elbow curve.

    Args:
        X (numpy.ndarray): Dataset of shape (n, d).
        kmin (int): Minimum number of clusters to check (inclusive).
        kmax (int): Maximum number of clusters to check (inclusive).
            Defaults to n (number of data points).
        iterations (int): Maximum K-means iterations per run.

    Returns:
        tuple: (results, d_vars) or (None, None) on failure.
            results (list): K-means (C, clss) output for each k.
            d_vars (list): Variance drop from kmin variance for each k.
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None
    if not isinstance(kmin, int) or isinstance(kmin, bool) or kmin <= 0:
        return None, None
    if (not isinstance(iterations, int)
            or isinstance(iterations, bool)
            or iterations <= 0):
        return None, None
    n = X.shape[0]
    if kmax is None:
        kmax = n
    if not isinstance(kmax, int) or isinstance(kmax, bool) or kmax <= 0:
        return None, None
    if kmax - kmin < 1:
        return None, None

    results, variances = [], []
    for k in range(kmin, kmax + 1):
        C, clss = kmeans(X, k, iterations)
        if C is None:
            return None, None
        results.append((C, clss))
        variances.append(variance(X, C))
    d_vars = list(variances[0] - np.array(variances))
    return results, d_vars
