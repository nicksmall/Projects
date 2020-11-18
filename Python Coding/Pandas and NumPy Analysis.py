#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:34:09 2020

@author: nicholassmall
"""

import pandas as pd
import numpy as np

DATA_CONSTANT={'Name':['Yuan','David','Margaret','Daniel','Gina','Catherine','Chris','Jaeki','Ethan','Murphy'],
      'Score':[12.5,9,16.5,'N/A',9,20,14.5,'N/A',8,19],
      'Attempt':[1,3,2,3,2,3,1,1,2,1],
      'Pass/fail':['Yes','No','Yes','No','No','Yes','Yes','No','No','Yes']}

alpha = ['a','b','c','d','e','f','g','h','i','j']


DATA = pd.DataFrame(DATA_CONSTANT, index=alpha)
print("------------------------------------------------------------")
print("Name and Scores of David, Daniel, Catherine and Chris")
print("------------------------------------------------------------")

print(DATA.iloc[[1,3,5,6], [0,1]])

print("------------------------------------------------------------")
print("Number of attempts is greater than 2")
print("------------------------------------------------------------")

condition1 = DATA[DATA['Attempt'] > 2]
print(condition1)

print("------------------------------------------------------------")
print("Score is missing")
print("------------------------------------------------------------")

condition2 = DATA[DATA['Score'].str.contains('N/A', regex=False, case=False, na=False)]
print(condition2)

print("-----------------------------------------------------------")
print("Number of attempts is greater than 1 and Score attempts is missing")
print("------------------------------------------------------------")

condition3 = DATA[(DATA["Attempt"] > 2) & DATA['Score'].str.contains('N/A', regex=False, case=False, na=False)]
print(condition3)

print("------------------------------------------------------------")
print("Appending, Removing, Replacing Record")
print("------------------------------------------------------------")

condition4 = pd.Series({'Name' : 'Song' , 'Score' : 15.5 , 'Attempt' : '1' , 'Pass/fail' : 'Yes'} , name='k')
DATA = DATA.append(condition4)
DATA = DATA.drop('h')
DATA = DATA.replace(['Yes'], 'Pass')
DATA = DATA.replace(['No'], 'Fail')
print(DATA)
