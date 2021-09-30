#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:25:42 2021

@author: scottswasey
"""

import pandas as pd 

df = pd.read_csv('glassdoor.csv')

#salary parsing 
#THIS IS MARKING A CREATED COLUMN IWTH 1 OR 0 
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
#50  (THIS IS IN THE COLUMN)
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
#$50K
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

#SO THIS IS SPLITTING ON THE DASH  50-70
df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
#CREATING A FIELD WITH A NUMBERICAL AVERAGE OF 50-70
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#Company name text only
# IT WAS SHOWING A RATING ON THE END  LIKE "MODA HEALTHCARE  1.9"   WE ARE GETTING RID OF THE RATING.   IT IS ONLY 3 CHARACTERS SO WE ARE GETTING RID OF 3 CHARACTERS ON THE END. 
#THIS IS ALSO BASED ON ANOTHER FEILS CALLED RATING  THAT SHOULD NOT BE -1
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#state field 
#WE ARE TAKING  THE SECOND PART OF A LOCATION AND DOING A SPLIT.   "ROCHESTER,NY"  IT IS 0 BASED SO WE ARE TAKING ELEMENT 1
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
#this is just a way to count by groups. 
df.job_state.value_counts()

#this is to see if the job is in the same state as headquarters. 
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#age of company 
#this is just subtracting the age of the company subtracted from the current year..  which is obviously not 2020
df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020 - x)

#parsing of job description (python, etc.)

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
 
#r studio 
# I think he could have done " r "  lower and it would have worked. 
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()

#spark 
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#aws 
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

#df.columns

#df_out = df.drop(['Unnamed: 0'], axis =1)

df.to_csv("salary_data_cleaned.csv", index = False)




