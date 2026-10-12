import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix , classification_report
from sklearn.preprocessing import StandardScaler


df = pd.read_csv('C:\\Users\\My Computer\\Downloads\\Python\\week5\\students_week5.csv')
x = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y= df['result']

X_train, X_test , y_train, y_test = train_test_split(x , y , test_size=0.2 , random_state= 42 , stratify= y)


# X_train → 80% student information → model learns from this
# y_train → 80% actual scores       → model learns the answers

# X_test  → 20% student information → model is tested on this
# y_test  → 20% actual scores       → used to check if predictions are correct


scaler = StandardScaler()


X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(max_iter= 100)
model.fit(X_train , y_train)

pred = model.predict(X_test)

print('Accuracy: ', accuracy_score(y_test , pred))

print(confusion_matrix(y_test , pred))

print(classification_report(y_test, pred))


# multiclass low / medium / high
print("  multiclass low / medium / high ")


df = pd.read_csv('C:\\Users\\My Computer\\Downloads\\Python\\week5\\students_week5.csv')
x = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y= df['performance']

X_train, X_test , y_train, y_test = train_test_split(x , y , test_size=0.2 , random_state= 42 , stratify= y)


# X_train → 80% student information → model learns from this
# y_train → 80% actual scores       → model learns the answers

# X_test  → 20% student information → model is tested on this
# y_test  → 20% actual scores       → used to check if predictions are correct


scaler = StandardScaler()


X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)



model = LogisticRegression(max_iter= 100)
model.fit(X_train , y_train)



pred = model.predict(X_test)

print('Accuracy: ', accuracy_score(y_test , pred))

print(confusion_matrix(y_test , pred))


print(model.predict_proba(X_test[ : 3]).round(2) ) 
# probability of each class 


