#!/usr/bin/env python3
"""This module is about pandas DataFrame."""


def slice(df):
    """
    Takes a pd.DataFrame and extracts columns High, Low, Close, Volume_(BTC)
    every 60th rows.
    Args:
        df (pandas DataFrame): the dataframe to extract data from.
    Returns:
        A sliced pandas Dataframe.
    """
    if df is None or type(df).__name__ != 'DataFrame':
        return 0
    return df.loc[::60, ["High", "Low", "Close", "Volume_(BTC)"]]
