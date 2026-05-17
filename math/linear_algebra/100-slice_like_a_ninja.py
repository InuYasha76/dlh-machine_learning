#!/usr/bin/env python3
"""This module is about ndarrays slicing."""


def np_slice(matrix, axes={}):
    """
    Slices a matrix along specific axes.
    Args:
        matrix: numpy array,
        axes: dictionary.
            key: defines the axis,
            value: defines start, end, step.
    Returns:
        A numpy array.
    """
    # Init a list of full slices (:) for every dimension of the matrix
    slice_list = [slice(None)] * matrix.ndim
    # Override the specific axes provided in the dictionary
    for axis, slice_args in axes.items():
        if axis < matrix.ndim:
            slice_list[axis] = slice(*slice_args)
    return matrix[tuple(slice_list)]
