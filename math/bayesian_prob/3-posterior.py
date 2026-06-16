#!/usr/bin/env python3
"""This module is about bayesian probability."""


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
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        raise ValueError(
                "x must be an integer that is greater than or equal to 0"
        )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    binomial_coeff = 1
    for i in range(1, x + 1):
        binomial_coeff = binomial_coeff * (n - i + 1) / i
    return binomial_coeff * (P**x) * ((1 - P) ** (n - x))


def intersection(x, n, P, Pr):
    """calculates the intersection of obtaining this data
    with the various hypothetical probabilities:
    Args:
        x (int): the number of patients that developed severe side effects.
        n (int): the total number of patients observed.
        P (numpy.ndarray): 1D array containing various hypothetical
        probabilities of developing severe side effects.
        Pr (numpy.ndarray): 1D array containing the prior beliefs of P.
    Returns:
        (numpy.ndarray): aa 1D array containing the intersection
        of obtaining x and n with each probability in P, respectively.
    """
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        raise ValueError(
                "x must be an integer that is greater than or equal to 0"
        )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or P.shape != Pr.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    for p in P:
        if not (0 <= p <= 1):
            raise ValueError("All values in P must be in the range [0, 1]")
    for pr in Pr:
        if not (0 <= pr <= 1):
            raise ValueError("All values in Pr must be in the range [0, 1]")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1.0):
        raise ValueError("Pr must sum to 1")
    return likelihood(x, n, P) * Pr


def marginal(x, n, P, Pr):
    """calculates the marginal probability of obtaining the data
    with the various hypothetical probabilities:
    Args:
        x (int): the number of patients that developed severe side effects.
        n (int): the total number of patients observed.
        P (numpy.ndarray): 1D array containing various hypothetical
        probabilities of developing severe side effects.
        Pr (numpy.ndarray): 1D array containing the prior beliefs of P.
    Returns:
        (numpy.ndarray): the marginal probability of obtaining x and n.
    """
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        raise ValueError(
                "x must be an integer that is greater than or equal to 0"
        )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or P.shape != Pr.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    for p in P:
        if not (0 <= p <= 1):
            raise ValueError("All values in P must be in the range [0, 1]")
    for pr in Pr:
        if not (0 <= pr <= 1):
            raise ValueError("All values in Pr must be in the range [0, 1]")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1.0):
        raise ValueError("Pr must sum to 1")
    return np.sum(likelihood(x, n, P) * Pr)


def posterior(x, n, P, Pr):
    """calculates the posterior probability for the various hypothetical
    probabilities of developing severe side effects given the data.
    Args:
        x (int): the number of patients that developed severe side effects.
        n (int): the total number of patients observed.
        P (numpy.ndarray): 1D array containing various hypothetical
        probabilities of developing severe side effects.
        Pr (numpy.ndarray): 1D array containing the prior beliefs of P.
    Returns:
        (numpy.ndarray): the marginal probability of obtaining x and n.
    """
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        raise ValueError(
                "x must be an integer that is greater than or equal to 0"
        )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or P.shape != Pr.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    for p in P:
        if not (0 <= p <= 1):
            raise ValueError("All values in P must be in the range [0, 1]")
    for pr in Pr:
        if not (0 <= pr <= 1):
            raise ValueError("All values in Pr must be in the range [0, 1]")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1.0):
        raise ValueError("Pr must sum to 1")
    return (likelihood(x, n, P) * Pr) / marginal(x, n, P, Pr)
