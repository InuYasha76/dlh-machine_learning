#!/usr/bin/env python3
"""This module is about pandas DataFrame."""


import pandas as pd


def from_file(filename, delimiter):
    """
    Loads data from a file as a pd.DataFrame.
    Args:
        filename (string): path to file to load.
        delimiter (string): separator used to delimit fields.
    Returns:
        Pandas DataFrame containing the loaded data.
    """
    if filename is None or not isinstance(filename, str):
        return 0
    try:
        if delimiter is None:
            df = pd.read_csv(filename, sep=delimiter, engine="python")
        else:
            df = pd.read_csv(filename, sep=delimiter)
    except Exception:
        return 0
    return df
