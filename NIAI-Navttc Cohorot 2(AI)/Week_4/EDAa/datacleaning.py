#############################
# EDA 
##############################
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# df = pd.read_csv('C:\Users\My Computer\Downloads\Python\EDAa\Books_Data_Clean.csv')  
df = pd.read_csv('C:\\Users\\My Computer\\Downloads\\Python\\EDAa\\Books_Data_Clean.csv')
# task 1

print(df.shape) 

# task 2
# which coloumn has missing values and how many missing in each 

print(df.isnull())
print(df.isnull().sum())
print()
print()
# task 3
# what is the average ( mean) book_average_rating across all books
print(df['Book_average_rating'].mean())

# task 4
#  total gross sales across  1070 books(sum)
print(df['gross sales'].sum())

# task 5
# which genre most frequent
# print(df["genre"].duplicated().sum)

print(df["genre"].value_counts().idxmax())



print()
print()
# task 6
# which publisher has the highest total unit sold
# print(df['publisher'].max())
# publisher_sales = df.groupby("Publisher")["units sold"].sum()
publisher_sales = (df.groupby("Publisher ")["units sold"])
# print(publisher_sales)
print(publisher_sales.idxmax())
print(publisher_sales.idxmax().max())


# task 7

# find the correlation between gross scale and publisher revenu is it strong or week 



# g = df[["gross sales", "publisher revenue"]].corr()

# sns.heatmap(g, annot= True)
# plt.show()

print(df.head(5))
# publishing year from smallest to largest 

print()



# task 9
year = df.sort_values("Publishing Year", ascending= True)

print(year)


#clean and prepare the data














# Question 1: Handle Missing Values



df["Book Name"] = df["Book Name"].fillna("Unknown")
# most frequent
df["language_code"] = df["language_code"].fillna(df["language_code"].mode()[0])
# middle in skewed data 
df["Publishing Year"] = df["Publishing Year"].fillna(
    df["Publishing Year"].median()
)



# Question 2: One-Hot Encoding for 'genre'

genre_ohe = pd.get_dummies(df["genre"])

print(genre_ohe.head())



# Question 3: Label Encoding for 'Author_Rating'


# Question 4: Check Skewness & Apply Log Transform
# data distribution is balanced or pulled towards one side like left or right 

skew_before = df["gross sales"].skew()

# 2. Apply log transform
df["gross sales log"] = np.log(df["gross sales"])

# 3. Skewness after transform
skew_after = df["gross sales log"].skew()


print("Skewness before log transform:", round(skew_before, 4))
print("Skewness after log transform:", round(skew_after, 4))
# print(
#     "Did it improve? Yes, the skewness dropped from 5.9325 down to 0.4818 (much closer to 0/normal distribution)."
# )



# Question 5: StandardScaler on 'units sold'
# one feature do not dominate to another 

scaler = StandardScaler()

# Scale the column
df["units_sold_scaled"] = scaler.fit_transform(df[["units sold"]])

#  transformed mean
scaled_mean = df["units_sold_scaled"].mean()

print(scaled_mean)
print("Transformed Mean:", round(scaled_mean, 6))
# print("Is it approximately 0? Yes (7.97e-17 is virtually 0).")















































# rating_map = {"Novice": 0, "Intermediate": 1, "Excellent": 2, "Famous": 3}
# df["Author_Rating"] = df["Author_Rating"].map(rating_map)

# print(df["Author_Rating"].head())

# # task 3

# from sklearn.preprocessing import LabelEncoder
# order = ['Novice ','intermediate','Excellent' ,'Famous']
# le = LabelEncoder()
# print(le.fit_transform(order))












# print(df.head(5))
# print(df.sample(5))
# print(df.tail())
# print(df.columns())
# print(df.dtypes)

# what is the difference between info and describe 



# print(df.describe)
# df.describe(include="object")
# print(df.info())
# df.isnull().sum()
# df.duplicated().sum()
# df[df.duplicated()]

# df.dtypes

# df["genre"].unique()
# df["genre"].nunique()
# df["genre"].value_counts()

# df["price"].hist()

# import matplotlib.pyplot as plt

# plt.hist(df["price"])
# plt.xlabel("Price")
# plt.ylabel("Number of Books")
# plt.show()

# #outliers
# plt.boxplot(df["price"].dropna())
# plt.show()

# df["genre"].value_counts().plot(kind="bar")
# plt.show()

# how many column
# which column are numerical and which are categorial
# are there missing values
# are there duplicates (rows,columnd)

# lets start #
####################################
