#!/usr/bin/env python3
"""This module is about pandas DataFrame manipulation."""


import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """
    Indexes two dataframes on their Timestamp columns and concatenates df1
    to df2 up to timestamp 1417411920
    Args:
        df1 (pandas.DataFrame): coinbase dataframe.
        df2 (pandas.DataFrame): bitstamp dataframe.
    Returns:
        A concatenated pandas DataFrame with multi-index keys ("bitstamp",
        "coinbase").
    """
    if not (isinstance(df1, pd.DataFrame) and isinstance(df2, pd.DataFrame)):
        return 0
    if df1.empty or df2.empty:
        return 0
    if "Timestamp" not in df1.columns or "Timestamp" not in df2.columns:
        return 0
    df1 = index(df1)
    df2 = index(df2)
    df2 = df2.loc[:1417411920]
    return pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
