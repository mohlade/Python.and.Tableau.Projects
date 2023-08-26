#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 14:52:12 2023

@author: Mohlade
"""

import pandas as pd 

# file_name = pd.read_csv('file.csv') <--- format

data = pd.read_csv('transaction2.csv')


data = pd.read_csv('transaction2.csv', sep=';')

#working with calculations

#Defining variables

CostPerItem = 11.73
SellingPricePerItem =  21.11
NumberOfItemsPurchased = 6

# Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerTransaction= ProfitPerItem*NumberOfItemsPurchased

 #CostPerTransaction Column Calculation 
 #variable= dataframe['column_name']
 
 
CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased  

#adding new column to DataFrame

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales Per Transaction 

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data ['NumberOfItemsPurchased']

#Profit Per Transaction Calculation = Sales - Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Mark-up = (Sales-Cost)/cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

#Rounding Markup 

roundmarkup =  round(data['Markup'],2)

data['Markup'] = roundmarkup

#combining data fields

#my_date = data['Day'] + '-' data['Month'] + '-' data['Year']


#change column type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
my_date = day+'-' + data['Month'] + '-' + year

data['Date'] = my_date


#using iloc to view specific columns.rows
data.iloc[0] #views with row with index 0 
data.iloc[-5] # views last 5 rows

data.iloc[:,2] # all rows second column 
data.iloc[4,2]#fourth row second column 

#using split to split the clients keywords field

#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',', expand = True)

#creating columns for split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['ClientStatus'] = split_col[2]


#using the replace function 

data['ClientAge'] = data['ClientAge'].str.replace('[', '')

data['ClientStatus'] = data['ClientStatus'].str.replace(']', '')

#using lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files 
#bringing a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')
 
#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')


#dropping columns
#df = df.drop('columnames' , axis = 1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Month','Year'], axis = 1)

#export to a csv file 

data.to_csv('ValueInc_Cleaned.csv', index = False)

#summary  of the data

data.info()













