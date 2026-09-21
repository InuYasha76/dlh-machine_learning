#!/usr/bin/env python3
"""Module that performs the EM algorithm for a Gaussian Mixture Model."""
import numpy as np
initialize = __import__('4-initialize').initialize
expectation = __import__('6-expectation').expectation
maximization = __import__('7-maximization').maximization


def expectation_maximization(X, k, iterations=1000, tol=1e-5, verbose=False):
    """Perform the expectation maximization algorithm for a GMM.

    Args:
        X (numpy.ndarray): Dataset of shape (n, d).
        k (int): Number of clusters (positive integer).
        iterations (int): Maximum number of EM iterations.
        tol (float): Log likelihood tolerance for early stopping.
        verbose (bool): If True, print log likelihood every 10 iterations
            and after the last iteration.

    Returns:
        tuple: (pi, m, S, g, l) or (None, None, None, None, None) on failure.
            pi (numpy.ndarray): Priors of shape (k,).
            m (numpy.ndarray): Centroid means of shape (k, d).
            S (numpy.ndarray): Covariance matrices of shape (k, d, d).
            g (numpy.ndarray): Posterior probabilities of shape (k, n).
            l (float): Log likelihood of the model.
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None, None, None, None
    if not isinstance(k, int) or isinstance(k, bool) or k <= 0:
        return None, None, None, None, None
    if (not isinstance(iterations, int)
            or isinstance(iterations, bool)
            or iterations <= 0):
        return None, None, None, None, None
    if (not isinstance(tol, (int, float))
            or isinstance(tol, bool)
            or tol < 0):
        return None, None, None, None, None
    if not isinstance(verbose, bool):
        return None, None, None, None, None
    pi, m, S = initialize(X, k)
    if pi is None:
        return None, None, None, None, None
    l_prev = 0
    for i in range(iterations):
        g, log_l = expectation(X, pi, m, S)
        if g is None:
            return None, None, None, None, None
        if verbose and i % 10 == 0:
            print('Log Likelihood after {} iterations: {}'.format(
                i, round(log_l, 5)))
        if i > 0 and abs(log_l - l_prev) <= tol:
            break
        l_prev = log_l
        pi, m, S = maximization(X, g)
    if verbose and i % 10 != 0:
        print('Log Likelihood after {} iterations: {}'.format(
            i, round(log_l, 5)))
    return pi, m, S, g, log_l
