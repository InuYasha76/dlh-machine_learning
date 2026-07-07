#!/usr/bin/env python3
"""This module is about pandas DataFrame manipulation."""


def prune(df):
    """
    Removes any entries where Close has NaN values.
    Args:
        df (pandas.DataFrame): pandas dataframe to prune.
    Returns:
        The modified DataFrame without NaN values in the 'Close' column.
    """
    if df is None or type(df).__name__ != 'DataFrame':
        return 0

    return df.dropna(subset=['Close'])
