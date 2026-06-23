#!/usr/bin/env python3
"""This module is about multivariate probability."""


import numpy as np


def mean_cov(X):
    """
    Calculates the mean and covariance of a data set.
    Args::
        X (numpy.ndarray): Shape (n, d) containing the data set.
    Returns:
        mean (numpy.ndarray): Shape (1, d) containing the mean of the data set.
        cov (numpy.ndarray): Shape (d, d) containing the covariance matrix.
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    n, d = X.shape
    if n < 2:
        raise ValueError("X must contain multiple data points")
    mean = np.mean(X, axis=0, keepdims=True)
    X_mean = X - mean
    cov = np.dot(X_mean.T, X_mean) / (n - 1)
    return mean, cov
