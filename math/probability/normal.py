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
