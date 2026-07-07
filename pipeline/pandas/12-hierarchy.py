#!/usr/bin/env python3
"""This module is about pandas DataFrame manipulation."""


import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """
    Take two pandas DataFrame objects and applies following modifications:
    - Swap the two indexes, so that 'Timestamp' becomes the 1st level
      of the Multi-Index.
    - Concatenate the bitstamp and coinbase tables from timestamps
      1417411980 to 1417417980 inclusive and adds keys to the data,
      labeling rows from df2 as 'bitstamp' and rows from df1 as 'coinbase'.
    - Sort the DataFrame on the 'Timestamp' colomn in chronological order.
    Args:
        - df1 (panda Dataframe): containing coinbase data.
        - df2 (panda Dataframe): containing bitestamp data.
    Returns:
        - The concatenated, index-modified, filtered and sorted DataFrame.
    """
    if not (isinstance(df1, pd.DataFrame) and isinstance(df2, pd.DataFrame)):
        return None
    if df1.empty or df2.empty:
        return None
    if "Timestamp" not in df1.columns or "Timestamp" not in df2.columns:
        return None
    df1 = index(df1)  # df1 index: Timestamp
    df2 = index(df2)  # df2 index: Timestamp
    df = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
    # df index: key | Timestamp
    df = df.swaplevel()  # df index after swap: Timestamp | key
    df = df.sort_index()  # df sort on Timestamp
    # df filter on Timestamp 1417411980 to 1417417980
    return df.loc[1417411980:1417417980]
