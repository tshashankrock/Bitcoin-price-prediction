#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 19:52:39 2018

@author: shashank
"""
from sklearn.metrics import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold,cross_val_score 
df1=pd.read_csv('roughbitcoin.csv',header=-1)
df2=pd.read_csv('roughlitecoin.csv',header=-1)
col_names1 = ['#+tweet','#neutraltweet','#negativetweet','bitcoinprice']
col_names2 = ['#+tweet','#neutraltweet','#negativetweet','litecoinprice']
df1.columns = col_names1
df2.columns = col_names2
x1 = df1.iloc[:,:-1]
x2 =df2.iloc[:,:-1]
y1 = df1['bitcoinprice'].values
y2 = df2['litecoinprice'].values
# Not using Statsmodel using sklearn model
# import statsmodels.api as sm
# import statsmodels.formula as smf
#x1_constant = sm.add_constant(x1)
#x2_constant = sm.add_constant(x2)
#model1 = sm.OLS(y1,x1_constant)
#model2 = sm.OLS(y2,x2_constant)
#lr1 = model1.fit()
#lr2 = model2.fit()
#lr1.summary()
#lr2.summary()
df1.corr()
df2.corr()
x1_train,x1_test,y1_train,y1_test = train_test_split(x1,y1,test_size=0.2,random_state=0,shuffle=False)
x2_train,x2_test,y2_train,y2_test = train_test_split(x2,y2,test_size=0.2,random_state=0,shuffle=False)
from sklearn.linear_model import LinearRegression 
regressor = LinearRegression()
regressor.fit(x1_train,y1_train)
y1_pred = regressor.predict(x1_test)
y2_pred = regressor.predict(x2_test)
y1_pred, y2_pred
meanerror=mean_absolute_error(y1_test, y1_pred)
meanerror
r2_score=r2_score(y1_test,y1_pred)

## The line/model
plt.scatter(y2_test,y2_pred)
plt.xlabel("True values")
plt.ylabel("Predicted values")

plt.scatter(y1_test,y1_pred)
plt.xlabel("True values")
plt.ylabel("Predicted values")
print("Score:"), regressor.score(x1_test,y1_test)
print("Score:"), regressor.score(x2_test,y2_test)

kf = KFold(n_splits=2,random_state=0,shuffle=False)
kf.get_n_splits(x1_train)
print(kf)

for x1_trainindex,x1_testindex in kf.split(x1_train):
    print("Train;", x1_trainindex, "Test:", x1_testindex)
#for train_index, test_index in kf.split(x1_train):
  #   print("TRAIN;", train_index, "Test:", test_index)
   #  x1_train, x1_test = x1[train_index], x1[test_index]
    # y1_train, y1_test = y1[train_index], y1[test_index]
scores = cross_val_score(regressor,x1,y1,scoring='',cv=kf)
#print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
#scoreing=scores.mean()
