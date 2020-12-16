#Importing libraries
import io
import pandas as pd 
import numpy as np
import requests as r

# Defining variables
url1 ='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url2 ='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url3 ='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
path= 'c://users/hp/Documents/BI/'
file_out1 = 'outfileproject1.csv'

#Reading data from the web
#Pulling confirmed covid cases data
res=r.get(url1)
res.status_code
df1=pd.read_csv(io.StringIO(res.text))
df1.count()
df1

#Pulling death covid data
res=r.get(url2)
res.status_code
df2=pd.read_csv(io.StringIO(res.text))
df2.count()
df2

#Pulling recovered covid data
res=r.get(url3)
res.status_code
df3=pd.read_csv(io.StringIO(res.text))
df3.count()
df3

#Let`s pivot our datasets. Making rows columns and columns rows
dates = df1.columns[4:]
df1_pivot = df1.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars=dates, var_name='Date', value_name='Confirmed')
df2_pivot = df2.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars=dates, var_name='Date', value_name='Deaths')
df3_pivot = df3.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars=dates, var_name='Date', value_name='Recovered')
df3_pivot = df3_pivot[df3_pivot['Country/Region']!='Canada']

#Data Cleaning
#Dropping useless column
df1_pivot.drop(['Lat','Long'],inplace=True, axis=1)
df1_pivot
df1_pivot.columns
df1_pivot.count()

df2_pivot.drop(['Lat','Long'],inplace=True, axis=1)
df2_pivot
df2_pivot.columns

df3_pivot.drop(['Lat','Long'],inplace=True, axis=1)
df3_pivot
df3_pivot.columns
df3_pivot = df3_pivot[df3_pivot['Country/Region']!='Canada']

#Merging Data 1,2,3
df_final = df1_pivot.merge(right=df2_pivot, how='left', on=['Province/State','Country/Region', 'Date'])
df_final = df_final.merge(right=df3_pivot, how='left',on=['Province/State','Country/Region', 'Date'])
df_final.count()
df_final.isnull().sum()
df_final[df_final['Recovered'].isnull()]
df_final.shape

#Cleaning Datasets
df_final['Recovered'] = df_final['Recovered'].fillna(0)
df_final['Date'] = pd.to_datetime(df_final['Date'])
df_final.count
df_final.columns

#Adding New Columns, grouping, and additional cleaning 
#Creates the Active Column and inputs the values
df_final['Active'] = df_final['Confirmed'] - df_final['Deaths'] - df_final['Recovered']

#Groups/Sums/Reset the index on the following columns
df_final_group = df_final.groupby(['Date', 'Country/Region'])['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()

#Grouped again
w = df_final_group.groupby(['Country/Region', 'Date', ])['Confirmed', 'Deaths', 'Recovered']

#Used to calculate the value of New Cases, New Deaths and, New recovered using .diff
w = w.sum().diff().reset_index()

#where the country region doesn't shift, it's replaced with the empty cell of NaN
s = w['Country/Region'] != w['Country/Region'].shift(1)
w.loc[s, 'Confirmed'] = np.nan
w.loc[s, 'Deaths'] = np.nan
w.loc[s, 'Recovered'] = np.nan

#Renames the previous columns confirmed, deaths and recovered into the ones below
w.columns = ['Country/Region', 'Date', 'New cases', 'New deaths', 'New recovered']

#Merges the new columns with values on the Country and Date
df_final_group = pd.merge(df_final_group, w, on=['Country/Region', 'Date'])

#Fill all NaN space with 0
df_final_group = df_final_group.fillna(0)
columns = ['New cases', 'New deaths', 'New recovered']

#Converts the data type of the columns specified above into INT
df_final_group[columns] = df_final_group[columns].astype('int')

#Replaces values that are lower than 0 with a 0 so it doesn't throw off the data
df_final_group['New cases'] = df_final_group['New cases'].apply(lambda x: 0 if x<0 else x)

#Final Data converted to CSV
df_final.to_csv(path+file_out1,index=False)
