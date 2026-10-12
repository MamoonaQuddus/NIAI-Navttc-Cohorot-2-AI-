import pandas as pd 


df = pd.read_csv('C:\\Users\\My Computer\\Downloads\\Python\\week6\\shop_sales_daily.csv', parse_dates=['date'])
print(df.head(3))

print('From', df['date'].min().date(), 'to' , df['date'].max().date(),
'|',len(df), 'days')



df['dayofweek'] = df['date'].dt.day_name()
df['month'] = df['date'].dt.month

print('\n Average sales by day of each week ')
print(df.groupby('dayofweek')['sales'].mean().round())

print('\n Average sales by month')
print(df.groupby('month')['sales'].mean().round())


# 2nd one
print("2nd code ")

from sklearn.metrics import mean_absolute_error

df = pd.read_csv('C:\\Users\\My Computer\\Downloads\\Python\\week6\\shop_sales_daily.csv', parse_dates=['date'])

df['log_1'] = df['sales'].shift(1)
df['log_7']= df['sales'].shift(7)
df['roll_7'] = df['sales'].shift(1).rolling(7).mean()
df['dayofweek'] = df['date'].dt.dayofweek
df['month'] = df['date'].dt.month
df = df.dropna()




train = df[df['date'] < '2025_10_01']
test = df[df['date'] >= '2025_10_01']
print("Train days:", len(train), '| Test Days:', len(test))

for name , col in [('Naive (yesterday)', 'log_1',('7-days average', 'roll_7'),
                    ('Seasonal naive (log 7 )', 'log_7')
                    )]:
    print(f'{name:24s} MAE: {mean_absolute_error(test["sales"], test[col]):.1f}')

# 3rd one
print("3rd code")

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


features = ['lod_1', 'log_7', 'roll_7', 'dayofweek', 'month']
X_train , y_train = train[features], train['sales']
X_test , y_test = test[features], test['sales']


for name, model in [('Linerar Regression', LinearRegression()),
                    ('Random Forest', RandomForestRegressor(300, random_state=42))
                    ]:
    model.fit(X_train, y_train)
    pred= model.predict(X_test)
    print(f'{name:18s} MAE: {mean_absolute_error(y_test, pred):.1f}')


rf= RandomForestRegressor(300, random_state=42).fit(X_train, y_train)
print(pd.Series(rf.feature_importants_, index=features).round(2))    