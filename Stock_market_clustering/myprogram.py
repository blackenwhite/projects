# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:28:00 2019

@author: NABAJYOTI
"""
# Importing the libraries
from pandas_datareader import data
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime

#define the instruments to download
companies_dict={
        'Amazon':'AMZN',
        'Apple' :'AAPL',
        'Walgreen':'WBA',
      #  'Northrop Gunnman':'NOP',
        'Boeing':'BA',
        'Lockheed Martin':'LMT',
        'McDonalds':'MCD',
        'Intel':'INTC',
        'Navistar':'NAV',
        'IBM':'IBM',
        'Texas Instruments':'TXN',
        'MasterCard':'MA',
        'Microsoft':'MSFT',
        'Symantec':'SYMC',
        'American Express':'AXP',
        'Pepsi':'PEP',
        'Coca Cola':'KO',
        'Johnson and Johnson':'JNJ',
        'Toyota':'TM',
        'Honda':'HMC',
       # 'Mistubishi':'MSBY',
        'Sony':'SNE',
        'Exxon':'XOM',
        'Chevron':'CVX',
        'Valeo Energy':'VLO',
        'Ford':'F',
        'Bank of America':'BAC'
        }
companies=sorted(companies_dict.items(),key=lambda x:x[1])
print(companies)

#Define the online source to use
data_source='yahoo'

#define the start and end dates
start_date='1/1/2015'
end_date='31/12/2017'

#use the pandas.data.DataReader to load the desired stack data
values=(companies_dict.values())

#panel_data=data.DataReader(list(values),data_source,start_date,end_date)
panel_data1=data.DataReader(list(values), data_source='yahoo', start=start_date, end=end_date, retry_count=3, pause=0.1,
           session=None, access_key=None)
print(panel_data1.axes)

#find stock open and stock data values
stock_open1=panel_data1.loc[:,'Open']
#stock_close=panel_data1.loc['Close']
#print(stock_close.iloc[0])
stock_close1=panel_data1.loc[:,'Close']
print(stock_close1.iloc[100])

#calculate daily stock movement
stock_close=np.array(stock_close1).T
stock_open=np.array(stock_open1).T

row,col=stock_close.shape
movements=np.zeros([row,col])

for i in range(0,row):
    movements[i,:]=np.subtract(stock_close[i,:],stock_open[i,:])

for i in range(len(companies)):
    print('Company : {}, Change : {}'.format(companies[i][0],sum(movements[i][:])));


#Kmeans and PCA
#Visualization -plot stack movements


#import Normalizer
from sklearn.preprocessing import Normalizer

#Create the Normalizer
norm=Normalizer()
new=norm.fit_transform(movements)

plt.clf
plt.figure(figsize=(10,10))
ax1=plt.subplot(221)
plt.plot(new[0][:])
plt.title(companies[19][0])

plt.subplot(222)
plt.plot(new[1][:])
plt.title(companies[1][0])
plt.show()

from sklearn.pipeline import make_pipeline
from sklearn.cluster import KMeans

#Create a Kmeans model-10 clusters
kmeans=KMeans(n_clusters=4,max_iter=100)
normal=Normalizer()
#maake a pipeline chaining normalizer and Kmeans
pipeline=make_pipeline(normal,kmeans)

#Fit pipeline to daily Stock movements
pipeline.fit(movements)
pipeline.fit(new)
print(kmeans.inertia_)

#predict the cluster labels
labels=pipeline.predict(new)

#Create a DataFrame aligning labels and companies

df=pd.DataFrame({'Label':labels,'companies':companies})

#Display df sorted by cluster label
print(df.sort_values('Label'))

from sklearn.decomposition import PCA
reduced_data=PCA(n_components=2).fit_transform(new)
kmeans=KMeans(n_clusters=4,max_iter=100)
kmeans.fit(reduced_data)
labels=kmeans.predict(reduced_data)

#Create a DataFrame aligning labels and companies

df=pd.DataFrame({'Label':labels,'companies':companies})
print(df.sort_values('Label'))


 

