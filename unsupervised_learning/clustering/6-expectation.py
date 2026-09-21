#!/usr/bin/env python3
"""Module that calculates the E-step in the EM algorithm for a GMM."""
import numpy as np
pdf = __import__('5-pdf').pdf


def expectation(X, pi, m, S):
    """Calculate the expectation step in the EM algorithm for a GMM.

    For each cluster, computes the weighted likelihood
    pi[j] * pdf(X, m[j], S[j]),
    then normalises across clusters to obtain posterior probabilities.

    Args:
        X (numpy.ndarray): Dataset of shape (n, d).
        pi (numpy.ndarray): Cluster priors of shape (k,).
        m (numpy.ndarray): Centroid means of shape (k, d).
        S (numpy.ndarray): Covariance matrices of shape (k, d, d).

    Returns:
        tuple: (g, l) or (None, None) on failure.
            g (numpy.ndarray): Posterior probabilities of shape (k, n).
            log_l (float): Total log likelihood.
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None
    if not isinstance(pi, np.ndarray) or pi.ndim != 1:
        return None, None
    if not isinstance(m, np.ndarray) or m.ndim != 2:
        return None, None
    if not isinstance(S, np.ndarray) or S.ndim != 3:
        return None, None
    n, d = X.shape
    k = pi.shape[0]
    if m.shape != (k, d) or S.shape != (k, d, d):
        return None, None
    g = np.zeros((k, n))
    for j in range(k):
        g[j] = pi[j] * pdf(X, m[j], S[j])
    total = g.sum(axis=0)
    log_l = np.sum(np.log(total))
    g /= total
    return g, log_l
