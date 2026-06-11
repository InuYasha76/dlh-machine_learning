#!/usr/bin/env python3
"""This module provides a class to model an Exponential distribution."""


class Exponential:
    """Represent an exponential distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Initialize the Exponential distribution parameters."""
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
            self.lambtha = float(len(data) / sum(data))

    def pdf(self, x):
        """
        Compute the value of the Probability Density Function
        for a given time period.
        Args:
            x (float): a time period [0; inf[
        Returns:
            float: probability the event happens at x time unit..
        """
        if x is None or x < 0:
            return 0
        e = 2.7182818285
        return self.lambtha * (e ** (-self.lambtha * x))

    def cdf(self, x):
        """
        Compute the value of the Cumulative Distribution Function
        for a time period.
        Args:
            x (float): a time period, must be >= 0.
        Returns:
            float: probability the event happens before x time unit.
        """
        if x is None or x < 0:
            return 0
        e = 2.7182818285
        return 1 - (e ** (-self.lambtha * x))
