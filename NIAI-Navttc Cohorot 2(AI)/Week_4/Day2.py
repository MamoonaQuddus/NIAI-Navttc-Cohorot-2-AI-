#-----------------------------------
# Feature engineering & Data Pipeline
#------------------------------------

# feature engineering means creating new feature from exsiting ones that help model to learn better
#feature extrction means picking out useful features from the dataset
import pandas as pd

# df = pd.DataFrame({
#     'height_cm' : [170, 180,160],
#     'weight_kg' : [65, 80, 55]
# })

# df['bmi'] = df['weight_kg'] / (df['height_cm'] /100)**2
# print(df)
# print(df['bmi'])


# task 1

# df2 = pd.DataFrame({
#     'price' : [170, 180,160],
#     'quantity' : [10,20,30]
# })


# df2['total_cost'] = df2['price'] + df2['quantity']
# print(df2)

# task 2

# total_income
# total_expense


# saving_rate =( saving / income) =?


df3 = pd.DataFrame({
    'total_income' : [170, 180,160],
    'total_expense' : [10,20,30]
})

df3['savings'] =df3['total_income'] - df3['total_expense']

df3['saving_rate'] = df3['savings'] / (df3['total_income']) * 100
print(df3)


# feature selection and binning
#------------------------------
# what's differnce bewteen feature selection and feature extraction
df =pd.DataFrame({
    'study_hrs' : [1,2,3,4,5],
    'sleep_hrs': [8,7,6,8,7],
    'marks': [50,55,65,70,85]
})

# how this will work  
print(df.corr()['marks'])

ages = pd.Series([5,17,25,45,68,80])
print(pd.cut(ages, bins=[0,12,19,50,100],
             labels=['child' , 'Teen' , 'Adult' ,'Senior']))


# task 1
# what's differnce bewteen feature selection and feature extraction
df2 =pd.DataFrame({
    'work_hrs' : [1,2,3,4,5],
    'sleep_hrs': [8,7,6,8,7],
    'bonus': [50,55,65,70,85]
})

# how this will work  
print(df2.corr()['bonus'])


# exams_score = 0-100
# Fail , Pass , Merit 

exam_score = pd.Series([0,17,25,45,68,100])
print(pd.cut(exam_score, bins=[0,49,60,80],
             labels=['Fail' ,'Pass' ,'Merit']))



# ETL & Batch vs Stream processing
# Extract ,Transform ,Load 
# OLTP AND olap (slow flake how to write ETL)
#--------------------------------
# # E 
# raw = pd.read_csv('Daily_sales_Csv')

# # T
# clean = raw.dropna().assign(
#     revenue = raw['price'] * raw['qty']
# ) 

# # L 
# clean.to_csv('processed_sales_csv', index= False)

#Automation with sklearn pipeline
#####################################
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

import numpy as np 

# hours and score 
x = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
])
y = np.array([40, 45 , 60 , 68 , 75 , 82 , 90])


pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LinearRegression())

])

pipe.fit(x, y)
print(pipe.predict([[9]]))