#!/usr/bin/env python
import matplotlib
import pandas as pd

df = pd.read_csv('NYC_taxi.csv', parse_dates=['pickup_datetime'], nrows=500000)
print(df.head()

# nyc longtitude
nyc_min_longtitude = -74.05
nyc_min_longtitude = -74.05

# nyc latitude
nyc_min_latitude = 40.63
nyc_min_latitude = 40.85

df2 = df.copy(deep=True)

