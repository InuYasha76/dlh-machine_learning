#!/usr/bin/env python3
"""This module contains a class to model Binomial distributions."""


class Binomial:
    """Represents a binomial distribution.

    Attributes:
        n (int):    the number of trials.
        p (float):  the probability of success per trial.
    """

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize the Binomial distribution attributes."""
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
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            # mean = n * p, variance = n * p * (1 - p)
            self.p = float(1 - (variance / mean))
            self.n = int(round(mean / self.p))
            # recalculate p to compensate for rounding of n
            self.p = float(mean / self.n)

    def pmf(self, k):
        """Compute the Probability Mass Function for k successes.
        Args:
            k (int, float): the number of successful trials to evaluate..
        Returns:
            float: the probability of getting exactly k successes in n trials.
        """
        if k is None:
            return 0
        k = int(k)
        if not (0 <= k <= self.n):
            return 0
        n_choose_k = 1
        min_iterations = int(min(k, self.n - k))
        for i in range(1, min_iterations + 1):
            n_choose_k = n_choose_k * (self.n - min_iterations + i) / i
        return n_choose_k * (self.p**k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Compute the Cumulative Distribution Function for k successes.
        Args:
            k (int, float): the number of successful trials to evaluate.
        Returns:
            float: the cumulative probability of getting at most k successes
            in n trials.
        """
        if k is None:
            return 0
        k = int(k)
        if k < 0:
            return 0
        if k >= self.n:
            return 1.0
        return sum(self.pmf(i) for i in range(k + 1))
