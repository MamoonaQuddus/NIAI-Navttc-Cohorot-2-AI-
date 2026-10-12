import pandas as pd
import numpy as np
import matplotlib as mlp

df = pd.read_csv("C:\\Users\\My Computer\\Downloads\\Python\\Week4_Day1\\pakistan house prediction dataset.csv")
# print(df.head())

# how to handle missing values 
#  how to convert string value into int
# how to handle duplicated column and rows
# how to handle null rows/column


print(df.info())
print(df.shape)
print(df.describe())

# 1. Fix Area_SqFt
df["Area_SqFt"] = (
    df["Area_SqFt"]
    .astype(str)
    .str.extract(r"(\d+\.?\d*)")[0]
    .astype(float)
)

# 2. Fix Year_Built
df["Year_Built"] = pd.to_numeric(df["Year_Built"], errors="coerce")


# 3. Fix Price_PKR
df["Price_PKR"] = (
    df["Price_PKR"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.extract(r"(\d+\.?\d*)")[0]
    .astype(float)
)




# how to handle null rows/column bcz if there are so many null values and the column is important we can just delete /remove that
print(df.isnull().sum())

# numerical column(values) will have been handled by median 

num_cols = ["Area_SqFt", "Bedrooms", "Bathrooms", "Floors", "Garage", "Price_PKR"]

for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# categorical column will be handled by mode

cat_cols = ["City", "Furnished", "Corner_Property", "Park_Facing"]

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])


print(df.isnull().sum())  
# this should be null now . bcz null value has been solved 


# how to handle duplicated column and rows /// just delete that 
print("duplicated values")
print(df.duplicated().sum())

df = df.drop_duplicates()
print(df.duplicated().sum())  # should be 0

print("duplicates has been handled")


# print(df["Area_SqFt"].unique().value_counts())

# print(df["Area_SqFt"].value_counts())



# how to handle missing values (how many ways exits deleting always not a good idea )
# df = df.dropna()
# print(df.head())








#  how to convert string value into int


print("# find missing values ")
print(df["Area_SqFt"].isna().sum())

print("# Shows how many unique values each column has. ")

print(df.nunique())



print("# ➡️ Shows the categories and how frequently they occur.")

cat_cols = ["City", "Location", "Condition", "Property_Type",
            "Furnished", "Corner_Property", "Park_Facing"]

for col in cat_cols:
    print("\n", col)
    print(df[col].value_counts())


print("# ➡️ Shows mean, min, max, quartiles, etc... Check numerical variables")


num_cols = ["Area_SqFt", "Bedrooms", "Bathrooms", "Floors",
            "Garage", "Year_Built", "Price_PKR"]

print(df[num_cols].describe())



print("This checks all numerical columns together for:")
# """"""
# Negative values
# Zero values
# Missing values
#  Minimum


# """"""
print()
print("Fix Area_SqFt = 0")
df = df[df["Area_SqFt"] > 0]
print((df["Area_SqFt"] <= 0).sum())


print("Fix missing Year_Built")
df["Year_Built"] = df["Year_Built"].fillna(df["Year_Built"].median())
print(df["Year_Built"].isna().sum())


num_cols = df.select_dtypes(include="number").columns

for col in num_cols:
    print(f"\n{col}")
    print("Negative:", (df[col] < 0).sum())
    print("Zero:", (df[col] == 0).sum())
    print("Missing:", df[col].isna().sum())
    print("Min:", df[col].min())
    print("Max:", df[col].max())


print('Now we convert text/categorical columns into numbers so Linear Regression can use them.')

cat_cols = df.select_dtypes(include=["object", "str"]).columns

print(cat_cols)

df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
print(df.dtypes)


num_cols = df.select_dtypes(include="number").columns


print("1. Check outliers in all numerical columns")
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = ((df[col] < lower) | (df[col] > upper)).sum()

    print(f"{col}: {outliers} outliers")

print("Now let's see the actual outlier values")
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]

    if len(outliers) > 0:
        print(f"\n{col}:")
        print(outliers[col].values)    