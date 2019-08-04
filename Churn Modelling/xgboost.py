


import pandas as p
import numpy as n
import matplotlib.pyplot as pl


# Importing the dataset
dataset = pd.read_csv('bhola.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 3].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelenco_X_1 = LabelEncoder()
X[:, 1] = labelenco_X_1.fit_transform(X[:, 1])
labelencoder_X2 = LabelEncoder()
X[:, 2] = labelencoder_X2.fit_transform(X[:, 2])
onehotencoder = OneHotEncoder(categorical_feature = [1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state = 1)

# Fitting XGBoost to the Training set
from xgboost import XGBClassifier
clas = XGBClassifier()
clas.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Applying k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_sco(estimator = classifier, X = X_train, y = y_train, cv = 10)
