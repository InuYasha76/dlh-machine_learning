#!/usr/bin/env python3
"""Module that finds the best number of GMM clusters using BIC."""
import numpy as np
expectation_maximization = __import__('8-EM').expectation_maximization


def BIC(X, kmin=1, kmax=None, iterations=1000, tol=1e-5, verbose=False):
    """Find the best number of clusters for a GMM using BIC.

    Uses the Bayesian Information Criterion formula:
    BIC = p * ln(n) - 2 * l, where p is the number of model parameters,
    n is the number of data points, and l is the log likelihood.

    Args:
        X (numpy.ndarray): Dataset of shape (n, d).
        kmin (int): Minimum number of clusters to check (inclusive).
        kmax (int): Maximum number of clusters to check (inclusive).
            Defaults to n (the number of data points).
        iterations (int): Maximum number of EM iterations.
        tol (float): EM log likelihood tolerance for early stopping.
        verbose (bool): If True, print EM log likelihood progress.

    Returns:
        tuple: (best_k, best_result, l, b) or (None, None, None, None).
            best_k (int): Best value for k based on BIC.
            best_result (tuple): (pi, m, S) for best_k.
            l (numpy.ndarray): Log likelihoods of shape (kmax-kmin+1,).
            b (numpy.ndarray): BIC values of shape (kmax-kmin+1,).
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None, None, None
    if not isinstance(kmin, int) or isinstance(kmin, bool) or kmin <= 0:
        return None, None, None, None
    if (not isinstance(iterations, int)
            or isinstance(iterations, bool)
            or iterations <= 0):
        return None, None, None, None
    if (not isinstance(tol, (int, float))
            or isinstance(tol, bool)
            or tol < 0):
        return None, None, None, None
    if not isinstance(verbose, bool):
        return None, None, None, None
    n, d = X.shape
    if kmax is None:
        kmax = n
    if not isinstance(kmax, int) or isinstance(kmax, bool) or kmax <= 0:
        return None, None, None, None
    if kmax - kmin < 1:
        return None, None, None, None
    k_range = kmax - kmin + 1
    log_l = np.zeros(k_range)
    bic = np.zeros(k_range)
    results = []
    for i, k in enumerate(range(kmin, kmax + 1)):
        pi, m, S, g, ll = expectation_maximization(
            X, k, iterations, tol, verbose)
        if pi is None:
            return None, None, None, None
        results.append((pi, m, S))
        log_l[i] = ll
        p = k * (1 + d + d * (d + 1) // 2) - 1
        bic[i] = p * np.log(n) - 2 * ll
    best_idx = np.argmin(bic)
    best_k = kmin + best_idx
    return best_k, results[best_idx], log_l, bic
