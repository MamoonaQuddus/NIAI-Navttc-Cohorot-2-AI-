import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv('C:\\Users\\My Computer\\Downloads\\Python\\week5\\home task\\diabetes.csv')
features = ['Age' , 'BMI' ,'Insulin' ,'BloodPressure']

x = df[features] 
y = df['Outcome']


x_train , x_test , y_train , y_test = train_test_split(x,y ,test_size = 0.2 , random_state = 42)
model = LinearRegression()
model.fit(x_train, y_train)
pred = model.predict(x_test)

print('R2:', round(r2_score(y_test, pred), 3))
print('RMSE:' , round(mean_squared_error(y_test , pred) ** 0.5 ,2))

# coef = weight
print(pd.Series(model.coef_, index=features).round(2))

print()
print("# polynomial LinearRegression ")
print()


# polynomial LinearRegression

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

df = pd.read_csv('C:\\Users\\My Computer\\Downloads\\Python\\week5\\home task\\diabetes.csv')
x = df.drop(columns=['Age' , 'BMI' ,'Insulin' ,'BloodPressure', 'Outcome'])
y= df['Outcome']

X_train, X_test , y_train, y_test = train_test_split(x , y , test_size=0.2 , random_state= 42)

# overfititng happening if we increase degree

for degree in range(1,3):
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())

    model.fit(X_train , y_train)
    train_r2= r2_score(y_train , model.predict(X_train))
    test_r2 = r2_score(y_test, model.predict(X_test))

    print(f'Degree {degree}: train R2 = {train_r2:.3f} | test R2 = {test_r2:.3f} ')

