# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:11:54 2019

@author: NABAJYOTI
"""






dat = p.read_csv('creditcar.csv')


print(data.columns)


data = data.sample(frac=0.1, random_state = 1)
print(data.shape)
print(data.describe())


 
data.hist(figsize = (20, 20))
plt.show()



Fraud = dat[dat['Class'] == 1]
Valid = dat[dat['Class'] == 0]

outlier_fract = len(Fraud)/float(len(Valid))
print(outlier_fract)

print('Fraud Cases: {}'.format(len(dat[dat['Class'] == 1])))
print('Valid Transactions: {}'.format(len(dat[dat['Class'] == 0])))


corrmat = data.corr()
fig = plt.figure(figsize = (12, 8))

sns.heatmap(corrmat, vmax = .8, square = True)
plt.show()


columns = data.columns.tolist()


columns = [c for c in columns if c not in ["Class"]]


target = "Class"

X = data[columns]
Y = data[target]

# Print shapes
print(X.shape)
print(Y.shape)


from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

# define random states
state = 1


classifie = {
    "Isolation_Forest": IsolationForest(max_samples=len(X),
                                        contamination=outlier_fraction,
                                        random_state=state),
    "LocalOutlierFactor": LocalOutlierFactor(
        n_neighbors=20,
        contamination=outlier_fract)}
    

plt.figure(figsize=(9, 7))
n_outliers = len(Fraud)

for i, (clf_name, clf) in enumerate(classifie.items()):
    
    
    if clf_name == "Local Outlier Factor":
        y_pred = clf.fit_predict(X)
        scores_pred = clf.negative_outlier_factor_
    else:
        clf.fit(X)
        scores_pred = clf.decision_function(X)
        y_pred = clf.predict(X)
    
     
    y_pred[y_pred == 1] = 0
    y_pred[y_pred == -1] = 1
    
    n_errors = (y_pred != Y).sum()
    
    
    
