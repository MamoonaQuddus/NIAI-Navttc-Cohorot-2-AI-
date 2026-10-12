import pandas as pd

df = pd.DataFrame({'name': ['Ali ', 'Sara', 'Ali'],
                   'marks': [85, 78,100]})

print(df.duplicated())
print(df.drop_duplicates())





#  task 1
import pandas as pd

df2 = pd.DataFrame({'dupllicated_name': ['Ali ', 'Ali', 'Ali'],
                   'marks': [85, 78,100]})

print(df2.duplicated())
print(df2.drop_duplicates())


# task 2

# df2 = pd.DataFrame(1,2,3100,4,5,3,2,1)
# df.


# Data Transformation
#########################################

import numpy as np
price = pd.Series([100, 400 , 1000, 50000])
log_price= np.log(price)
print(log_price)


# task 1
import numpy as np
income = pd.Series([100, 400 , 1000000, 50000])
log_income= np.log(income)
print(log_income)


# task 2
print(income)
print(log_income)


# encoding categorical variables
####################################

from sklearn.preprocessing import LabelEncoder
sizes = ['Small' , 'Medium' ,'Large']
le = LabelEncoder()
print(le.fit_transform(sizes))


# task 1

from sklearn.preprocessing import LabelEncoder
gender = ['Male', 'Female']
le = LabelEncoder()
print(le.fit_transform(gender))


# Feature Scaling (Stander & MinMax)
from sklearn.preprocessing import StandardScaler , MinMaxScaler
valus =  np.array([
    [10],
    [20],
    [30],
    [40],
    [50]
])

print(StandardScaler().fit_transform(valus).flatten())
print(MinMaxScaler().fit_transform(valus).flatten())




# task 1
from sklearn.preprocessing import StandardScaler , MinMaxScaler
valus =  np.array([
    [101],
    [450],
    [3000],
    [414],
    [598]
])

print(StandardScaler().fit_transform(valus).flatten())

print()
print(MinMaxScaler().fit_transform(valus).flatten())

