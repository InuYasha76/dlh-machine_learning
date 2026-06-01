#!/usr/bin/env python3
"""This module is about Calculus."""


def summation_i_squared(n):
    """Sum n squared numbers.
    Args:
        n (int): last number in the serie.
    Returns:
        int: sum of the first n squared numbers.
    """
    if not n or not isinstance(n, int) or n < 0:
        return None

    if n == 0:
        return 0

    return (n * n) + summation_i_squared(n - 1)


if __name__ == "__main__":
    print(summation_i_squared(5))
