#!/usr/bin/env python3
"""This module is about pandas DataFrame manipulation."""


import pandas as pd


def concat(df1, df2):
    """
    Indexes two dataframes on their Timestamp columns and concatenates df1
    to df2.
    Args:
        df1 (pandas.DataFrame): coinbase dataframe.
        df2 (pandas.DataFrame): bitstamp dataframe.
    Returns:
        A concatenated pandas DataFrame with multi-index keys.
    """
    index = __import__("10-index").index
    df1 = index(df1)
    df2 = index(df2)
    df2 = df2.loc[:1417411920]
    return pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
