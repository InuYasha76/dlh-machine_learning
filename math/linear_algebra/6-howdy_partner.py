#!/usr/bin/python3
"""This module is about Arrays."""


def cat_arrays(arr1, arr2):
    if not isinstance(arr1, list):
        arr1 = []
    if not isinstance(arr2, list):
        arr2 = []
    return arr1 + arr2


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
