import pandas as pd
import numpy as np
import matplotlib as mlp

df = pd.read_csv("C:\\Users\\My Computer\\Downloads\\Python\\Week4_Day1\\House Price Prediction Dataset.csv")
# print(df.head())
print(df.shape)


# df['Area'] = df['Area'] / 272.25




x= df['Area']
# print(x)

y = df['Price']
# print(y)

print()
mean_x = df['Area'].mean()
print(mean_x)

print()

mean_y = df['Price'].mean()
print(mean_y)

print()
dev_x = df['Area'] - mean_x


print(dev_x)

dev_y = df['Price'] - mean_y

print(dev_y)


print()

print()
print()
mul_dev = dev_x * dev_y
print(mul_dev)


square_dev_x =  dev_x **2
print(square_dev_x)

sum_dev = mul_dev.sum()
sum_square_dev_x = square_dev_x.sum()


print("m slop")

m = sum_dev / sum_square_dev_x
print(m)

print("b intercept")

b= mean_y - (m * mean_x)
print(b)



print("y Now for a particulr value")
print(df['Area'][0])
y = m * df['Area'][0] + b
print(y)

print("for all the values ")

y = m * df['Area'] + b
print(y)










