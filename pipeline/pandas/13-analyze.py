#!/usr/bin/env python3
"""This module is about pandas DataFrame manipulation."""


def analyze(df):
    """
    Computes descriptive statistics for all columns but the Timestamp column.
    Args:
        df (pandas.DataFrame): pandas dataframe to process.
    Returns:
        A new pandas DataFrame containing the descriptive statistics.
    """
    if df is None or type(df).__name__ != 'DataFrame':
        return 0

    return df.drop(columns=['Timestamp'], errors='ignore').describe()
