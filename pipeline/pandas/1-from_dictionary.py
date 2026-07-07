#!/usr/bin/env python3
"""This module is about pandas dataframes."""


import pandas as pd

data = {
        "First": [0.0, 0.5, 1.0, 1.5],
        "Second": ["one", "two", "three", "four"]
}
index = [chr(65 + i) for i in range(4)] 
df = pd.DataFrame(data, index)
print(df)
