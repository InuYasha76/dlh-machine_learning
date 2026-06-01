#!/usr/bin/env python3
"""This module is about Calculus."""


def summation_i_squared(n):
    """Sums n numbers squared.
    Args:
        n (int): last number in the series.
    Returns:
        int: sum of the first n numbers squared.
    """
    if type(n) is float and n.is_integer():
        n = int(n)
    if n is None or type(n) is bool or type(n) is not int or n < 0:
        return None
    return (n * (n + 1) * (2 * n + 1)) // 6
