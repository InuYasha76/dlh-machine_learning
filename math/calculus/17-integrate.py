#!/usr/bin/env python3
"""This module is about polynomials."""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.
    Args:
        poly (list): list of coeffs representing a polynomial.
        C (int): the integration constant.
    Returns:
        list: new List of coeffs representing the integral of th polynomial.
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

    integral = [C]
    for i, coeff in enumerate(poly, start=1):
        div = coeff / i
        integral.append(int(div) if div == int(div) else div)

    while len(integral) > 0 and integral[-1] == 0:
        integral.pop()

    return integral


if __name__ == "__main__":
    print(poly_integral([5, 3, 0, 1]))
