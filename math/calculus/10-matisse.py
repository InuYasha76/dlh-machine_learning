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

    if not poly or not isinstance(poly, list):
        return None

    return [i * n for i, n in enumerate(poly)]


if __name__ == "__main__":
    print(poly_derivative([5, 3, 0, 1]))
