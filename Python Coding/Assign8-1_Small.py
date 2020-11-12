# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:54:05 2020

@author: Nick
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns;
CITY_TEMP = {'CityA_High':[33,37,44,56,67,75,79,78,71,60,50,38], 'CityA_Low':[19,22,28,38,47,57,62,60,53,42,35,24],
'CityB_High':[54,59,67,76,83,91,93,94,84,75,63,55],'CityB_Low':[26,30,37,46,56,65,69,67,59,48,36,28]}
  
# DataFrame
dataobject = pd.DataFrame(CITY_TEMP)

# Line Plot

cityA_temp=dataobject[['CityA_High','CityA_Low']]
cityA_temp.plot.line(title='Temperature Change Over A Year')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.show()

# Bar plot

Y = np.arange(12)
fig = plt.figure()
y = fig.add_axes([0,0,1,1])
y.bar( Y+0.00, cityA_temp['CityA_High'], color = 'black', width = 0.45)
y.bar( Y+0.25, cityA_temp['CityA_Low'], color = 'red', width = 0.25)
y.set_title('City A High temperature vs Low temperature')
y.set_ylabel('Temperature')
y.set_xlabel('Month')
y.set_xticks(Y + 0.25 / 2)
y.set_xticklabels(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
y.legend(labels=['CityA High', 'CityA Low'])
plt.show()


# Scatter plot
plt.scatter(dataobject['CityA_High'],dataobject['CityB_High'])
plt.scatter(dataobject['CityA_Low'],dataobject['CityB_Low'])
plt.xlabel('City A High and Low Temperatures')
plt.ylabel('City B High and Low Temperatures')
plt.show()