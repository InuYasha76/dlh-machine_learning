#!/usr/bin/env python3
"""This module provides a class to model an Exponential distribution."""


class Exponential:
    """Represents an exponential distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Initialize the Exponential distribution parameters."""
        if data is None:
            if lambtha < 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = lambtha
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(len(data) / sum(data))
