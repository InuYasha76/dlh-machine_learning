#!/usr/bin/env python3
"""This module is about pandas DataFrame manipulation."""


def flip_switch(df):
    """
    Sorts the dataframe in reverse chronological order by Timestamp
    and then transposes it.
    Args:
        df (pandas.DataFrame): pandas dataframe to perform operations on.
    Returns:
        A new pandas Dataframe sorted in reverse chronological order
        and transposed.
    """
    if df is None or type(df).__name__ != 'DataFrame':
        return 0

    df_sorted = df.sort_values(by='Timestamp', ascending=False)
    return df_sorted.T
