#!/usr/bin/python

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier


iris = load_iris()

print iris.feature_names
print iris.target_names

# Requirements for Scikit-learn -
# 1. Feature and Response should be separate objects
# 2. Feature and Response should be numeric
# 3. Feature and Response should be Numpy arrays
# 4. Feature and Response should have specific shapes i.e. rows and columns

# Convention is to store Feature in 'X' and response in 'y'

X = iris.data
y = iris.target

knn = KNeighborsClassifier(n_neighbors=1)

#print knn

# fit the model with training data (i.e. model training)
knn.fit(X,y)

print iris.target_names[knn.predict([2,3,4,5])[0]]
