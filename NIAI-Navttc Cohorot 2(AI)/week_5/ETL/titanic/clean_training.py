
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# =========================================================
# 1. LOAD DATASET
# =========================================================

df = pd.read_csv(
    r"C:\Users\My Computer\Downloads\Python\ETL\titanic\train.csv"
)

print("Original shape:", df.shape)
print(df.head())
print(df.info())


# =========================================================
# 2. BASIC CHECKS
# =========================================================

print("\nMissing values:")
print(df.isnull().sum())

print("\nTarget distribution:")
print(df["Survived"].value_counts())

print("\nDuplicate rows:")
print(df.duplicated().sum())


# =========================================================
# 3. REMOVE DUPLICATES
# =========================================================

df = df.drop_duplicates(subset="PassengerId")


# =========================================================
# 4. FEATURE ENGINEERING
# =========================================================

# ----- Title from Name -----

df["Title"] = df["Name"].str.extract(
    r",\s*([^\.]+)\."
)

# Combine similar titles
df["Title"] = df["Title"].replace({
    "Mlle": "Miss",
    "Ms": "Miss",
    "Mme": "Mrs"
})

# Combine rare titles
rare_titles = [
    "Dr", "Rev", "Major", "Col", "Don",
    "Lady", "Sir", "Capt",
    "the Countess", "Jonkheer"
]

df["Title"] = df["Title"].replace(
    rare_titles,
    "Rare"
)


# ----- Age -----

# Fill missing Age using median Age within each Title
df["Age"] = df.groupby("Title")["Age"].transform(
    lambda x: x.fillna(x.median())
)

# Convert Age to integer
df["Age"] = df["Age"].astype(int)


# ----- Cabin → Deck -----

# Take first letter of Cabin
# Missing Cabin becomes "U" = Unknown
df["Deck"] = df["Cabin"].str[0].fillna("U")


# ----- Embarked -----

# Only a few values are missing
df["Embarked"] = df["Embarked"].fillna(
    df["Embarked"].mode()[0]
)


# ----- Fare transformation -----

df["Fare_log"] = np.log1p(df["Fare"])


# ----- Family features -----

df["FamilySize"] = (
    df["SibSp"] +
    df["Parch"] +
    1
)

df["IsAlone"] = (
    df["FamilySize"] == 1
).astype(int)


# =========================================================
# 5. DROP UNNECESSARY ORIGINAL COLUMNS
# =========================================================

df = df.drop(
    columns=[
        "Name",
        "Ticket",
        "Cabin",
        "PassengerId"
    ]
)


# =========================================================
# 6. ENCODE CATEGORICAL FEATURES
# =========================================================

df = pd.get_dummies(
    df,
    columns=[
        "Sex",
        "Embarked",
        "Title",
        "Deck"
    ],
    drop_first=True
)


# =========================================================
# 7. LOWERCASE COLUMN NAMES
# =========================================================

df.columns = [
    column.lower()
    for column in df.columns
]


# =========================================================
# 8. CHECK FINAL DATA
# =========================================================

print(
    f"\nFinal shape: {df.shape}"
)

print("\nRemaining missing values:")
print(df.isnull().sum())

print("\nFinal columns:")
print(df.columns)


# =========================================================
# 9. CORRELATION WITH TARGET
# =========================================================

print("\nCorrelation with Survived:")

print(
    df.corr()["survived"]
    .sort_values(ascending=False)
)


# =========================================================
# 10. X AND Y
# =========================================================

X = df.drop(
    columns=["survived"]
)

y = df["survived"]


# =========================================================
# 11. TRAIN / TEST SPLIT
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)


# =========================================================
# 12. MODELS
# =========================================================

models = {

    "Logistic Regression":
        LogisticRegression(max_iter=1000),

    "SVM (RBF)":
        SVC(),

    "KNN (k=5)":
        KNeighborsClassifier(5),

    "Naive Bayes":
        GaussianNB()
}


# =========================================================
# 13. TRAIN + EVALUATE
# =========================================================

for name, model in models.items():

    pipe = make_pipeline(
        StandardScaler(),
        model
    )

    pipe.fit(
        X_train,
        y_train
    )

    y_pred = pipe.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    print("\n" + "=" * 50)
    print(name)

    print(
        f"Accuracy: {accuracy:.3f}"
    )

    print("\nConfusion Matrix:")

    print(
        confusion_matrix(
            y_test,
            y_pred
        )
    )

    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            y_pred
        )
    )

