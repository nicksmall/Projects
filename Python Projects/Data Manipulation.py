

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA = {'Year':[2002,2002,2003,2003,2003,2004,2004,2005,2005], 'Name':['Tom','Joe','Tom','Joe','Tom','Tom','Joe','Tom','Joe'],
'Salary':[54000,50000,56000,50000,56000,58120,57100,58120,60300],'Interest_Rate':[0.10,0.10,0.15,0.10,0.15,0.16,0.16,0.16,0.20]}


dataobject = pd.DataFrame(DATA)


print("----------------------------------------------------")
print('First 6 rows of the table')
print("----------------------------------------------------")

dataobject = pd.DataFrame(DATA)
print(dataobject.head(6))

print("----------------------------------------------------")
print('Sorted by Year in Chronological order')
print("----------------------------------------------------")

dataobject = dataobject.sort_values(['Year'],ascending=[True])
print(dataobject)

print("----------------------------------------------------")
print('Brief Description')
print("----------------------------------------------------")

description = dataobject.describe()
print(round(description,2))

print("----------------------------------------------------")
print('Salary Holding')
print("----------------------------------------------------")

dataobject['Holding'] = (((dataobject.Salary * (dataobject.Interest_Rate)) + 1500))
dataobject
print(dataobject)

print("----------------------------------------------------")
print('Sum of Holding for Tom and Joe')
print("----------------------------------------------------")

DATA2 = dataobject.groupby("Name")
sum_holding = DATA2["Holding"].sum()
print(sum_holding)

print("----------------------------------------------------")
print('Holdings Change over 4 years')
print("----------------------------------------------------")

dataobject.groupby(["Name"])["Holding"].plot(title="Holdings Change over 4 years",legend=True)
plt.xticks(dataobject.index,dataobject["Year"].values)
plt.xlabel('Year')
plt.ylabel('Holdings')
plt.show()
