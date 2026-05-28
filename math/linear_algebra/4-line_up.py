#!/usr/bin/env python3
"""This module is about Linar Algebra."""


def add_arrays(arr1, arr2):
    """Adds two arrays element-wise"""
    try:
        return [sum(items) for items in zip(arr1, arr2, strict=True)]
    except ValueError:
        return None


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7, 8]
    print(add_arrays(arr1, arr2))
    print(arr1)
    print(arr2)
    print(add_arrays(arr1, [1, 2, 3]))
