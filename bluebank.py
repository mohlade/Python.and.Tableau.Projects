#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 14:00:15 2023

@author: Mohlade
"""

import json 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#method 1 to read json data

json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file :
    data = json.load(json_file) 
    

#transform to dataframe 
loandata = pd.DataFrame(data)

#finding unique values for the purpose column 

loandata['purpose'].unique()

#describe the data 

loandata.describe() 

#describe data for a particular column 


loandata['fico'].describe()


#using EXP() to get annual income 
income = np.exp(loandata['log.annual.inc'])
loandata['annual.income'] = income 


#applying loops to loan data 
length = len(loandata) 
ficocat = []
for x in range(0,length):
    category = loandata['fico'] [x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category < 600:
        cat = 'Poor'
    elif category >= 601 and category < 660:
        cat = 'Fair'
    elif category >= 660 and category < 700:
        cat = 'Good'
    elif category >= 700:
        cat = 'Excellent'
    else:  
        cat = 'Unknown'
    ficocat.append(cat)   
    

ficocat = pd.Series(ficocat)    

loandata['fico.category'] = ficocat
     


#df.loc as conditional statements
#df.loc[df[columnname] condition,newcolumnname]  = 'value if condition is met'

# for interest rates , a new column is wanted. rate>0.12 then high, else low 


loandata.loc[loandata['int.rate'] > 0.12,'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12,'int.rate.type'] = 'Low'
      


#number of loans/rows by fico category 

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'pink', width = 0.1)
plt.show()

pplot = loandata.groupby(['purpose']).size()
pplot.plot.bar(color = 'grey')
plt.show()


#scatter plots

ypoint = loandata['annual.income']
xpoint = loandata['dti']
plt.scatter(xpoint,ypoint)
plt.show()



# writing to csv 

loandata.to_csv('loan_clean.csv', index = True)

