#!/usr/bin/env python3
"""This module is about lists. Assumes type int, float non empty lists.."""


def cat_arrays(arr1, arr2):
    """Concatenates two arrays."""
    if isinstance(arr1, list) and isinstance(arr2, list):
        return arr1 + arr2
    return None


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8]
    print(cat_arrays(arr1, arr2))
    print(arr1)
    print(arr2)
    print()
    arr3 = None
    print(arr3)
    print(arr2)
    print(cat_arrays(None, arr2))
