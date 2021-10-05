#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 08:04:38 2021

@author: scottswasey
"""

import pandas as pd
import matplotlib as plt
import numpy as np

df = pd.read_csv("eda_data.csv")

df.columns
#choose relevant columns

df_model = df[['avg_salary','Rating','Size','Type of ownership','Industry','Sector','Revenue','num_comp','hourly','employer_provided',
             'job_state','same_state','age','python_yn','spark','aws','excel','job_simp','seniority','desc_len']]
# get dummy data 
df_dum = pd.get_dummies(df_model)

# train test split 
from sklearn.model_selection import train_test_split

X = df_dum.drop('avg_salary', axis =1)
y = df_dum.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# multiple linear regression 
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()


#MULTIPLE LINEAR REGRESSION
#LASSO REGRESSION   BECAUSE THE DATA SET IS GOING TO BE SO SPARSE WITH DATA
#TREE BASED MODEL   TO COMPARE WITH THE LINEAR SET
#NOW TUNE THE MODELSGRIDSEARCHCV
#TEST ENSAMBLES
