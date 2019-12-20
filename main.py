#!/usr/bin/env python
import matplotlib
matplotlib.use("TkAgg")
from utils import preprocess, feature_engineer
import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import BatchNormalization
from sklearn.metrics import mean_squared_error


try:
  print("Reading in the dataset. This will take some time..")
  df = pd.read_csv('NYC_taxi.csv', parse_dates=['pickup_datetime'], nrows=500000)

except:
  print("""
    Dataset not found in your computer.
    """)
  quit()

df = preprocess(df)
df = feature_engineer(df)

df_prescaled = df.copy()
df_scaled = df.drop(['fare_amount'], axis=1)
df_scaled = scale(df_scaled)
cols = df.columns.tolist()
cols.remove('fare_amount')
