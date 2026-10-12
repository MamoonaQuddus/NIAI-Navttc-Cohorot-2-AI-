age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)

marks= 40
remarks = "Pass" if marks >=40 else "Fail"
print(remarks)

# break  continue, pass

for i in range(5):
    if i== 5:
        break
    print(i)
    print()
   

    

for i in range(20):
    if i % 2 == 0:
        continue
    print(i)    


# Task 1-20 ,stop 15

for i in range(20):
    if i == 15:
        break
    print(i)

for i in range(20):
    if i % 3 == 0:
        continue
    print(i)  


#  task loop & enumerate


fruits =[ "banana" ,"Mango", "apple"]
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(index, fruit)

fruitss = ["biryani" ,"Korma" , "Russian Salad","Pizza","Ice_cream"] 
for index, fruit in enumerate(fruitss):
    print(index, fruit)   



# use a for loop with range to print the first 10 square numbers (1,4 , 9 ...)
for i in range(1, 11):
    print(i**2)


for i in range(11):
    print(i**2)
print()


# Major difference in while and for loop 
# when u don't know where to stop like in for we already know the end point ....

count =0
while count < 5:
    print(count)
    count += 1
print()

# write a while loop that print even number  from 2 - 20
i=2
while i < 21:
    if i % 2== 0:
        print(i)
    else:    
        i+=1    

# i=2
# while i < 21:
#     if i % 2== 0:
#         print(i)        