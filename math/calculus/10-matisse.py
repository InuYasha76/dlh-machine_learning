#!/usr/bin/env python3
"""This module is about polynomials."""


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.
    Args:
        poly (number): list of coeffs representing a polynomial.
    Returns:
        numbers: List of coffs representing polynomials of derivative.
    """

    if poly is None or type(poly) is not list or not poly:
        return None

    derivative = [i * n for i, n in enumerate(poly[1:], start=1)]

    if not derivative or all(k == 0 for k in derivative):
        return [0]

    return derivative


if __name__ == "__main__":
    print(poly_derivative([5, 3, 0, 1]))
