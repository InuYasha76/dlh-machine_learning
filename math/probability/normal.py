#!/usr/bin/env python3
"""This module provides a class to model a Normal distribution."""


class Normal:
    """Represents a Normal distribution
    Attributes:
        mean (float): the mean of the distribution.
        stddev (float): the stanrard deviation of the distribution.
    """

    def __init__(self, data=None, mean=0.0, stddev=1.0):
        """Initialize the Normal distribution attributes."""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.mean = float(sum(data) / len(data))

            cumul_sum_diff = 0
            for n in data:
                cumul_sum_diff += (n - self.mean) ** 2

            self.stddev = float((cumul_sum_diff / len(data)) ** 0.5)

    def z_score(self, x):
        """Calculates the z-score of a given x-value.
        Args:
            x (float) is the x value.
        Returns:
            z-score (float) represents how many stddev is x away from mean.
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score.
        Args:
            z (float) is the z score.
        Returns:
            float, the x-value of z.
        """
        return self.mean + (z * self.stddev)

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value.
        Args: x (float) is the x-value.
        Returns: flaot, the PDF value for x.
        """
        pi = 3.1415926536
        e = 2.7182818285
        z = self.z_score(x)
        k = 1 / (self.stddev * ((2 * pi) ** 0.5))

        return k * (e ** (-0.5 * (z ** 2)))
