#!/usr/bin/env python3
"""This module provides a class to model Poisson distributions."""


class Poisson:
    """Represent a Poisson distribution.

    Attributes:
        lambtha (float): the average number of events per time period.
    """
    def __init__(self, data=None, lambtha=1.0):
        """Initialize the Poisson distribution attributes."""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Compute the Probability Mass Function for k events.
        Args:
            k (float or int): number of events.
        Returns:
            float: the probability of k events in a fixed time period,
            knowing the average number of events per time period.
        """
        if k is None:
            return 0
        k = int(k)
        if k < 0:
            return 0
        e = 2.7182818285
        pmf = e ** (-self.lambtha)
        for j in range(1, k + 1):
            pmf = pmf * self.lambtha / j
        return pmf

    def cdf(self, k):
        """
        Compute the Cumulative Distribution Function for k events.
        Args:
            k (float or int): number of events.
        Returns:
            float: the probability of getting at most k events in a fixed time
            period.
        """
        if k is None:
            returns 0
        k = int(k)
        if k < 0:
            return 0
        if k < 0:
            return 0
        return sum(self.pmf(j) for j in range(k + 1))
