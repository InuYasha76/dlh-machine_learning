#!/usr/bin/env python3
"""This module is about pandas."""


import pandas as pd


def from_numpy(array):
    """
    creates a pd.DataFrame from a np.ndarray
    Args:
        array (np.ndarray): array input to turn into a pandas dataframe.
    Returns:
        A dataframe (pandas.DataFrame): with alphabetically ordered and
        capitalized columns names.
    """
    if array is None or type(array).__name__ != "ndarray":
        return 0
    col_number = array.shape[1]
    if col_number > 26:
        return 0
    df = pd.DataFrame(array)
    if col_number > 0:
        df.columns = [chr(65 + i) for i in range(col_number)]
    return df
