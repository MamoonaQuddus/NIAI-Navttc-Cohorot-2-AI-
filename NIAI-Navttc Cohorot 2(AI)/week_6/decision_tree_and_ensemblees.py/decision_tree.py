###################################
# Decision Tree
# ############################ 

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier,export_text
# from sklearn.ensemble import RandomForestClassifier

# df = pd.read_csv('C:\\Users\\My Computer\\Downloads\\Python\\week5\\students_week5.csv')

# x= df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
# y = df['result']

# X_train , X_test, y_train , y_test = train_test_split(x, y , random_state= 42 , test_size=0.2 ,stratify=y)

# for depth in [3, None]:
#     tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
#     tree.fit(X_train, y_train)
#     print(f'max_depth= {depth}: train ={tree.score(X_train, y_train):.3f}'
#           f'| test = {tree.score(X_test, y_test):.3f}'
#           )


# small = DecisionTreeClassifier(max_depth= 2 , random_state= 42 ).fit(X_train , y_train)
# print(export_text(small, feature_names=list(x.columns)))    

# print()
# print("Random Forest")
# print()

# # randon forest + feature engineering 
# forest = RandomForestClassifier(n_estimators=200 , random_state=42)
# forest.fit(X_train , y_train)
# print('Random Forest test accuracy', round(forest.score(X_test , y_test),3))


# importance = pd.Series(forest.feature_importances_, index=x.columns)
# print(importance.sort_values(ascending=False).round(3))  







print(" train on loan dataset")
print()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,export_text
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('C:\\Users\\My Computer\\Downloads\\Python\\week6\\loan_data_set.csv')

# print(df.head(5))
# df.info()

df = df.drop(columns=['Loan_ID'])
# print(df.describe())
print(df.isnull().sum())
print(df['Loan_Status'].value_counts())
print(df.duplicated().sum())

df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['Married'] = df['Married'].fillna(df['Married'].mode()[0])
df['Dependents'] = df['Dependents'].fillna(df['Dependents'].mode()[0])
df['Self_Employed'] = df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])



df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].median())
df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])

df = pd.get_dummies(
    df,
    columns=[
        'Gender',
        'Married',
        'Dependents',
        'Education',
        'Self_Employed',
        'Property_Area'
    ],
    drop_first=True
)


x = df.drop(columns=['Loan_Status'])
y= df['Loan_Status']




X_train, X_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)



print("\nTraining shape:")
print(X_train.shape)

print("Testing shape:")
print(X_test.shape)


# x= df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
# y = df['result']

# X_train , X_test, y_train , y_test = train_test_split(x, y , random_state= 42 , test_size=0.2 ,stratify=y)

for depth in [3, None]:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(X_train, y_train)
    print(f'max_depth= {depth}: train ={tree.score(X_train, y_train):.3f}'
          f'| test = {tree.score(X_test, y_test):.3f}'
          )


small = DecisionTreeClassifier(max_depth= 2 , random_state= 42 ).fit(X_train , y_train)
print(export_text(small, feature_names=list(x.columns)))    

print()
print("Random Forest")
print()

# randon forest + feature engineering 
forest = RandomForestClassifier(n_estimators=200 , random_state=42)
forest.fit(X_train , y_train)
print('Random Forest test accuracy', round(forest.score(X_test , y_test),3))


importance = pd.Series(forest.feature_importances_, index=x.columns)
print(importance.sort_values(ascending=False).round(3))  




