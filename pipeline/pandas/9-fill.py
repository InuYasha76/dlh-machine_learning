#!/usr/bin/env python3
"""This module is about pandas DataFrame manipulation."""


def fill(df):
    """
    Fills missing values in a dataframe.
    Args:
        df (pandas.DataFrame): pandas dataframe with NaN values.
    Returns:
        A NaN cleaned pandas DataFrame.
    """
    if df is None or type(df).__name__ != 'DataFrame':
        return 0
    df = df.drop(columns=['Weighted_Price'])
    df['Close'] = df['Close'].ffill()
    df = df.fillna(value={
        'High': df['Close'],
        'Low': df['Close'],
        'Open': df['Close'],
        'Volume_(BTC)': 0,
        'Volume_(Currency)': 0
    })
    return df
