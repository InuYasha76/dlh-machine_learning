#!/usr/bin/env python3
"""This module contains a class Binomial to model Binomial distributions."""


class Binomial:
    """Represents a binomial distribution."""
    def __init__(self, data=None, n=1, p=0.5):
        """Initialize the binomial distribution."""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            self.n = int(n)
            if not (0 < p < 1):
                raise ValueError("p must be greater than 0 and less than 1")
            self.p = float(p)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = 0
            for data_point in data:
                variance += (data_point - mean) ** 2
            variance /= len(data)
            # moyenne = n * p, variance = n * p * (1 - p)
            self.p = float(1 - (variance / mean))
            self.n = int(round(mean / self.p))
            # for rounding compensation, recalculate p
            self.p = float(mean / self.n)
