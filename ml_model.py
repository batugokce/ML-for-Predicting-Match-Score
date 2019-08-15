# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 03:24:34 2019

@author: Batuhan
"""

import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

data = pd.read_csv("Modified data/modified_1819.csv")

x = data.iloc[:,4:]
y1 = data.iloc[:,2:3]
y2 = data.iloc[:,3:4]

X = x.values
Y1 = y1.values
Y2 = y2.values

lr = LinearRegression()
lr.fit(X,Y1)
y_pred = lr.predict(X)

ctr = 0
for i in range(len(y_pred)):
    if int(y_pred[i]) == Y1[i]:
        ctr += 1
        
print("linear regression basari orani: ", ctr/len(y_pred))

poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(X)
lr2 = LinearRegression()
lr2.fit(x_poly,y1)
y_pred = lr2.predict(x_poly)

ctr = 0
for i in range(len(y_pred)):
    if int(y_pred[i]) == Y1[i]:
        ctr += 1
        
print("poly reg basari orani: ", ctr/len(y_pred))


x_train, x_test, y_train, y_test = train_test_split(x,y1,test_size=0.2, random_state=0)


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3,metric="minkowski",weights="distance")
knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)

ctr = 0
for i in range(len(y_pred)):
    if y_pred[i] == y_test.values[i]:
        ctr += 1
        
print("knn basari orani: ", ctr/len(y_pred))

