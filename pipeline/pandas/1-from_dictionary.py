#!/usr/bin/env python3
"""This module is about pandas dataframes."""


import pandas as pd

my_dict = {
        "First": [0.0, 0.5, 1.0, 1.5],
        "Second": ["one", "two", "three", "four"]
}
df = pd.DataFrame(my_dict)
df.index = [chr(65 + i) for i in range(4)]
