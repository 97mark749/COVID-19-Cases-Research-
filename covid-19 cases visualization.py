# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 21:57:28 2020

@author: Mark Kirby
"""
import pandas as pd
#from matplotlib import pypolt as plt


data = pd.read_csv("us-counties.csv")
print(data.head())
print(data.describe())