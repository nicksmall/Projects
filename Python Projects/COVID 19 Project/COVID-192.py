#Importing libraries
import io
import pandas as pd
import requests as r
import numpy as np
import matplotlib.pyplot as plt

# Defining variables
path= 'c://users/hp/Documents/BI/'
file_out2 = 'outfileproject2.csv'
 
#First dataset
#Reading data from the web
url='https://opendata.arcgis.com/datasets/628578697fb24d8ea4c32fa0c5ae1843_0.csv'
res=r.get(url)
res.status_code
df1=pd.read_csv(io.StringIO(res.text))

#let's look at data count and column names
df1.head()
df1.columns
df1.count()

#Dropping useless column
df1.drop(['ï»¿X', 'Y','Lat','Long_','Combined_Key','Incident_Rate','Admin2','UID','Recovered','People_Tested','People_Hospitalized','ISO3'],inplace=True, axis=1)
df1
df1.columns

#let's look at count and missing data
df1.count()
df1.isnull().sum()
df1[df1['FIPS'].isnull()]

# Let`s drop the missing FIPS. We will explain our choice in the report
df1.dropna(subset=['FIPS'],how='any', inplace=True)
df1.isnull().sum()

#Second dataset
#Reading data from the web

df2=pd.read_csv('https://data.cdc.gov/api/views/k8wy-p9cg/rows.csv?accessType=DOWNLOAD&bom=true&format=true')
df2

#let's look at data count and column names
df2.head()
df2.columns
df2.count()

#Dropping useless column
df2.drop(['State', 'Data as of', 'Start week', 'End Week','FIPS State','Urban Rural Code', 'FIPS County','Non-Hispanic American Indian or Alaska Native', 'Non-Hispanic Asian','Other','Urban Rural Description','Footnote'],inplace=True, axis=1)
df2
df2.columns

#We need to drop two rows per FIPS. We will drop row containing 'Distribution of all-cause deaths (%)' 
#and 'Distribution of population (%)'
for index,row in df2.iterrows():
    index=df2[df2['Indicator']=='Distribution of all-cause deaths (%)'].index
    df2.drop(index,inplace=True )

for index,row in df2.iterrows():
    index=df2[df2['Indicator']=='Distribution of population (%)'].index
    df2.drop(index,inplace=True )
   
#let's look at count and missing data
df2.count()
df2.isnull().sum()
df2[df2[['Non-Hispanic Black','Hispanic']].isnull()]
df2

#Filling missing values for 'Black' and 'Hispanic' by their average
df2.fillna(df2.mean(), inplace = True)
df2['County Name'].replace(to_replace ="0", value ="Not Known")
df2.replace(',','', regex=True, inplace=True)

#Changing data type
df2["Total deaths"] = pd.to_numeric(df2["Total deaths"])
df2["COVID-19 Deaths"] = pd.to_numeric(df2["COVID-19 Deaths"])                                       
df2.dtypes

# Adding the death per race columns
df2['Covid_death_White']=df2['COVID-19 Deaths']*df2['Non-Hispanic White']
df2['Covid_death_Black']=df2['COVID-19 Deaths']*df2['Non-Hispanic Black']
df2['Covid_death_Hispanic']=df2['COVID-19 Deaths']*df2['Hispanic']
df2.count()

#Third dataset
#Reading data from the web
df3=pd.read_csv('https://data.cdc.gov/api/views/kn79-hsxy/rows.csv?accessType=DOWNLOAD&bom=true&format=true')
df3

#let's look at data count and column names
df3.head()
df3.columns
df3.count()

#let's look at count and missing data
df3.drop(['State', 'County name', 'First week', 'Last week', 'Date as of'],inplace=True, axis=1)
df3.count()
df3.isnull().sum()
df3

#Renaming all columns of FIPS so they match
df2.rename(columns={'FIPS Code':'FIPS'}, inplace=True)
df3.rename(columns={'FIPS County Code':'FIPS'}, inplace=True)

# Merging all data
df_merge = df1.merge(right=df2, how='left',on=['FIPS'])
df_merge = df_merge.merge( right=df3,  how='left',on=['FIPS'])
df_merge.count()
df_merge.isnull().sum()

#Filling missing values
df_merge.fillna('0', inplace = True)
df_merge['County Name'].replace(to_replace ="0", value ="Not Known")
df_merge["Total deaths"] = pd.to_numeric(df_merge["Total deaths"])
df_merge

#Correlation matrix 
df_merge.drop(['OBJECTID'],inplace=True, axis=1) 
corrmatrix = df_merge.corr()
corrmatrix

#Final Data converted to CSV
df_merge.to_csv(path+file_out2,index=False)

