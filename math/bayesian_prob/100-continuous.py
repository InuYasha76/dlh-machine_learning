#!/usr/bin/env python3
"""This module is about bayesian probability."""


from scipy import special


def posterior(x, n, p1, p2):
    """calculates the posterior probability that the severe side-effect
    probability is between p1 and p2, given x occurrences in n patients
    Args:
        x (int): the number of patients that developed severe side effects.
        n (int): the total number of patients observed.
        p1 (float): lower bound of the range [p1, p2].
        p2 (float): upper bound of the range [p1, p2].
    Returns:
        (float): the posterior probability that p is within the range [p1, p2]
        given x and n.
    """
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        raise ValueError(
                "x must be an integer that is greater than or equal to 0"
        )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not (type(p1) is float and 0 <= p1 <= 1):
        raise ValueError("p1 must be a float in the range [0, 1]")
    if not (type(p2) is float and 0 <= p2 <= 1):
        raise ValueError("p2 must be a float in the range [0, 1]")
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")
    alpha = x + 1
    beta = n - x + 1
    cdf_p2 = special.betainc(alpha, beta, p2)
    cdf_p1 = special.betainc(alpha, beta, p1)
    return cdf_p2 - cdf_p1
