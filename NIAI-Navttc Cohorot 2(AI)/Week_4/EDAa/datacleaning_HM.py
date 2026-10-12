
#############################
# EDA 
# EDA is about asking "why?"
##############################
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# df = pd.read_csv('C:\Users\My Computer\Downloads\Python\EDAa\Books_Data_Clean.csv')  
df = pd.read_csv('C:\\Users\\My Computer\\Downloads\\Python\\EDAa\\Books_Data_Clean.csv')

# df.describe() → gives statistical summary of numerical columns.
# describe() by default focuses on numerical columns.
# df.describe(include="object") Gives a summary of text/categorical columns.

# print(df.describe())
# print(df.describe(include="object"))
print(df.shape) 
# df.head()
# df.tail()

#info tells you about the structure of the DataFrame.
# df.info()
# print(df.isnull())
# print(df.isnull().sum())
print()
print(df.duplicated().sum())
print(df.dtypes)

print(df["genre"].unique())
print(df["genre"].value_counts())


# unique() → shows what unique values exist.
# value_counts() → shows how many times each unique value appears.
#orr
# value_counts() = count each unique value
# sum() = add all values

# visualization
###############

# distribution
# skewness
# possible outliers
# concentration

# df["sale price"].hist()
# df["price"].hist() → Pandas way (easy)
# plt.hist(df["price"]) → Matplotlib way (more control)

# Pandas histogram
# A histogram answers:

# Where are most of the books concentrated?

# df["price"].hist()
# plt.title("Pandas Histogram")
# plt.show()

# Matplotlib histogram
# plt.hist(df["sale price"])
# plt.title("Matplotlib Histogram")
# plt.show()

# A boxplot is useful for spotting potential outliers.
# But remember:
# Outlier ≠ error
# plt.boxplot(df["sale price"].dropna())
# plt.show()


# 14. Categorical visualization
# Suppose you want to understand genres.

# df["genre"].value_counts().plot(kind="bar")
# plt.show()


# Relationships between variables
# df.plot.scatter(x="sale price", y="units sold")
# plt.show()


# df.boxplot(column="sale price", by="genre")
# plt.show()

# Correlation
# For numerical variables:
# we can print corr and can also use heatmap
# print(df.corr(numeric_only=True))

# corr = df.corr(numeric_only=True)
# sns.heatmap(corr, annot=True)
# plt.show()

# print(df[["sale price", "Publisher", "Publishing Year"]].corr())
# corr = df[["sale price", "Publisher", "Publishing Year"]].corr()
# sns.heatmap(corr, annot=True)
# plt.show()

print()
print("next")
# Filtering
##########
# a = df[df["sale price"] > 4.5]
# print(a)

# do target coloumn but show whole table as well
a = df.sort_values("index", ascending=False)
# print(a)

b = df["Publishing Year"].value_counts().sort_index()
print(b)

# Cross-tabulation
#####################

# ?

# GroupBy
# "How does one group differ from another?"


# OUTLIER ANALYSIS
# plt.boxplot(df["sale price"].dropna())
# plt.ylabel("Price")
# plt.show()

print(df.groupby("genre")["sale price"].agg(
    ["mean", "median", "min", "max"]
))

df.boxplot(column="sale price", by="genre")
plt.show()

# pd.crosstab(df["genre"], df["author"])


