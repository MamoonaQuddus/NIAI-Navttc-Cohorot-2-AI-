import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv('C:\\Users\\My Computer\\Downloads\\Python\\week5\\students_week5.csv')
x= df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y = df['result']

X_train , X_test, y_train , y_test = train_test_split(x, y , random_state= 42 , test_size=0.2 ,stratify=y)


# scaler = StandardScaler()

# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)


#SVM

# for kernel in ['linear', 'rbf']:
#     model = SVC(kernel=kernel, C=1.0)   # sirf left side change kiya
#    SVC(kernel='rbf', gamma=...)
#     model.fit(X_train, y_train)
#     acc = accuracy_score(y_test, model.predict(X_test))
#     print(f'SVM({kernel}) accuracy : {acc:.3f}')


# K_Nearest Neighbours
raw = KNeighborsClassifier(n_neighbors=5).fit(X_train ,y_train)

print('KNN without Scaling:', accuracy_score(y_test, raw.predict(X_test)))

scaler = StandardScaler()
X_train_s, X_test_s , =  scaler.fit_transform(X_train), scaler.transform(X_test)



for k in [1,3,5,7,9,15,25,50,]:
    knn = KNeighborsClassifier(n_neighbors=k).fit(X_train_s, y_train)
    acc = accuracy_score(y_test, knn.predict(X_test_s))
    print(f'k={k:>2}: accuracy = {acc:.3f}')    


