#!/usr/bin/env python3
"""This module is about Bayesian probability."""


def likelihood(x, n, P):
    """calculates the likelihood of obtaining this data given
    various hypothetical probabilities of developing severe side effects.
    Args:
        x (int, float): random veriable, the number of patients that developped
        severe side effects.
        n (int, float): the total number of patients observed.
        P (numpy.ndarray): hypothetical probabilities of developing severe
        side effects
    Returns:
        float: a 1D numpy.ndarray containing the likelihood of obtaining
        the data, x and n, for each probability in P, respectively
    """
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        raise ValueError(
                "x must be an integer that is greater than or equal to 0"
        )
    if x > n:
        raise ValueError("x cannot be greater than n")
    is_np_array = hasattr(P, '__class__') and P.__class__.__name__ == 'ndarray'
    is_1d_array = hasattr(P, 'ndim') and P.ndim == 1
    if not (is_np_array and is_1d_array):
        raise TypeError("P must be a 1D numpy.ndarray")
    if not all(0 <= p <= 1 for p in P.tolist()):
        raise ValueError("All values in P must be in the range [0, 1]")
    binomial_coeff = 1
    for i in range(1, x + 1):
        binomial_coeff = binomial_coeff * (n - i + 1) // i
    return binomial_coeff * (P ** x) * ((1 - P) ** (n - x))
