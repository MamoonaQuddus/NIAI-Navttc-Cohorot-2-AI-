import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import  GaussianNB 

from sklearn.metrics import accuracy_score , confusion_matrix



# P(yes/ x1 , x2 ,... xn) = P(x1/y) ,P(x2/y) ... xn

# prior pro 
# p(fever =yes) = 7/10
# p(fever = no)= 3/10


# conditional pro 
#         fever(yes)    fever(no)  
# covid    4/7           2/3
# flue     3/7           2/3


# 4/7  * 3/7 *7/10  
# 12/70  6/35 = 0.17

# 2/3 * 2/3 * 3/10 
# 4/30 = 0.133

df = pd.read_csv('C:\\Users\\My Computer\\Downloads\\Python\\week5\\students_week5.csv')
x= df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y = df['result']

X_train , X_test, y_train , y_test = train_test_split(x, y , random_state= 42 , test_size=0.2 ,stratify=y)


model = GaussianNB()
model.fit(X_train , y_train)
pred = model.predict(X_test)
print('Accuracy' , accuracy_score(y_test , pred))

print(confusion_matrix(y_test, pred))

new_Student = X_test.iloc[[0]]

print('pass probability ', model.predict_proba(new_Student)[0][1].round(2))




