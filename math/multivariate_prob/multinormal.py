import numpy as np
"""This module is about multivariate probability."""


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
