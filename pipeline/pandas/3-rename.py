#!/usr/bin/env python3
"""This module is about pandas DataFrame."""


import pandas as pd


def rename(df):
    """
    Modifies a pd.DataFrame.
    Args:
        df (pandas.DataFrame): pandas dataframe to perform modifications on.
    Returns:
        A new Pandas DataFrame containing 2 columns: 'Datetime', 'Close'.
    """
    if df is None or not isinstance(df, pd.DataFrame):
        return 0
    df_renamed = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], format="%Y-%m-%d %H:%M:%S")
    return df[["Datetime", "Close"]]
