#!/usr/bin/env python3
"""This module is about pandas DataFrame manipulation."""


def high(df):
    """
    Sorts a pandas dataframe by the High price in descending order.
    Args:
        df (pandas.DataFrame): pandas dataframe to sort.
    Returns:
        A new pandas DataFrame sorted by 'High' in descending order.
    """
    if df is None or type(df).__name__ != 'DataFrame':
        return 0

    return df.sort_values(by='High', ascending=False)
