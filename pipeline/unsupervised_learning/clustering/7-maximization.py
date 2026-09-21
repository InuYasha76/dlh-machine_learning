#!/usr/bin/env python3
"""Module that calculates the M-step in the EM algorithm for a GMM."""
import numpy as np


def maximization(X, g):
    """Calculate the maximization step in the EM algorithm for a GMM.

    Args:
        X (numpy.ndarray): Dataset of shape (n, d).
        g (numpy.ndarray): Posterior probabilities of shape (k, n).

    Returns:
        tuple: (pi, m, S) or (None, None, None) on failure.
            pi (numpy.ndarray): Updated priors of shape (k,).
            m (numpy.ndarray): Updated centroid means of shape (k, d).
            S (numpy.ndarray): Updated covariance matrices of shape (k, d, d).
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None, None
    if not isinstance(g, np.ndarray) or g.ndim != 2:
        return None, None, None
    n, d = X.shape
    k = g.shape[0]
    if g.shape[1] != n:
        return None, None, None
    N = g.sum(axis=1)
    pi = N / n
    m = (g @ X) / N[:, np.newaxis]
    S = np.zeros((k, d, d))
    for j in range(k):
        diff = X - m[j]
        S[j] = (g[j, :, np.newaxis] * diff).T @ diff / N[j]
    return pi, m, S
