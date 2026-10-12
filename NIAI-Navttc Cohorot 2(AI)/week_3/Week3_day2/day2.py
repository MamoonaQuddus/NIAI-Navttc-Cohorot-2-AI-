# ########################################
# pandas
# pandas is python library for working with Tabular data , like excel but in code. 
########################################

import pandas as pd
data = {'name': ['Ali', 'Sara', 'zain'],
        'marks': [78,88,33]

}
df = pd.DataFrame(data)
print(df)

# task 1
students = {
    'name': ["Ali", "Zafar","Atif","Aslam"],
    'city': ["Sargodha", "Lahore","Peshwar","Multan"],
    'score':[20,50,60,80]
}

df = pd.DataFrame(df)
print(df)
print(len(df))
print(df.columns) 
print(df.columns) 

# task 2


################################
# Series
#################################
s = pd.Series([10 , 20 ,30 ], index = ['a' , 'b' , 'c'])
print(s)


df = pd.DataFrame({
    "name": ["Mamoona","Ayesha"],
    "marks": [10,20]
})

print(df["name"])

# task 1

s = pd.Series(["Lahore", "Islamabad", "Karachi", "Lahore","Faisalbad" ], index = ['a' , 'b' , 'c','d','e'])
print(s)

# task 2
df = pd.DataFrame({
    "name": ["Mamoona","Ayesha"],
    "marks": [10,20]
})

print(df["marks"])

# Selection and indexing

# task 1
df = pd.DataFrame({
    "name": ["Mamoona","Ayesha","Ali","Cameron","Danial"],
    "marks": [90,70,90,60,100]
})
# print(df[df['marks']> 75])

# task 2
print(df[["marks", "name"]])
# print(df[df['marks'], df["name"]])


# Dataframe operations
df = pd.DataFrame({
    "name": ["Mamoona","Ayesha","Ali","Cameron","Danial"],
    "marks": [90,70,90,60,100]
})

df['grades'] = df['marks'].apply(
    lambda x: 'pass' if x >= 80 else 'fail' 
)
# def check_status(x):
#     if x >= 80:
#         return 'pass'
#     else:
#         return 'fail'


print(df.sort_values('marks', ascending=False))

# task 1

df['labels'] = df['marks'].apply(
    lambda x: 'high' if x >= 70 else 'low' 
)
print(df["labels"])

# task 2
df.value_counts("labels")

# handling missing value
df = pd.DataFrame({
    'a':[1,2,None],
    'b':[4,None,6]
})

print(df.isnull())
print(df.fillna(0))

# task 1
df = pd.DataFrame({
    'a':[3,None,None],
    'b':[None,None,6]
})
print(df.isnull())

# task 2
print(df.fillna(0))
print(df.dropna())

# Groupby
print()
print()
sales = pd.DataFrame({'dept':['IT','CS','IT','CS'],
                      'sales':[100, 150,80, 90]

                      })
print(sales.groupby('dept')['sales'].sum())

# task 1
products = pd.DataFrame({
    'category':['shampoo', 'mobile', 'laptop'],
    'price': [12,13,15]
})
print(products.groupby('category')['price'].mean())


# task 2
print(products.groupby('category').count())

# merging and concatintion

a = pd.DataFrame({
    "id": [1,2,3],
    "name": ["Mamoona","Ayesha","Ali",]
    
})

print(a)
b = pd.DataFrame({
    "id": [1,2,4],
    "marks": [90,70,90]
})
print(b)
print(pd.merge(a,b, on='id' ,how ='inner'))



# task 1
a = pd.DataFrame({
    "id": [1,2,3],
    "name": ["Mamoona","Ayesha","Ali",]
    
})

print(a)
b = pd.DataFrame({
    "id": [1,2,4],
    "marks": [90,70,90]
})
print(b)
print(pd.merge(a,b, on='id' ,how ='left'))


# task 2
print(pd.concat([a, b], axis=1))
print(pd.concat([a, b]))


# pandas plotting
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "id": [1,2,3],
    "name": ["Mamoona","Ayesha","Ali",]
    
})
df.plot(x='name', y='id' , kind = 'bar')
plt.show()


