#!/usr/bin/env python3
"""This module is about polynomials."""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.
    Args:
        poly (number): list of coeffs representing a polynomial.
    Returns:
        numbers: new List of coeffs representing the integral of th polynomial.
    """

    if type(C) is float and C.is_integer():
        C = int(C)

    if (
            type(C) is not int or
            poly is None or type(poly) is not list or not poly
    ):
        return None

    if not all(type(p) is int or type(p) is float for p in poly):
        return None

    integral = [
            int(div) if div.is_integer() else div
            for i, coeff in enumerate(poly, start=1)
            if (div := coeff / i) or True
    ]

    integral.insert(0, C)
    return integral


if __name__ == "__main__":
    print(poly_integral([5, 3, 0, 1]))
