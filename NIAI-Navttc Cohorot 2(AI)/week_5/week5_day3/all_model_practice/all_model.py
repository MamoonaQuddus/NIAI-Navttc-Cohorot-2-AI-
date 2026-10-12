import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import  GaussianNB 
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score , confusion_matrix


df = pd.read_csv('C:\\Users\\My Computer\\Downloads\\Python\\week5_day3\\all_model_practice\\Breast Cancer Wisconsin (Diagnostic) Data Set.csv')

print(df.shape)
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df['diagnosis'].value_counts())
print(df.duplicated().sum())
df.drop_duplicates()



x= df.drop(columns=['diagnosis', 'id', 'Unnamed: 32'])
y = df['diagnosis'].map({"M":1 ,"B":0})

X_train , X_test, y_train , y_test = train_test_split(x, y , random_state= 42 , test_size=0.2 ,stratify=y)

models = {'Logistic Regression ': LogisticRegression(max_iter=1000), 
         'SVM (RBF) ': SVC(), 'KNN( k=5)': KNeighborsClassifier(5),'Naive Bays': GaussianNB() }


for name, m in models.items():
    pipe = make_pipeline(StandardScaler(), m).fit(X_train , y_train)

    print(f'{name:20s} accuary = {pipe.score(X_test, y_test): .3f}')


# for name, model in models.items():

#     pipe = make_pipeline(
#         StandardScaler(),
#         model
#     )

#     pipe.fit(X_train, y_train)

#     y_pred = pipe.predict(X_test)

#     print("\n", "=" * 50)
#     print(name)

#     print("Accuracy:",
#           accuracy_score(y_test, y_pred))

#     print("\nConfusion Matrix:")
#     print(confusion_matrix(y_test, y_pred))

#     print("\nClassification Report:")
#     print(classification_report(y_test, y_pred))