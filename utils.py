#!/usr/bin/env python
import pandas as pd

def preprocess(df):
  
  def remove_missing_value(df): 
    df = df.dropna()
    return df
 
  def remove_fare_amount_outliers(df, lower_bound, upper_bound):
    df = df[(df['fare_amount'] >= lower_bound) & (df['fare_amount'] <= upper_bound)]
    return df

  def replace_passenger_count_outliers(df):
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
  df = remove_fare_amount_outliers(df, lower_bound = 0, upper_bound = 100)
  df = replace_passenger_count_outliers(df)
  df = remove_lat_long_outliers(df)
  return df


  def feature_engineer(df):
    def create_time_features(df):
      df['year'] = df['pickup_datetime'].dt.year
      df['month'] = df['pickup_datetime'].dt.month
      df['day'] = df['pickup_datetime'].dt.day
      df['day_of_week'] = df['pickup_datetime'].dt.dayofweek
      df['hour'] = df['pickup_datetime'].dt.hour
      df = df.drop(['pickup_datetime'], axis=1)
      return df

    def euc_distance(lat1, long1, lat2, long2):
      return (((lat1-lat2)**2 + (long1-long2)**2)**0.5)


    def create_pickup_dropoff_dist_features(df):
      df['travel_distance'] = euc_distance(df['pickup_latitude'], df['pickup_longitude'], df['dropoff_logitude'])
      return df


    def create_airport_dist_feature(df):
       airports = {'JFK Airport': (-73.78,40.643),
                   'Laguardia Airport': (-73.87, 40.77),
                   'Midtown': (-74.18, 40.69)}


       for airport in airports:
        df['pickup_dist_' + airport] = euc_distance(df['pickup_latitude'], df['pickup_longitude'], airports[airport[0]])
        df['dropoff_dist_' + airport] = euc_distance(df['dropoff_latitude'], df['dropoff_longitude'], airports[airport[0]])
       return df

    df = create_time_features(df)
    df = create_pickup_dropoff_dist_features(df)
    df = create_airport_dist_feature(df)
    df = df.drop(['key'], axis=1)
    
    return df
