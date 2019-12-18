#!/usr/bin/env python
import pandas as pd

def preprocess(df):
  
  def remove_missing_value(df): 
    df = df.dropna()
    return df
 
  def remove_fare_amount_outliers(df, lower_bound, upper_bound):
    df = df[(df['fare_amount'] >= lower_bound) & (df['fare_amount'] <= upper_bound)]
    return df

  def replace_passenger_count_outliner(df):
    mode = df['passenger_count'].mode()
    df.loc[df['passenger_count'] == 0, 'passenger_count'] = mode
    return df

  def remove_lat_long_outliers(df):
    
    # nyc longitude
    nyc_min_longitude = -74.05
    nyc_max_longitude = -73.75

    # nyc latitude
    nyc_min_latitude = 40.63
    nyc_max_latitude = 40.85

    df2 = df.copy(deep=True)
    for long in ['pickup_longitude', 'dropoff_longitude']:
      df2 = df2[(df2[long] > nyc_min_longitude) & (df2[long] < nyc_max_longitude)]

    for lat in ['pickup_latitude', 'dropoff_latitude']:
      df2 = df2[(df2[lat] > nyc_min_latitude) & (df2[lat] < nyc_max_latitude)]

    return df

  df = remove_missing_value(df)
  df = remove_fare_amount_outliner(df, lower_bound = 0, upper_bound = 100)

  df = replace_passenger_count_outliers(df)
  df = remove_lat_long_outliers(df)
  return df
