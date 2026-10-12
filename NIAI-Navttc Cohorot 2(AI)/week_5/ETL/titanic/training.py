import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import  GaussianNB 
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

from sklearn.metrics import accuracy_score , confusion_matrix


df = pd.read_csv('C:\\Users\\My Computer\\Downloads\\Python\\ETL\\titanic\\train.csv')

print(df.shape)
# print(df.head())
# print(df.info())
# print(df.isnull().sum())
# print(df['Survived'].value_counts())
# print(df.duplicated().sum())
# df= df.drop_duplicates()
# print(df)





df = df.copy()

# 0) dedupe FIRST, on the true identifier, while PassengerId still exists
df = df.drop_duplicates(subset="PassengerId")

# a) Title extraction from Name (also lets us do smarter Age imputation)
# df["Title"] = df["Name"].str.extract(r",\s*([^\.]+)\.")

df["Title"] = df["Name"].str.extract(r",\s*([^\.]+)\.")

df["Title"] = df["Title"].replace({"Mlle": "Miss", "Ms": "Miss", "Mme": "Mrs"})
rare_titles = ["Dr", "Rev", "Major", "Col", "Don", "Lady", "Sir",
                   "Capt", "the Countess", "Jonkheer"]
df["Title"] = df["Title"].replace(rare_titles, "Rare")

    # b) Age: fill missing with the median age WITHIN each title group
    #    (a Master gets a boy's median age, a Mr gets an adult male's, etc.)
df["Age"] = df.groupby("Title")["Age"].transform(lambda x: x.fillna(x.median()))
df["Age"] = df["Age"].astype(int)  # safe now: no missing values left

    # c) Cabin -> Deck (first letter). 'U' = Unknown, since ~77% are missing
    #    and dropping them all would throw away real signal for the ones we have.
df["Deck"] = df["Cabin"].str[0].fillna("U")

    # d) Embarked: only 2 missing -> safe to fill with the mode (most common port)
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # e) Fare: right-skewed with real (not erroneous) high outliers -> log-transform
    #    instead of deleting rows, so extreme fares don't dominate a model later.
df["Fare_log"] = np.log1p(df["Fare"])

    # f) Family features (simple, interpretable engineered features)
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

    # g) drop columns we've replaced with better features, or that are
    #    high-cardinality with no direct signal (raw Name, Ticket, Cabin, PassengerId)
df = df.drop(columns=["Name", "Ticket", "Cabin", "PassengerId"])

    # h) encode categoricals
    #    - Sex, Embarked, Title, Deck: no inherent order -> one-hot encode
    #    - Pclass: already an ordinal number (1/2/3) -> leave as-is, don't one-hot
df = pd.get_dummies(df, columns=["Sex", "Embarked", "Title", "Deck"], drop_first=True)

    # i) lowercase all column names (convention, avoids case-mismatch bugs later)
df.columns = [c.lower() for c in df.columns]

    # j) Correlation check
df.corr()["survived"].sort_values(ascending=False)


print(f"[transform] {len(df)} rows, {len(df.columns)} columns after encoding")
    




# pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# Cabin , Embarked , Ticket, Sex, Name

x= df.drop(columns=['survived'])
y = df['survived']

X_train , X_test, y_train , y_test = train_test_split(x, y , random_state= 42 , test_size=0.2 ,stratify=y)

models = {'Logistic Regression ': LogisticRegression(max_iter=1000), 
         'SVM (RBF) ': SVC(), 'KNN( k=5)': KNeighborsClassifier(5),'Naive Bays': GaussianNB() }


for name, m in models.items():
    pipe = make_pipeline(StandardScaler(), m).fit(X_train , y_train)

    print(f'{name:20s} accuary = {pipe.score(X_test, y_test): .3f}')