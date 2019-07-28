# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:27:31 2019

@author: NABAJYOTI
"""

import sys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sklearn

#Load the dataset
games=pd.read_csv("games.csv")
#print the names of the coloumns in games
print(games.columns)
print(games.shape)

#making a histogram of the average rating of the games
plt.hist(games["average_rating"])
plt.show()

#print the first row of all the games with zero scores
print (games[games["average_rating"]==0].iloc[0])

#print the first row of all the games with positive scores
print (games[games["average_rating"]>0].iloc[0])

#remove the games with no reviews
games=games[games["users_rated"]>0]

#remove those games with missing values
games=games.dropna(axis=0)

#make a histogram of all the average ratings
plt.hist(games["average_rating"])
plt.show()
#Correlation matrix
corrmat=games.corr()
fig=plt.figure(figsize=(12,9))
sns.heatmap(corrmat,vmax=0.8,square=True)




#get all the columns from the dataFrame
columns=games.columns.tolist()

#filter the columns we dont need
columns=[c for c in columns if c not in ["bayes_average_rating","average_rating","type","name","id"]]

#store the variable we'll be predicting on
target="average_rating"

#Generate training and test dataset
from sklearn.model_selection import train_test_split

#Generaate training set
train=games.sample(frac=0.8,random_state=1)

#select anything not in the trainingg set and put it in the test set
test=games.loc[~games.index.isin(train.index)]

print(test.shape)

#import linear regression model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#initialize the model class
LR=LinearRegression()

#fit the model into the training data
LR.fit(train[columns],train[target])

#Generate predictions for the test set
predictions=LR.predict(test[columns])
mean_squared_error(predictions,test[target])


from sklearn.ensemble import RandomForestRegressor
RFR=RandomForestRegressor(n_estimators=100,min_samples_leaf=10,random_state=1)
RFR.fit(train[columns],train[target])

predictions=RFR.predict(test[columns])
mean_squared_error(predictions,test[target])

rating_LR=LR.predict(test[columns].iloc[0].values.reshape(1,-1))
rating_RFR=RFR.predict(test[columns].iloc[0].values.reshape(1,-1))


    
    



























