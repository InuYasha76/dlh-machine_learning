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

    def pmf(self, k):
        """Compute the Probability Mass Function of the Binomial distribution.
        Args:
            k (int, float): the number of successful trials to evaluate..
        Returns:
            float: the probability of getting k successes.
        """
        if k is None or not (0 <= k <= self.n):
            return 0
        n_choose_k = 1
        min_iterations = int(min(k, self.n - k))
        for i in range(1, min_iterations + 1):
            n_choose_k *= (self.n - k + i) / i
        return n_choose_k * (self.p**k) * ((1 - self.p) ** (self.n - k))
