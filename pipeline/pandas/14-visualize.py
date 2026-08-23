#!/usr/bin/env python3
"""This module is about pandas DataFrame manipulation and plotting."""


import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

"""
This script performs the following:
- Import the coinbase bitcoin dataset,
- Remove the column 'Weighted_Price',
- Rename the column 'Timestamp' to 'Date',
- Convert the timestamp values to date values,
- Index the data frame on 'Date',
- Set missing values in 'Close' to the previous row value,
- Set missing values in 'High', 'Low', 'Open' to the same row's 'Close' value,
- Set missing values in 'Volume_(BTC)' and 'Volume_(Currency)' to 0,
- Plot the data from 2017 and beyond at daily intervals and group the values
  of the same day such that:
  - 'High': max,
  - 'Low': min,
  - 'Open': mean,
  - 'Close': mean,
  - 'Volume_(BTC)': sum,
  - 'Volume_(Currency)': sum,
- Return the transformed pd.DataFrame before plotting.
"""
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df = df.drop(columns=['Weighted_Price'], errors='ignored')
df = df.rename(columns={'Timestamp': 'Date'})
df['Date'] = pd.to_datetime(df['Date'], unit='s')
df = df.set_index('Date')
df['Close'] = df['Close'].ffill()
df = df.fillna(value={
    'High': df['Close'],
    'Low': df['Close'],
    'Open': df['Close'],
    'Volume_(BTC)': 0,
    'Volume_(Currency)': 0
})
start_date = pd.Timestamp('2017-01-01 00:00:00')
df_2017 = df.loc[start_date:]
df_daily = df_2017.resample('D').agg({
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
})
print(df_daily)
df_daily.plot()
plt.show()
