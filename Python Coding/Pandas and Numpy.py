#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 19:17:27 2020

@author: nicholassmall
"""

import pandas as pd 
import numpy as np

print("------------------------------------------------------------")
print("Displays The first 5 rows including headers")
print("------------------------------------------------------------")

data = pd.read_csv("Athlete.csv") 
dataobject = pd.DataFrame(data)
print(dataobject.head(5))

print("------------------------------------------------------------")
print("Number of Rows and Columns")
print("------------------------------------------------------------")

data2 = np.genfromtxt('Athlete.csv',delimiter=",")
num_rows, num_cols = data2.shape
print(num_rows, num_cols)

print("------------------------------------------------------------")
print("Overwrite and saves 1993 for ID 1")
print("------------------------------------------------------------")

dataobject.set_value(0, "Year", 1993)
dataobject.to_csv("Athlete.csv", index=False)
print(dataobject.Year)

print("------------------------------------------------------------")
print("Display Weight Minus 10")
print("------------------------------------------------------------")

weight = dataobject['Weight'] - 10
print(weight)

print("------------------------------------------------------------")
print("Ratio of weight | BMI")
print("------------------------------------------------------------")

dataobject['Ratio of Weight'] = ((dataobject.Weight / (dataobject.Height) ** 2) * 10000)
print(round(dataobject,2))



# I tried switching to .iat/.at from the warning, but it gives me an error.
