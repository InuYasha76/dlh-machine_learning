#!/usr/bin/env python3
"""This module is about pandas DataFrame manipulation."""


def index(df):
    """
    Sets the Timestamp column as the index of the dataframe.
    Args:
        df (pandas.DataFrame): pandas dataframe to process.
    Returns:
        A new pandas DataFrame with the 'Timestamp' coumn as index.
    """
    if df is None or type(df).__name__ != 'DataFrame':
        return 0
    return df.set_index('Timestamp')
