#!/usr/bin/env python3
"""Module that calculates the PDF of a Gaussian distribution."""
import numpy as np


def pdf(X, m, S):
    """Calculate the probability density function of a Gaussian distribution.

    Args:
        X (numpy.ndarray): Data points of shape (n, d).
        m (numpy.ndarray): Mean of the distribution of shape (d,).
        S (numpy.ndarray): Covariance matrix of shape (d, d).

    Returns:
        numpy.ndarray: PDF values of shape (n,) with minimum value 1e-300,
            or None on failure.
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None
    m = np.asarray(m)
    S = np.asarray(S)
    if m.ndim != 1:
        return None
    if S.ndim != 2:
        return None
    d = m.shape[0]
    if X.shape[1] != d or S.shape != (d, d):
        return None
    S_inv = np.linalg.inv(S)
    det = np.linalg.det(S)
    diff = X - m
    coeff = 1 / (((2 * np.pi) ** (d / 2)) * np.sqrt(det))
    mahal = np.sum((diff @ S_inv) * diff, axis=1)
    return np.maximum(coeff * np.exp(-0.5 * mahal), 1e-300)
