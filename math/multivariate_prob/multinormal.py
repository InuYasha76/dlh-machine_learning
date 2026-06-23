#!/usr/bin/env python3
"""This module is about multivariate probability."""

import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution."""

    def __init__(self, data):
        """
        Initializes the MultiNormal class.
        Parameters:
            data (numpy.ndarray): Shape (d, n) containing the data set.
        Initializes:
            mean (numpy.ndarray): Shape (d, 1) containing the mean of data.
            cov (numpy.ndarray): Shape (d, d) containing the covariance matrix.
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")
        self.mean = np.mean(data, axis=1, keepdims=True)
        data_mean = data - self.mean
        self.cov = np.dot(data_mean, data_mean.T) / (n - 1)

    def pdf(self, x):
        """Calculates the PDF at a given data point x.
        Parameters:
            x (numpy.ndarray): Shape (d, 1) containing the data point.
        Returns:
            float: The value of the PDF at x.
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.mean.shape[0]
        if x.shape != (d, 1):
            raise ValueError(f"x must have the shape ({d}, 1)")
        det_sigma = np.linalg.det(self.cov)
        inv_sigma = np.linalg.inv(self.cov)
        k = 1.0 / np.sqrt(det_sigma * (2 * np.pi) ** d)
        x_mean = x - self.mean
        exponent = -0.5 * (x_mean.T @ inv_sigma @ x_mean)
        return k * np.exp(exponent.item())
