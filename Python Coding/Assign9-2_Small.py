# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:14:20 2020

@author: Nick
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


print("----------------------------------------------------")
print('Original Data')
print("----------------------------------------------------")

myData = pd.read_csv(r'titanic.csv')
print(myData.head())

print("----------------------------------------------------")
print('Dropped Columns')
print("----------------------------------------------------")

myData = myData.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
print(myData.head())

print("----------------------------------------------------")
print('Female and Male converted to 0:1')
print("----------------------------------------------------")

myData['Sex'] = myData['Sex'].map({'female':0, 'male':1})
print(myData.head())

print("----------------------------------------------------")
print('Brief Description of myData')
print("----------------------------------------------------")

description = myData.describe()
print(round(description,2))

print("----------------------------------------------------")
print('Pclass and survived vs Sex and survived Analysis')
print("----------------------------------------------------")

yx = sns.barplot(x='Pclass', y='Survived', data=myData)
yx.set_title('Pclass and Survival')
plt.show()

yxx = sns.pointplot(x='Sex', y='Survived', hue='Pclass', data=myData)
yxx.set_title('Sex and Survival')
plt.show()

print('People assigned to Pclass 1 have a high probability of surviving based on both charts')

print("----------------------------------------------------")
print('Male and Female survival regarding age Analysis')
print("----------------------------------------------------")

female = myData[myData['Sex']==0]
ax = sns.distplot(female[female['Survived']==1].Age.dropna(), bins=18, label = 'Survived', kde =False)
ax = sns.distplot(female[female['Survived']==0].Age.dropna(), bins=40, label = 'Not Survived', kde =False)
ax.set(xlabel='Female Age', ylabel='Survival / Deaths')
ax.legend()
ax.set_title('Female')
plt.show()

male = myData[myData['Sex']==1]
ax = sns.distplot(male[male['Survived']==1].Age.dropna(), bins=18, label = 'Survived', kde =False)
ax = sns.distplot(male[male['Survived']==0].Age.dropna(), bins=40, label = 'Not Survived', kde =False)
ax.set(xlabel='Male Age', ylabel='Survival / Deaths')
ax.legend()
ax.set_title('Male')
plt.show()

print('Males between the ages of 18 and 30 have a high probability of survival.')
print('Female survival is higher between ages 14 and 40.')
print('Males ages 5 and 18 have a low probability of survival.')
print('Females have a high probability of survival between ages of 5 and 18.')