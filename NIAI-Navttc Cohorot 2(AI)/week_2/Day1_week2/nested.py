# useful for grids/tables

for i in range(1,4):
    for j in range(1, 4):
        print(i ,"*" ,j ,"=", i*j  )


# print a full 5*5 multiplication table for loops
# row=i
# coloum=j
# *
# **
# ***
# ****
# *****
# 5*1=5
# 5*2= 10


for i in range(1,6):
    for j in range(i):
        print("*" , end="")
    print()    
        
print()

for i in range(1, 11):
    print(5, "*", i, "=", 5 * i)


# *****
# ****
# ***
# **
# *


for i in range(1 ,6):
    for j in range(6):
        print("*" , end="")
    print()   


# 1 2 3
# 1 2 3
# 1 2 3   

for i in range(1 ,4):
    for j in range(1, 4):
        print("i" , end=" ")
    print()  