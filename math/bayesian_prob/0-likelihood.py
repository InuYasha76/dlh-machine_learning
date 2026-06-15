#!/usr/bin/env python3
"""This module is about Bayesian probability."""


import numpy as np


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
    if n is None or type(n) is not int or n < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
        )
    if x is not None:
        x = int(x)
    if x > n:
        raise ValueError("x cannot be greater than n")
    if P is None or not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not (np.all(P >= 0) and np.all(P <= 1)):
        raise ValueError("All values in P must be in the range [0, 1]")
    binomial_coeff = 1
    for i in range(1, x + 1):
        binomial_coeff = binomial_coeff * (n - i + 1) // i
    return binomial_coeff * (P ** x) * ((1 - P) ** (n - x))


if __name__ == '__main__':
    import numpy as np
    likelihood = __import__('0-likelihood').likelihood

    P = np.linspace(0, 1, 11)
    # [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    print(likelihood(26, 130, P))
