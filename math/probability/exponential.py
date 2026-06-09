#!/usr/bin/env python3
"""This module provides a class to model an Exponential distribution."""


class Exponential:
    """Represents an exponential distribution."""

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
        Calculates the value of the PDF for a given time period.
        Args:
            x (float): a time period [0; inf[
        Returns:
            float, the pdf value for x
        """
        if x < 0:
            return 0
        e = 2.7182818285

        return self.lambtha * (e ** (-self.lambtha * x))

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given time period.
        Args:
            x (float): a time period [0; inf[
        Returns:
            float, the cdf value for x
        """
        if x < 0:
            return 0
        e = 2.7182818285

        return 1 - (e ** (-self.lambtha * x))
