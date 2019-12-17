#!/usr/bin/env python
import pandas as pd

def preprocess(df):
  
  def remove_missing_value(df): 
    df = df.dropna()
    return df
