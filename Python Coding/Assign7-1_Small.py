#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:10:35 2020

@author: nicholassmall
"""

import pandas as pd
import numpy as np

DATA_CONSTANT={'Department':['Accounting','Accounting','Sales','Sales','Sales','Sales'],
      'Employee':['Margaret','Chris','Jaeki','Yuane','Nina','Lara'],
      'Salary':[120000,87000,43500,60000,55000,73000]}
DATA_CONSTANT=pd.DataFrame(DATA_CONSTANT)



description = (DATA_CONSTANT.describe())
salary = (DATA_CONSTANT.sort_values(['Department', 'Salary'], ascending=[True, True]))

print("----------------------------------------------------")
print("Brief Description of the Data")
print("----------------------------------------------------")
print(description)
print("----------------------------------------------------")
print("Data Sorted by Department and Salary")
print("----------------------------------------------------")
print(salary)




def f(row):

    if row['Salary'] >=60000:

        return 'High'

    elif row['Salary'] >50000:

        return 'Medium'

    else:

        return 'Low'

DATA_CONSTANT['Salary Level'] = DATA_CONSTANT.apply(f, axis=1)
print("----------------------------------------------------")
print("Salary Range | High = >60k | Medium = >50k | Low = <50k")
print("----------------------------------------------------")
print(DATA_CONSTANT)
print("----------------------------------------------------")
print("Number of employees in each Salary Level")
print("----------------------------------------------------")
print(DATA_CONSTANT['Salary Level'].value_counts())
print("----------------------------------------------------")
print("Mean of the department Salaries")
print("----------------------------------------------------")
print(DATA_CONSTANT[['Department','Salary']].groupby('Department').mean())

