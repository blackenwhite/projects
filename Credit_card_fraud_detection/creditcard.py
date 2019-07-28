#creditcard.py
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sklearn 
import numpy as np

#load the csv file
dataset=pd.read_csv('creditcard.csv')
data=dataset
print(data.columns)
print(data.shape)
print(data.describe())

#plot histogram of each parameter
data.hist(figsize=(20,20))
plt.show()

#determine the number of frauds in the dataset
Fraud=data[data['Class']==1]
Valid=data[data["Class"]==0]
outlier_fraction=len(Fraud)/float (len(Valid))
print("Fraud cases = {}".format(len(Fraud)))
print("Valid cases = {}".format(len(Valid)))

#correlaation matrix
corrmat=data.corr()
fig=plt.figure(figsize=(12,9))
sns.heatmap(corrmat,vmax=0.8,square=True)

#getting all the columns
columns=data.columns.tolist()
columns=[c for c in columns if c not in ["Class"]]
target="Class"
X=data[columns]
Y=data[target]

from sklearn.metrics  import accuracy_score,classification_report
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

#define a random  state
state=1

#define the outlier detection methods
classifiers={
        "Isolation Forest":IsolationForest(max_samples=len(X),contamination
                                           =outlier_fraction,random_state=state),
        "Local outlier factor":LocalOutlierFactor(n_neighbors=20,contamination=outlier_fraction)
        }

#fit the classifier
n_outliers=len(Fraud)

for i ,(clf_name,clf) in enumerate(classifiers.items()):
    #fit the data and tag the outliers
     if clf_name=="Local outlier factor":
         y_pred=clf.fit_predict(X)
         scores_pred=clf.negative_outlier_factor_
     else:
        clf.fit(X)
        scores_pred=clf.decision_function(X)
        y_pred=clf.predict(X)
        
    #Reshape the prediction values for fraud to 1 and valid to 0
     y_pred[y_pred==1]=0
     y_pred[y_pred==-1]=1
     
     n_errors=(y_pred!=Y).sum()
     #Run classification metrics
     print('{} : {}'.format(clf_name,n_errors))
     print(accuracy_score(Y,y_pred))
     print(classification_report(Y,y_pred))
     
