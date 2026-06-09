#!/usr/bin/env python3
"""This module is about the Poisson's distribution."""


class Poisson:
    """This class is about Poisson law."""

    def __init__(self, data=None, lambtha=1.0):
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
        """instance method, computes the PMF given k successes."""
        if k < 0:
            return 0.0
        k = int(k)
        e = 2.7182818285
        pmf = e ** (-self.lambtha)

        if k == 0:
            return pmf

        for j in range(1, k + 1):
            pmf = pmf * self.lambtha / j

        return pmf
