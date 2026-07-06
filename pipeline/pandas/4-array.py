#!/usr/bin/env python3
"""This module is about pandas DataFrame."""


def array(df):
    """
    Converts the last 10 lines of columns High, Close of a dataframe
    into a numpy array.
    Args:
        df (pandas.DataFrame): contains columns 'High' and 'Close'.
    Returns:
        A numpy.ndarray containing the last 10 lines of 'High' and 'Close'.
    """
    if df is None or type(df).__name__ != "DataFrame":
        return 0
    return df[["High", "Close"]].tail(10).to_numpy()
