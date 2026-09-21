#!/usr/bin/env python3
"""Module that performs the EM algorithm for a Gaussian Mixture Model."""
import numpy as np
initialize = __import__('4-initialize').initialize
expectation = __import__('6-expectation').expectation
maximization = __import__('7-maximization').maximization

FAILURE = (None, None, None, None, None)
PRINT_EVERY = 10


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
    if (not isinstance(X, np.ndarray) or X.ndim != 2
            or not isinstance(k, int) or isinstance(k, bool) or k <= 0
            or not isinstance(iterations, int)
            or isinstance(iterations, bool) or iterations <= 0
            or not isinstance(tol, (int, float))
            or isinstance(tol, bool) or tol < 0
            or not isinstance(verbose, bool)):
        return FAILURE
    pi, m, S = initialize(X, k)
    if pi is None:
        return FAILURE
    g, log_l = expectation(X, pi, m, S)
    if g is None:
        return FAILURE
    if verbose:
        print(f'Log Likelihood after 0 iterations: {round(log_l, 5)}')
    for i in range(1, iterations + 1):
        pi, m, S = maximization(X, g)
        if pi is None:
            return FAILURE
        l_prev = log_l
        g, log_l = expectation(X, pi, m, S)
        if g is None:
            return FAILURE
        if verbose and i % PRINT_EVERY == 0:
            print(f'Log Likelihood after {i} iterations: {round(log_l, 5)}')
        if abs(log_l - l_prev) <= tol:
            break
    if verbose and i % PRINT_EVERY != 0:
        print(f'Log Likelihood after {i} iterations: {round(log_l, 5)}')
    return pi, m, S, g, log_l
