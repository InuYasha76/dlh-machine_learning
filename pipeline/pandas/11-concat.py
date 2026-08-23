#!/usr/bin/env python3
"""This module is about pandas DataFrame manipulation."""


import pandas as pd
index_by_timestamp = __import__("10-index").index


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
    df1 = index_by_timestamp(df1)
    df2 = index_by_timestamp(df2)
    df2 = df2.loc[:1417411920]
    return pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
