#!/usr/bin/python

# Assumption:
#	A linear relationship between Size and Cost of a pizza, we can use Linear Regression model to predict the price of a pizza.

import numpy as np
from sklearn.linear_model import LinearRegression

# Diameter of Pizza in X
# Cost of Pizza in y
# Diameter and Cost are "parameters" of a model


X = np.array([[6],[8],[10],[14],[18]])
y = np.array([[7],[9],[13],[17.5],[18]])

model = LinearRegression()
model.fit(X,y)

print 'A 12" pizza would cost $%.2f'%(model.predict([12])[0])

