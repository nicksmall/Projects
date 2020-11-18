# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 17:36:42 2020

@author: Nick
"""


#declaring necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA = {'State':['CA','TX','FL','NY','IL','PA'], 'TimeZone':['PST','CST','EST','EST','CST','EST'],
'Population':[39250,27862,20612,19745,12801,12784],'Percentage':[12,9,6,6,4,4]}
 

print("----------------------------------------------------")
print('Displays Data Frame')
print("----------------------------------------------------") 
# DataFrame
dataobject = pd.DataFrame(DATA)
print(dataobject)

print("----------------------------------------------------")
print('Sorted Estimated population of the year 2016')
print("----------------------------------------------------")

dataobject = dataobject.sort_values(['State','TimeZone'],ascending=[True,True])
print(dataobject)

print("----------------------------------------------------")
print('Population in Real Numbers')
print("----------------------------------------------------")

dataobject['Pop in Real Numbers'] = (dataobject.Population * 1000)
print(dataobject)

print("----------------------------------------------------")
print('Avg, Min, and Max Population of each State')
print("----------------------------------------------------")

AVG = dataobject["Pop in Real Numbers"].mean()
MIN = dataobject["Pop in Real Numbers"].min()
MAX =  dataobject["Pop in Real Numbers"].max()
print((round(AVG,2), MIN, MAX,))

print("----------------------------------------------------")
print('Population of Each Time Zone')
print("----------------------------------------------------")

DATA2 = dataobject.groupby("TimeZone")
TimeZone_Group = DATA2["Pop in Real Numbers"].sum()
print(TimeZone_Group)

print("----------------------------------------------------")
print('Bar Plot of States Populations')
print("----------------------------------------------------")

y = dataobject[['State','Population']].plot(kind='bar', title ="Population", figsize=(15, 10), legend=True, fontsize=15, hatch='/', color='red')
y.set_xlabel("State", fontsize=12)
y.set_ylabel("In Thousands", fontsize=12)
plt.xticks(dataobject.index,dataobject["State"].values)
plt.show()

print("----------------------------------------------------")
print('Pie Chart of States Populations')
print("----------------------------------------------------")

explode = (0.1, 0, 0, 0, 0, 0)
piechart = dataobject.plot.pie(y='Population', labels=dataobject['State'], title="Population", legend=False, shadow=True, explode=explode)
plt.show()
