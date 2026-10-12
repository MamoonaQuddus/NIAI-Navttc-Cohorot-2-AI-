#############################
# EDA 
##############################
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

# sns.displot([0, 1, 2, 3, 4, 5])
# sns.displot([0, 1, 2, 3, 4, 5], kind="kde")
# plt.show()
# print(df)
print(df.shape)
print(df.head(5))
# print(df.head())
print(df.dtypes)

# task 2

# data types of each coloum
print(df.describe())
print()

# task 3

print(df['day'].value_counts())
print()

# sns.histplot(df['total_bill'])
# plt.show()


# task 4


# average total bill = ? mon_sun
# which day has the highest average value 

# groupby(day)
# total_bill
# mean()
print(df.groupby('day')['total_bill'].mean())
print(df.groupby('day')['total_bill'].max())

# task 5

# day_avg = df.groupby('day')['total_bill'].mean()
# print(day_avg)

# df.plot(x='totl_bill', y='tip' , kind = 'scatter')
sns.scatterplot(x = 'total_bill' , y ="tip" , data=df)
# plt.show()
print("yes bigger bill mean bigger tip ")

# multivriate
 
temp = df[['total_bill','tip','size']].corr()
# df['total_bill','tip' ,'size'].corr()
sns.heatmap(temp ,annot=True)
plt.show()

print()