# why we use function
# what is exception handling
# set of instruction / reusable block of code
# why we use retun keyword ? we use it only if we want to use that value somewhere else 


def add_num(a , b):
    c= a+b
    print(c)
    return c


total = add_num(3,5)
print(total)    

print()

# task 1
def square(n):
    sq= n*n
    return sq

print(square(2))
print(square(4))
print(square(8))





# task 2
# def greet(name):
#     msg = "Hello" , name ,"!"
#     print(msg)

# greet("Ali")    


def greet(name):
    print(f"Hello, {name}!")

greet("Ali")


# local vs global variables / function scope

x = 10 
def kuch_b_print_kaaro():
    y = 5
    print(x + y)

kuch_b_print_kaaro()


# try printing the local variables from outside the function an observe the error it produce 


x = 10 
def kuch_b_print_kaaro():
    y = 5
    x=10
    print(x + y)
    

kuch_b_print_kaaro()
# print(y)


# So why use lambda?

# The biggest reason is when you need a small function as an argument to another function.

# lambda
def square(n):
    return n*n

print(square(2))


square = lambda n: n*n 
print(square(2))


add = lambda a, b: a+b 
print(add(2,4))

# example 

students = [
    ("Ali", 25),
    ("Sara", 20),
    ("Ahmed", 23)
]

students.sort(key=lambda student: student[1])

print(students)



# multiplies two numbers and test it with two differnt pair of numbers


multlipiation = lambda a ,b : a * b
print(multlipiation(2 ,4))



# check number whether even as true or False



is_even = lambda n: n % 2 == 0
print(is_even(2))




# marks= 40
# remarks = "Pass" if marks >=40 else "Fail"
# print(remarks)


# why we use map ad filters
# it is only appliable on list
# when we want to go on every element of any data_structure 
# when we want to go on specific element


nums =[ 1,2,3,4,5]

squared = list(map(lambda x : x *x , nums))
print(squared)



evens = list(filter(lambda x: x % 2 == 0 , nums))
print(evens)


# nums = [1, 2, 3, 4, 5, 6]

# def is_even(x):
#     return x % 2 == 0

# evens = list(filter(is_even, nums))

# print(evens)


# map task
# use map convert a list of celsius temprature to fahrenheit
celsius =[ 10 , 20 , 30 ,40 ,50 ]
converted_temprature = list(map(lambda x : (x * 9/5 )+ 32 , celsius))


print(converted_temprature)
print()


# use filter  to keep only numbers greater than 10 from a list of your choice

num = [ 2, 5 , 7, 8 , 15 , 20, 50]

values = list(filter(lambda x: x > 10 , nums ))

print(values)


# nested function
def outer(text):
    def inner():
        print("Introduction" , text)

outer("Hi i am Mamoona")     

# task 1

# inner function that prints a formatted receipt line
def process_order(item):
    def print_receipt():
        print(f"Item ordered: {item}")

    print_receipt()


# Example Usage
process_order("Laptop")

# task 2
def process_order(item, price):
    def print_receipt():
        discount = price * 0.10
        final_price = price - discount
        print(f"Item: {item}")
        print(f"Original Price: ${price:.2f}")
        print(f"Discount (10%): ${discount:.2f}")
        print(f"Total Due: ${final_price:.2f}")

    print_receipt()



process_order("Laptop", 1000)


# home task
def analyze_numbers(nums):
    max_num=max(nums)
    min_num=min(nums)
    avg=sum(nums)/len(nums)
    return max_num , min_num ,avg


max, min, avg = analyze_numbers([10, 20, 30, 40, 50])
print(max , min, avg)


# result = 1
# def factorial(n):
#     if n >= 1:
#         result *=n
#         n +=n
#     print(n)

# factorial(5)


def factorial_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial_for(5))  