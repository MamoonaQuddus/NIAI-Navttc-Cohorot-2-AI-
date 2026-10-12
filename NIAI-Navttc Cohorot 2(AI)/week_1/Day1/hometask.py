# Operators

# Task one

a = 17
b = 5
c = 2

print(a%b)
print( a > b and  b > c ) 
print ((a + b) * c)
print(a ** c // b)
print(a % b == 0 or a % c == 0)
        
# Task 2
x = 10
y = 20

print(x)
x += 5
x *= 2
x -= y
x //= 3

# print(x += 5)
# print(x *= 2)
# print(x -= y)
# print(x //= 3)
print(x)


# print(x=x+5)
# print(x=x*2)
# print(x=x-y)
# print(x=x//3)

# slicing and indexing

text= "Python"
print(text[0])

print(text[0:5])


# Input & Type Casting
# Task 1

Name = input("Name")
Age = int(input("Age"))
Current_Year = int(input("currenr_year"))

year_50= Current_Year + (50- Age)    #50-24=26 ,2026 + 26=2052
print(f"{Name} will be turn 50 in {year_50}")

# task 2
# price= 120
# quatity= 2

price = float(input("price"))
quatity = int(input("quatity"))

total= price * quatity
discount = total * 0.10
final_price = total - discount

print(f"total {total} discount {discount} final_price {final_price}")
print(f"total: {total:.2f}, Discount: {discount:.2f}, Final Price: {final_price:.2f}")

# Data Types & Variables

x = 10
y = 10.0
z = "10"
a = True
b = [10]

# explain why false
print(x == y)
print(x == z)
print(x == a)
print(x is y)
print(x == b)

# Task 2
student_name = "Ali"
age = "21"
height = "5.8"
is_student = "True"
marks = ["85", "90", "78"]



# Strings & String Operations

text = "  Machine Learning is Amazing  "

# String

# task 1
text= " What is Machine learning "
print(len(text.split))
print(text.strip())
print(text.title())

# task 2
print(text.replace("Machine", "Deep"))
print("how" in text)




